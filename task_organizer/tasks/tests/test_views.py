from django.urls import reverse
from tasks.models import Task
from datetime import date, timedelta
import pytest


@pytest.mark.django_db
class TestTaskViews:
    def test_task_list_view(self, client):
        response = client.get(reverse('task_list'))
        assert response.status_code == 200

    def test_add_task_valid(self, client):
        data = {
            'title': 'New Task',
            'description': 'Description',
            'due_date': (date.today() + timedelta(days=1)).isoformat(),
        }
        response = client.post(reverse('add_task'), data)
        assert response.status_code == 302
        assert Task.objects.filter(title='New Task').exists()
