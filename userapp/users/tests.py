from django.test import TestCase,client,Client
from django.urls import reverse

# Create your tests here.
class SignupTest(TestCase):
    def test_signup_without_username(self):
        """checks if username can be empty"""
        response=Client().post(reverse('users:signup'),{"username": "","first_name":"","last_name": "","email":"","password1":"","password2":""})
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"Did you forget to fill in your username?")
        
    def test_signup_with_two_unmatching_passwords(self):
        """doesn't create a user if two passwords provided don't match"""
        response=Client().post(reverse('users:signup'),{"username": "use2r","first_name":"","last_name": "","email":"","password1":"ashok12364","password2":"ashok13234"})
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"Passwords no match")
        
    def test_signup_with_right_credentials(self):
        """redirects to index page if right credentials are given"""
        response=Client().post(reverse('users:signup'),{"username": "user","first_name":"","last_name": "","email":"","password1":"ashok1234","password2":"ashok1234"})
        self.assertEqual(response.status_code,302)
        response1= self.client.get(reverse("users:index"))
        self.assertEqual(response1.status_code,302)

    def test_signup_with_invalid_but_matching_passwords(self):
        """shows validation errors if password does not satisfy the conditions"""
        response=Client().post(reverse('users:signup'),{"username": "user22","first_name":"","last_name": "","email":"","password1":"ashok","password2":"ashok"})
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"Passwords must contain")

class LoginTest(TestCase):
    def test_login_with_invalid_credentials(self):
        username = "love"
        password= "loveisgood69"
        Client().post(reverse('users:signup'),{"username": username,"first_name":"","last_name": "","email":"","password1":password,"password2":password})
        response=Client().post(reverse('users:login'),{"username": "randomUser", "password":password})
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"Invalid credentials")

    def test_login_with_invalid_credentials(self):
        username = "love"
        password= "loveisgood69"
        Client().post(reverse('users:signup'),{"username": username,"first_name":"","last_name": "","email":"","password1":password,"password2":password})
        response=Client().post(reverse('users:login'),{"username": username, "password":password})
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"Logged in")

class LogoutTest(TestCase):
    def test_logout(self):
        """logs out if log out link is clicked"""
        username = "love"
        password= "loveisgood69"
        Client().post(reverse('users:signup'),{"username": username,"first_name":"","last_name": "","email":"","password1":password,"password2":password})
        response= self.client.get(reverse('users:logout'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"Logged out")


class UserViewTest(TestCase):
    def test_with_user_not_logged_in(self):
        """if any user is not logged in currently, it redirects to login page"""
        response= self.client.get(reverse('users:index'))
        self.assertEqual(response.status_code,302)
