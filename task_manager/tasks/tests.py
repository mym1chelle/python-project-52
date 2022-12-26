from django.test import TestCase
from django.urls import reverse
from task_manager.tasks.models import Tasks
from task_manager.users.models import Users
from constants.tasks_constants import\
    CREATE_TASK_SUCCESS_MESSAGE,\
    CHANGE_TASK_SUCCESS_MESSAGE,\
    DELETE_TASK_ERROR_MESSAGE,\
    DELETE_TASK_SUCCESS_MESSAGE


class StatusesTestCase(TestCase):
    fixtures = ['users.json', 'statuses.json', 'tasks.json']

    def setUp(self):
        self.user1 = Users.objects.get(pk=1)
        self.user2 = Users.objects.get(pk=2)
        self.task1 = Tasks.objects.get(pk=1)
        self.task2 = Tasks.objects.get(pk=2)
        self.task3 = Tasks.objects.get(pk=3)

    def test_tasks_list(self):
        """Test tasks list"""
        self.client.force_login(self.user1)
        response = self.client.get(reverse('tasks:tasks'))
        self.assertTemplateUsed(
            response,
            template_name='tasks/tasks.html',
        )
        statuses_list = list(response.context['tasks'])
        task1, task2, task3 = statuses_list
        self.assertEqual(response.status_code, 200)
        self.assertEqual(task1.name, 'Destroy wall Maria')
        self.assertEqual(task2.name, 'Destroy Wall Rosa')
        self.assertEqual(task3.name, "Infiltrate Liberio's camp")


    def test_create_task(self):
        """Test create task"""
        self.client.force_login(self.user1)
        response = self.client.get(reverse('statuses:create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            template_name='create_edit_forms.html',
        )

        new_task = {
            'name': 'Destroy Paradise Island',
            'description': 'Destroy Paradise Island and all the people who live on it',
            'status': 1,
            'created_by': 1,
            'executor': 3,
        }
        response = self.client.post(
            path=reverse('tasks:create'),
            data=new_task,
            follow=True,
        )

        self.assertRedirects(response, '/ru/tasks/', status_code=302)

        self.assertContains(
            response,
            CREATE_TASK_SUCCESS_MESSAGE,
            status_code=200,
        )
        new_task = Tasks.objects.get(id=4)
        self.assertEqual('Destroy Paradise Island', new_task.name)
        self.assertEqual('Destroy Paradise Island and all the people who live on it', new_task.description)
        self.assertEqual('New', new_task.status.name)
        self.assertEqual('Zeke Yeager', new_task.created_by.get_full_name())
        self.assertEqual('Bertholdt Hoover', new_task.executor.get_full_name())

    def test_change_task(self):
        """Test change task"""
        task = self.task1
        self.client.force_login(self.user1)
        response = self.client.get(reverse(
            'tasks:update',
            args=(task.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            template_name='create_edit_forms.html',
        )

        changed_task = {
            'name': 'Carry out an easy death plan',
            'description': 'Make all the inhabitants of Paradise Island sterile',
            'status': 2,
            'executor': 1,
        }
        response = self.client.post(
            reverse('tasks:update', args=(task.id,)),
            changed_task,
            follow=True,
        )

        self.assertRedirects(response, '/ru/tasks/', status_code=302)
        self.assertContains(
            response,
            CHANGE_TASK_SUCCESS_MESSAGE
        )
        new_task = Tasks.objects.get(id=task.id)
        self.assertEqual('Carry out an easy death plan', new_task.name)
        self.assertEqual('Make all the inhabitants of Paradise Island sterile', new_task.description)
        self.assertEqual('Working', new_task.status.name)
        self.assertEqual('Eren Yeager', new_task.created_by.get_full_name())
        self.assertEqual('Zeke Yeager', new_task.executor.get_full_name())

    def test_delete_task_by_anothe_user(self):
        """Test task delete by another user"""
        task = self.task1
        self.client.force_login(self.user1)
        response = self.client.get(reverse(
            'tasks:delete', args=(task.id,))
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            template_name='delete.html',
        )
        response = self.client.post(reverse(
            'tasks:delete', args=(task.id,)),
            follow=True
        )

        self.assertTrue(Tasks.objects.get(pk=task.id))
        self.assertRedirects(response, '/ru/tasks/', status_code=302)
        self.assertContains(
            response,
            DELETE_TASK_ERROR_MESSAGE,
        )

    def test_delete_task(self):
        """Test task delete """
        task = self.task1
        self.client.force_login(self.user2)
        response = self.client.get(reverse(
            'tasks:delete', args=(task.id,))
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            template_name='delete.html',
        )
        response = self.client.post(reverse(
            'tasks:delete', args=(task.id,)),
            follow=True
        )
        with self.assertRaises(Tasks.DoesNotExist):
            Tasks.objects.get(pk=task.id)
        self.assertRedirects(response, '/ru/tasks/', status_code=302)
        self.assertContains(
            response,
            DELETE_TASK_SUCCESS_MESSAGE,
        )
