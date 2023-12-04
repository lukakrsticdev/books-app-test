from django.urls import include, path
from .authentication import urls as auth_urls
from .views import (
    MyBooksApiView, 
    MyBooksDetailApiView
)

urlpatterns = [
    path('auth/', include(auth_urls)),
    path('mybooks/', MyBooksApiView.as_view()),
    path('mybooks/<int:book_id>', MyBooksDetailApiView.as_view())
]