from django.urls import path
from .views import list_users, create_user, uptade_user, delete_user

#criação das urls do crud

urlpatterns = [
    path('', list_users, name='list_users'),
    path('new', create_user, name='create_user'),
    path('update/<int:id>/', update_user, name='update_user'),
    path('delete/<int:id>/', delete_user, name='delete_user'),
]
