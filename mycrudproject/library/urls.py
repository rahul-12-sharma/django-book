from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Map root URL to home view
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('add/', views.add_book, name='add_book'),
    path('books/', views.book_list, name='book-list'),
    path('edit/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete/<int:pk>/', views.delete_book, name='delete_book'),
]
