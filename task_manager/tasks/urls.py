from django.urls import  path
from . views import task_list, task_create
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', task_list, name='task_list'),
    path('task_create',task_create, name ='task_create')
]

urlpatterns += staticfiles_urlpatterns()
