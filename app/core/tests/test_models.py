from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test models"""

    def test_create_user_with_email_successful(self):
        email = 'singh.dvya05@gmail.com'
        password = 'test@123'
        user = get_user_model().objects.create_user(
            email = email,
            password = password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        sample_emails = [
            ['singh1.dvya05@gmail.com', 'singh1.dvya05@gmail.com'],
            ['Singh2.dvya05@gmail.com', 'Singh2.dvya05@gmail.com'],
            ['SINGH3.DVYA05@GMAIL.COM', 'SINGH3.DVYA05@gmail.com'],
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample1')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'singh.dvya05')

    def test_create_superuser(self):
        user = get_user_model().objects.create_superuser(
            'singh.dvya05@gmail.com',
            'test123',
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)           