from django.test import TestCase
from django.urls import reverse

from task_manager.users.models import Users
from task_manager.constants import *


class UserTestCase(TestCase):
    fixtures = ['users.json', ]

    def setUp(self):
        self.user1 = Users.objects.get(pk=1)
        self.user2 = Users.objects.get(pk=2)
        self.user3 = Users.objects.get(pk=3)

    def test_users_list(self):
        """Test users list"""
        response = self.client.get(reverse('users'))
        self.assertTemplateUsed(
            response,
            template_name='users.html',
        )
        users_list = list(response.context['users'])
        user1, user2, user3 = users_list
        self.assertEqual(response.status_code, 200)
        self.assertEqual(user1.username, 'beasttitan')
        self.assertEqual(user1.first_name, 'Zeke')
        self.assertEqual(user1.last_name, 'Yeager')
        self.assertEqual(user2.username, 'attacktitan')
        self.assertEqual(user2.first_name, 'Eren')
        self.assertEqual(user2.last_name, 'Yeager')
        self.assertEqual(user3.username, 'excollosaltitan')
        self.assertEqual(user3.first_name, 'Bertholdt')
        self.assertEqual(user3.last_name, 'Hoover')

    def test_create_user(self):
        """Test create user"""
        response = self.client.get(reverse('create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            template_name='create_edit_forms.html',
        )

        new_user = {
            'first_name': 'Reiner',
            'last_name': 'Braun',
            'username': 'armoredtitan',
            'password1': 'qwertyklaskdlkasldkalkdlaksldkaslkdajdlsajdas12312',
            'password2': 'qwertyklaskdlkasldkalkdlaksldkaslkdajdlsajdas12312',
        }
        response = self.client.post(
            path=reverse('create'),
            data=new_user,
            follow=True,  # will reach the last redirect
        )

        self.assertRedirects(response, '/ru/login/', status_code=302)

        self.assertContains(
            response,
            CREATE_USER_SUCCESS_MESSAGE,
            status_code=200,
        )
        new_user = Users.objects.get(username=new_user['username'])
        self.assertEqual('Reiner', new_user.first_name)
        self.assertEqual('Braun', new_user.last_name)
        self.assertTrue(new_user.check_password('qwertyklaskdlkasldkalkdlaksldkaslkdajdlsajdas12312'))

    def test_change_user(self):
        """Test change user"""
        user = self.user3
        self.client.force_login(Users.objects.get(pk=user.id))
        response = self.client.get(reverse('change', args=(user.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            template_name='create_edit_forms.html',
        )

        changed_user = {
            'first_name': 'Armin',
            'last_name': 'Arlert',
            'username': 'newcollosaltitan',
            'password1': 'q1w2e3r4aldklasdklakdlakdlaksldkallawja',
            'password2': 'q1w2e3r4aldklasdklakdlakdlaksldkallawja',
        }
        response = self.client.post(
            reverse('change', args=(user.id,)),
            changed_user,
            follow=True,
        )

        self.assertRedirects(response, '/ru/users/', status_code=302)
        self.assertContains(
            response,
            CHANGE_USER_SUCCESS_MESSAGE
        )
        new_user = Users.objects.get(username=changed_user['username'])
        self.assertEqual('Armin', new_user.first_name)
        self.assertEqual('Arlert', new_user.last_name)
        self.assertTrue(new_user.check_password('q1w2e3r4aldklasdklakdlakdlaksldkallawja'))

    def test_change_by_another_user(self):
        """Test user change by another user"""
        user1 = self.user1
        user2 = self.user2
        self.client.force_login(Users.objects.get(pk=user1.id))
        response = self.client.get(reverse('change', args=(user2.id,)), follow=True)
        self.assertRedirects(response, '/ru/users/', status_code=302)
        self.assertContains(
            response,
            CHANGE_USER_ERROR_MESSAGE,
        )

    def test_delete_by_another_user(self):
        """Test user delete by another user"""
        user1 = self.user1
        user2 = self.user2
        self.client.force_login(Users.objects.get(pk=user1.id))
        response = self.client.get(reverse('delete', args=(user2.id,)), follow=True)
        self.assertRedirects(response, '/ru/users/', status_code=302)
        self.assertContains(
            response,
            CHANGE_USER_ERROR_MESSAGE,
        )
