import unittest
import os
os.environ['TESTING'] = 'true'

from app import app
class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        html = response.get_data(as_text=True)
        self.assertIn("<title>Alana</title>", html)
        self.assertIn("<h2>About me</h2>", html)
        self.assertIn("<h3>Fun Facts</h3>", html)
        self.assertIn("<h2>Previous Work Experience</h2>", html)
        self.assertIn("<h2>Education</h2>", html)
        self.assertIn("https://api.mapbox.com/mapbox-gl-js/v3.12.0/mapbox-gl.css", html)
        self.assertIn("https://api.mapbox.com/mapbox-gl-js/v3.12.0/mapbox-gl.js", html)

    def test_timeline(self):
        response = self.client.get("api/timeline_post")
        self.assertEqual(response.status_code, 200)
        assert response.is_json
        json = response.get_json()
        self.assertIn("timeline_posts", json)
        self.assertEqual(len(json["timeline_posts"]), 0)

        post = self.client.post("/api/timeline_post", data={
            "name": "John Doe",
            "email": "john@example.com",
            "content": "Hello world, I'm John!"
        })
        self.assertEqual(post.status_code, 200)
        assert post.is_json
        post_data = post.get_json()
        self.assertEqual(post_data["name"], "John Doe")
        self.assertEqual(post_data["email"], "john@example.com")
        self.assertEqual(post_data["content"], "Hello world, I'm John!")

        html_response = self.client.get("/timeline")
        self.assertEqual(html_response.status_code, 200)
        timeline_html = html_response.get_data(as_text=True)
        self.assertIn('<form id="form"', timeline_html)
        self.assertIn('<h1>Timeline Posts</h1>', timeline_html)
        self.assertIn('<div id="posts-wrapper">', timeline_html)

    def test_malformed_timeline_post(self):
        response = self.client.post("/api/timeline_post", data={"email": "john@example.com", "content": "Hello world, I'm John!"})
        self.assertEqual(response.status_code, 400)
        html = response.get_data(as_text=True)
        self.assertIn("Invalid name", html)

        response = self.client.post("/api/timeline_post", data={"name": "John Doe", "email": "john@example.com"})
        self.assertEqual(response.status_code, 400)
        html = response.get_data(as_text=True)
        self.assertIn("Invalid content", html)

        response = self.client.post("/api/timeline_post", data={"name": "John Doe", "content": "Hello world, I'm John!"})
        self.assertEqual(response.status_code, 400)
        html = response.get_data(as_text=True)
        self.assertIn("Invalid email", html)