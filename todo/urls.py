from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('delete/<list_id>', views.delete, name='delete'),
    path('done/<list_id>', views.done, name='done'),
    path('undone/<list_id>', views.undone, name='undone'),
    path('edit/<list_id>', views.edit, name='edit'),
]
