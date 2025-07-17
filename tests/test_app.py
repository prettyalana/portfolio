import unittest
import os
os.environ['TESTING'] = 'true'

from app import app
class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>Alana</title>" in html
        assert "<h2>About me</h2>" in html
        assert "<h3>Fun Facts</h3>" in html
        assert "<h2>Previous Work Experience</h2>" in html
        assert "<h2>Education</h2>" in html
        assert 'https://api.mapbox.com/mapbox-gl-js/v3.12.0/mapbox-gl.css' in html
        assert 'https://api.mapbox.com/mapbox-gl-js/v3.12.0/mapbox-gl.js' in html

    def test_timeline(self):
        response = self.client.get("api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0

        post = self.client.post("/api/timeline_post", data={
            "name": "John Doe",
            "email": "john@example.com",
            "content": "Hello world, I\'m John!"
        })
        assert post.status_code == 200
        assert post.is_json
        post_data = post.get_json()
        assert post_data["name"] == "John Doe"
        assert post_data["email"] == "john@example.com"
        assert post_data["content"] == "Hello world, I\'m John!"
