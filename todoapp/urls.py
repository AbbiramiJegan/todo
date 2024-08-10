from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('delete/<int:id>/', views.delete_todo, name='delete_todo'),  # Delete a todo item
    path('finish/<int:id>/', views.mark_finished, name='mark_finished'),  # Mark a todo item as finished
]
