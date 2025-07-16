import unittest
import os

os.environ["TESTING"] = "true"

from app import app


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert '<title>Alana</title>' in html 
        assert '<menu class="menu-container">' in html
        assert '<header class="nav-bar">' in html
        assert '<div class="profile">' in html
        assert '<section id="about-me">' in html
        assert '<section id="work-experience">' in html
        assert '<section id="education">' in html
        assert '<div id="map">' in html
    
    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0
        post_data = {
            "name": "John Doe",
            "email": "johndoe@example.com",
            "content": "Hi, I\'m John Doe!"
        }
        post = self.client.post("/api/timeline_post", json=post_data)
        assert post.status_code == 200
        new_post = self.client.get("/api/timeline_post")
        new_post_json = new_post.get_json()
        assert len(new_post_json["timeline_posts"]) == 1
        first_post = new_post_json["timeline_posts"][0]
        assert first_post["name"] == "John Doe"
        assert first_post["email"] == "johndoe@example.com"
        assert first_post["content"] == "Hi, I\'m John Doe!"
        timeline_posts_html = response.get_data(as_text=True)
        assert '<h1>Timeline Posts</h1>' in timeline_posts_html 
        assert '<div class="form-wrapper">' in timeline_posts_html
        assert '<div id="posts-wrapper">' in timeline_posts_html