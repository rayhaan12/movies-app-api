from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_success(self):
        """Test creating a new user with an email is successful"""
        email = 'test@mail.com'
        username = 'Tester97'
        password = 'testpass'

        user = get_user_model().objects.create_user(
            email=email,
            username=username,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertEqual(user.username, username)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test that the user email has been normalized"""
        email = 'test@MaIl.com'
        username = 'Tester97'
        password = 'testpass'

        user = get_user_model().objects.create_user(
            email=email,
            username=username,
            password=password
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating a user with no email raises an error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=None,
                username="Tester97",
                password="testpass"
            )

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            email='test@mail.com',
            username='Tester97',
            password='testpass'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
