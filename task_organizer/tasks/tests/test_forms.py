import os
import django
import pytest
from datetime import date, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_organizer.settings')
django.setup()

from tasks.forms import TaskForm

pytestmark = pytest.mark.django_db


class TestTaskForm:
    def test_valid_form(self):
        form = TaskForm(data={
            'title': 'Test Task',
            'description': 'Description',
            'due_date': (date.today() + timedelta(days=1)).isoformat(),
        })
        assert form.is_valid() is True

    def test_empty_form(self):
        form = TaskForm(data={})
        assert form.is_valid() is False
        assert 'title' in form.errors
