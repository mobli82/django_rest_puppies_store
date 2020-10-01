from django.urls import path
from .views import get_post_puppies, get_delete_update_puppy

urlpatterns = [
    path('api/v1/puppies/<int:pk>/', get_delete_update_puppy, name='get-delete-update-puppy'),
    path('api/v1/puppies/', get_post_puppies, name='get-post-puppies'),
]
