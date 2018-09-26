import unittest
from api.models import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User(2, "maria", "mimi", "mary", "maria@gmail.com", "1234")

    def test_user_id(self):
        # Tests that the user_id is equal to the given user_id
        self.assertEqual(self.user.user_id, 2, "user_id must be 1")
        self.user.user_id = 4
        self.assertEqual(self.user.user_id, 4, "user_id is now 4")

    def test_firstname(self):
        # Tests that the date_added is equal to the given date
        self.assertEqual(self.user.first_name, "maria")

    def test_last_name(self):
        # Tests that the entry text is equal to the given content
        self.assertEqual(self.user.last_name, "mimi")
        self.user.last_name = "sandra"
        self.assertEqual(self.user.last_name, "sandra", "last name has changed to\
        sandra")
    
    def test_username(self):
        self.assertEqual(self.user.user_name, "mary")
    
    def test_email(self):
        self.assertEqual(self.user.email, "maria@gmail.com")
        self.user.email = "sandra@yahoo.com"
        self.assertEqual(self.user.email, "sandra@yahoo.com")
    
    def test_password(self):
        self.assertEqual(self.user.password, "1234")

    def test_class_instance(self):
        # Tests that the defined object is an instance of a class
        self.assertIsInstance(self.user, User)
