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
        # TODO Add more tests relating to the /api/timeline_post GET and POST apis
        # TODO Add more tests relating to the timeline page