from django.urls import path
from .views import event_list_view

urlpatterns = [
    path('', event_list_view, name='events'),
]
