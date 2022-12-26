from django.test import TestCase
from django.urls import reverse
from task_manager.statuses.models import Statuses
from task_manager.users.models import Users
from constants.statuses_constants import\
    CREATE_STATUS_SUCCESS_MESSAGE,\
    CHANGE_STATUS_SUCCESS_MESSAGE,\
    DELETE_STATUS_ERROR_MESSAGE,\
    DELETE_STATUS_SUCCESS_MESSAGE


class StatusesTestCase(TestCase):
    fixtures = ['statuses.json', 'users.json', 'tasks.json']

    def setUp(self):
        self.user = Users.objects.get(pk=1)
        self.status1 = Statuses.objects.get(pk=1)
        self.status2 = Statuses.objects.get(pk=2)

    def test_statuses_list(self):
        """Test statuses list"""
        self.client.force_login(self.user)
        response = self.client.get(reverse('statuses:statuses'))
        self.assertTemplateUsed(
            response,
            template_name='statuses/statuses.html',
        )
        statuses_list = list(response.context['statuses'])
        status1, status2 = statuses_list
        self.assertEqual(response.status_code, 200)
        self.assertEqual(status1.name, 'New')
        self.assertEqual(status2.name, 'Working')

    def test_create_status(self):
        """Test create status"""
        self.client.force_login(self.user)
        response = self.client.get(reverse('statuses:create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            template_name='create_edit_forms.html',
        )

        new_status = {'name': 'Testing'}
        response = self.client.post(
            path=reverse('statuses:create'),
            data=new_status,
            follow=True,
        )

        self.assertRedirects(response, '/ru/statuses/', status_code=302)

        self.assertContains(
            response,
            CREATE_STATUS_SUCCESS_MESSAGE,
            status_code=200,
        )
        new_status = Statuses.objects.get(id=3)
        self.assertEqual('Testing', new_status.name)

    def test_change_status(self):
        """Test change status"""
        status = self.status1
        self.client.force_login(self.user)
        response = self.client.get(reverse(
            'statuses:change',
            args=(status.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            template_name='create_edit_forms.html',
        )

        changed_status = {'name': 'Done'}
        response = self.client.post(
            reverse('statuses:change', args=(status.id,)),
            changed_status,
            follow=True,
        )

        self.assertRedirects(response, '/ru/statuses/', status_code=302)
        self.assertContains(
            response,
            CHANGE_STATUS_SUCCESS_MESSAGE
        )
        new_status = Statuses.objects.get(id=status.id)
        self.assertEqual('Done', new_status.name)

    def test_delete_status(self):
        """Test delete status"""
        status = self.status2
        self.client.force_login(self.user)
        response = self.client.get(reverse(
            'statuses:delete',
            args=(status.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            template_name='delete.html'
        )

        response = self.client.post(
            reverse(
                'statuses:delete',
                args=(status.id,)
            ),
            follow=True
        )
        with self.assertRaises(Statuses.DoesNotExist):
            Statuses.objects.get(pk=status.id)
        self.assertRedirects(response, '/ru/statuses/', status_code=302)
        self.assertContains(
            response,
            DELETE_STATUS_SUCCESS_MESSAGE
        )

    def test_delete_use_status(self):
        """Test delete use status"""
        status = self.status1
        self.client.force_login(self.user)
        response = self.client.get(reverse(
            'statuses:delete',
            args=(status.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            template_name='delete.html'
        )

        response = self.client.post(
            reverse(
                'statuses:delete',
                args=(status.id,)
            ),
            follow=True
        )
        self.assertTrue(Statuses.objects.get(pk=status.id))
        self.assertRedirects(response, '/ru/statuses/', status_code=302)
        self.assertContains(
            response,
            DELETE_STATUS_ERROR_MESSAGE
        )
