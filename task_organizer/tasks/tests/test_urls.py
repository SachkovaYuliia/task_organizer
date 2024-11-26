from django.urls import reverse, resolve
from tasks.views import task_list, add_task


def test_task_list_url():
    path = reverse('task_list')
    assert resolve(path).func == task_list


def test_add_task_url():
    path = reverse('add_task')
    assert resolve(path).func == add_task
