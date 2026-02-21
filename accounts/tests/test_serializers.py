from django.test import TestCase
from accounts.serializers import UserSerializer

class RegistrationSerializer(TestCase):

    def test_create_user(self):
        data = {
            "username": "marco",
            "email": "marco@home.com",
            "password": "strongpassword123",
        }

        serializer = UserSerializer(data=data)
        self.assertTrue(serializer.is_valid())

        user = serializer.save()

        self.assertEqual(user.username, "marco")

        self.assertTrue(user.check_password(data["strongpassword123"]))


    def test_password_not_in_response(self):
        data = {
            "username": "marco",
            "email": "marco@home.com",
            "password": "strongpassword123",
        }

        serializer = UserSerializer(data=data)
        serializer.is_valid()
        user = serializer.save()

        serialized_data = RegistrationSerializer(user)
        self.assertNotIn("password", serialized_data)


