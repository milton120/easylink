from faker import Faker

from django.urls import reverse

from common.test_case import EasyLinkTestCase


class MeDetailAPITest(EasyLinkTestCase):
    url = reverse('me-details')

    def test_login_user_details_get(self):
        # ===========================================
        #  Check without login
        # ===========================================
        request = self.client.get(self.url)
        self.assertUnAuthorized(request)

        # ===========================================
        #  Check with login
        # ===========================================
        login = self.client.login(email=self.user.email, password='testpass')
        self.assertTrue(login)

        request = self.client.get(self.url)
        self.assertSuccess(request)
        # check if it is the same user
        self.assertEqual(request.data['id'], self.user.pk)

        # ===========================================
        #  Check for admin user
        # ===========================================
        self.user.is_staff = True
        self.user.save()
        request = self.client.get(self.url)
        self.assertSuccess(request)
        # check if it is the same user
        self.assertEqual(request.data['id'], self.user.pk)

        # logout
        self.client.logout()


class PasswordResetTest(EasyLinkTestCase):
    url = reverse('password_reset')
    fake = Faker()

    def test_password_reset(self):

        # ===========================================
        #  Check for a random email
        # ===========================================
        data = {
            'email': self.fake.email()
        }
        request = self.client.post(self.url, data)
        self.assertDeleted(request)

        # ===========================================
        #  Check with an invalid email
        # ===========================================

        data = {
            'email': self.fake.ssn()
        }
        request = self.client.post(self.url, data)
        self.assertBadRequest(request)

        # ===========================================
        #  Check for a valid email
        # ===========================================
        data = {
            'email': self.fake.email()
        }
        request = self.client.post(self.url, data)
        self.assertDeleted(request)

        # ===========================================
        #  Check for a logged in user
        # ===========================================
        login = self.client.login(email=self.user.email, password='testpass')
        self.assertTrue(login)
        data = {
            'email': self.user.email
        }
        request = self.client.post(self.url, data)
        self.assertDeleted(request)

        # ===========================================
        #  Check for admin user
        # ===========================================
        self.user.is_staff = True
        self.user.save()
        data = {
            'email': self.user.email
        }
        request = self.client.post(self.url, data)
        self.assertDeleted(request)


class SetPasswordTest(EasyLinkTestCase):
    url = reverse('set_password')

    def test_password_set(self):
        # ===========================================
        #  Check without logged in
        # ===========================================
        data = {
            'new_password': 'newtestpass',
            're_new_password': 'newtestpass',
            'current_password': 'testpass'
        }
        request = self.client.post(self.url, data)
        self.assertUnAuthorized(request)

        # ===========================================
        #  Check for the logged in users
        # ===========================================
        # login
        login = self.client.login(email=self.user.email, password='testpass')
        self.assertTrue(login)
        # now change the password
        data = {
            'new_password': 'newtestpass',
            're_new_password': 'newtestpass',
            'current_password': 'testpass'
        }
        request = self.client.post(self.url, data)
        self.assertDeleted(request)
        # now logout
        self.client.logout()
        # login again using the new password
        login = self.client.login(
            email=self.user.email, password='newtestpass')
        self.assertTrue(login)

        # now check with a wrong password
        data = {
            'new_password': 'testpass',
            're_new_password': 'testpass',
            'current_password': 'wrongpassword'
        }
        request = self.client.post(self.url, data)
        self.assertBadRequest(request)
        # now logout
        self.client.logout()

        # ===========================================
        #  Check for admin user
        # ===========================================
        self.user.is_superuser = True
        self.user.is_staff = True
        self.user.save()
        login = self.client.login(email=self.user.email, password='testpass')
        self.assertTrue(login)
        data = {
            'new_password': 'newtestpass',
            're_new_password': 'newtestpass',
            'current_password': 'testpass'
        }
        request = self.client.post(self.url, data)
        self.assertDeleted(request)
