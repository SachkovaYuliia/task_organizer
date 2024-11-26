from tasks.models import Task
from datetime import date, timedelta
import pytest


@pytest.mark.django_db
def test_task_str():
    task = Task.objects.create(
        title='Sample Task',
        description='Description',
        due_date=(date.today() + timedelta(days=1))
    )
    assert str(task) == 'Sample Task'
