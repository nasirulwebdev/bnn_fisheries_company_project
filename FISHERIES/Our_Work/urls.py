from django.urls import path
from .views import our_work_list_view

urlpatterns = [
    path('', our_work_list_view, name='our_work'),
]
