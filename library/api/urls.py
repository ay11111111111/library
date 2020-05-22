from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('list/', views.book_list, name='list'),
    path('<int:pk>/', views.book_detail, name='detail'),
    path('create/', views.book_create, name='create'),
]


urlpatterns = format_suffix_patterns(urlpatterns)
