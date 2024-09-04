from django.test import TestCase
from .models import Task

class TaskListViewTests(TestCase):
    def setUp(self):
        Task.objects.create(title="Task 1", description="Test task 1", due_date="2024-09-05", priority=1, status="To Do")
        Task.objects.create(title="Task 2", description="Test task 2", due_date="2024-09-10", priority=2, status="Done")
    
    def test_filter_by_status(self):
        response = self.client.get('/tasks/?status=To Do')
        self.assertContains(response, "Task 1")
        self.assertNotContains(response, "Task 2")
    
    def test_sort_by_priority(self):
        response = self.client.get('/tasks/?sort_by=priority')
        tasks = response.context['tasks']
        self.assertEqual(tasks[0].title, "Task 1")
    
    def test_sort_by_due_date(self):
        response = self.client.get('/tasks/?sort_by=due_date')
        tasks = response.context['tasks']
        self.assertEqual(tasks[0].title, "Task 1")
