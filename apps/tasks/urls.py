from django.urls import path, include
from .views import tasks, delete_task, get_tasks, update_task, new_page


urlpatterns = [
    path('', tasks, name='index'),
    path('delete_task/<int:task_id>/', delete_task, name='delete_task'),  
    path('create/', new_page, name='create_task'),  
    path('update/<int:task_id>/', update_task, name='update_task')
]