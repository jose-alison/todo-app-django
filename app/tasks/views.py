from typing import Any
from django.views.generic import ListView

from . import models

class TaskListView(ListView):
    model = models.Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'


    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        data = super().get_context_data(**kwargs)
        print(data)
        return data
