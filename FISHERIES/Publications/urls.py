from django.urls import path
from .views import publication_list_view

urlpatterns = [
    path('', publication_list_view, name='publications'),
]
