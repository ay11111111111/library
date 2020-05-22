from django.urls import path
from . import views
from .views import (AuthorCreateView,
                    AuthorUpdateView,
                    AuthorDeleteView,
                    BookCreateView,
                    BookDetailView,
                    BookUpdateView,
                    BookDeleteView
                    )

urlpatterns = [
    path('', views.home, name='library-home'),
    path('about/', views.about, name='library-about'),
    path('author/create/', AuthorCreateView.as_view(), name='author-create'),
    path('author/<int:pk>/update/', AuthorUpdateView.as_view(), name='author-update'),
    path('author/<int:pk>/delete/', AuthorDeleteView.as_view(), name='author-delete'),
    path('book/create/', BookCreateView.as_view(), name='book-create'),
    path('book/<int:pk>', BookDetailView.as_view(), name='book-detail'),
    path('book/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('book/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]
