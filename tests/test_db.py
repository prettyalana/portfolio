import unittest
from peewee import *

from app import TimelinePost

MODELS = [TimelinePost]

test_db = SqliteDatabase(":memory:")


class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)

        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        test_db.drop_tables(MODELS)

        test_db.close()

    def test_timeline_post(self):
        first_post = TimelinePost.create(
            name="John Doe", email="john@example.com", content="Hello world, I'm John!"
        )
        self.assertEqual(first_post.id, 1)
        second_post = TimelinePost.create(
            name="Jane Doe", email="jane@example.com", content="Hello world, I'm Jane!"
        )
        self.assertEqual(second_post.id, 2)

        first_post = TimelinePost.get(TimelinePost.id == 1)
        self.assertEqual(first_post.name, "John Doe")
        self.assertEqual(first_post.email, "john@example.com")
        self.assertEqual(first_post.content, "Hello world, I'm John!")
        second_post = TimelinePost.get(TimelinePost.id == 2)
        self.assertEqual(second_post.name, "Jane Doe")
        self.assertEqual(second_post.email, "jane@example.com")
        self.assertEqual(second_post.content, "Hello world, I'm Jane!")
