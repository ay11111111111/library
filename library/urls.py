from django.urls import path
from . import views
from .views import PostCreateView

urlpatterns = [
    path('', views.home, name='library-home'),
    path('about/', views.about, name='library-about'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
]
