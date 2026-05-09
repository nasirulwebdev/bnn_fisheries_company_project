from django.urls import path
from . import views

urlpatterns = [
    path('', views.notice_list, name='notice_list'),

    path(
        'details/<int:id>/',
        views.notice_detail,
        name='notice_detail'
    ),
]