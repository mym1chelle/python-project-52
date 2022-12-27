from django.test import TestCase
from django.urls import reverse
from task_manager.tasks.models import Tasks
from task_manager.users.models import Users
from task_manager.labels.models import Labels
from task_manager.statuses.models import Statuses
from constants.labels_constants import\
    CREATE_LABEL_SUCCESS_MESSAGE,\
    CHANGE_LABEL_SUCCESS_MESSAGE,\
    DELETE_LABEL_SUCCESS_MESSAGE,\
    DELETE_LABEL_ERROR_MESSAGE


class StatusesTestCase(TestCase):
    fixtures = [
        'users.json',
        'statuses.json',
        'tasks.json',
        'labels.json',
        'tasklabelrelation.json'
    ]

    def setUp(self):
        self.user = Users.objects.get(pk=1)

        self.status1 = Statuses.objects.get(pk=1)
        self.status2 = Statuses.objects.get(pk=2)

        self.task1 = Tasks.objects.get(pk=1)
        self.task2 = Tasks.objects.get(pk=2)
        self.task3 = Tasks.objects.get(pk=3)

        self.label1 = Labels.objects.get(pk=1)
        self.label2 = Labels.objects.get(pk=2)
        self.label3 = Labels.objects.get(pk=3)
        self.label4 = Labels.objects.get(pk=4)

    def test_labels_list(self):
        """Test labels list"""
        self.client.force_login(self.user)
        response = self.client.get(reverse('labels:labels'))
        self.assertTemplateUsed(
            response,
            template_name='labels/labels.html',
        )
        labels_list = list(response.context['labels'])
        label1, label2, label3, label4 = labels_list
        self.assertEqual(response.status_code, 200)
        self.assertEqual(label1.name, 'label one')
        self.assertEqual(label2.name, 'label two')
        self.assertEqual(label3.name, 'label three')
        self.assertEqual(label4.name, 'label four')

    def test_create_label(self):
        """Test create label"""
        self.client.force_login(self.user)
        response = self.client.get(reverse('labels:create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            template_name='create_edit_forms.html',
        )

        new_label = {'name': 'label five'}
        response = self.client.post(
            path=reverse('labels:create'),
            data=new_label,
            follow=True,
        )

        self.assertRedirects(response, '/labels/', status_code=302)

        self.assertContains(
            response,
            CREATE_LABEL_SUCCESS_MESSAGE,
            status_code=200,
        )
        new_label = Labels.objects.get(id=5)
        self.assertEqual('label five', new_label.name)

    def test_change_label(self):
        """Test change label"""
        label = self.label1
        self.client.force_login(self.user)
        response = self.client.get(reverse(
            'labels:update',
            args=(label.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            template_name='create_edit_forms.html',
        )

        changed_label = {'name': 'Changed label'}
        response = self.client.post(
            reverse('labels:update', args=(label.id,)),
            changed_label,
            follow=True,
        )

        self.assertRedirects(response, '/labels/', status_code=302)
        self.assertContains(
            response,
            CHANGE_LABEL_SUCCESS_MESSAGE
        )
        new_label = Labels.objects.get(id=label.id)
        self.assertEqual('Changed label', new_label.name)

    def test_delete_label(self):
        """Test label delete """
        label = self.label2
        self.client.force_login(self.user)
        response = self.client.get(reverse(
            'labels:delete', args=(label.id,))
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            template_name='delete.html',
        )
        response = self.client.post(reverse(
            'labels:delete', args=(label.id,)),
            follow=True
        )
        with self.assertRaises(Labels.DoesNotExist):
            Labels.objects.get(pk=label.id)
        self.assertRedirects(response, '/labels/', status_code=302)
        self.assertContains(
            response,
            DELETE_LABEL_SUCCESS_MESSAGE,
        )

    def test_delete_a_use_label(self):
        """Test a use label delete """
        label = self.label3
        self.client.force_login(self.user)
        response = self.client.get(reverse(
            'labels:delete', args=(label.id,))
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            template_name='delete.html'
        )
        response = self.client.post(reverse(
            'labels:delete', args=(label.id,)),
            follow=True
        )
        self.assertTrue(Labels.objects.get(id=label.id))
        self.assertRedirects(response, '/labels/', status_code=302)
        self.assertContains(
            response,
            DELETE_LABEL_ERROR_MESSAGE
        )
