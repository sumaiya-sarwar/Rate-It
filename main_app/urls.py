from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('books/', views.Booklist.as_view(), name="booklist"),
    path('books/new', views.BookCreate.as_view(), name="book_create"),
    path('books/<int:pk>/', views.Bookdetails.as_view(), name="bookdetails"),
    path('books/<int:pk>/update', views.BookUpdate.as_view(), name="book_update"),
    path('books/<int:pk>/delete',views.BookDelete.as_view(), name="book_delete"),
    path('favorites/<int:pk>/books/<int:book_pk>', views.FavoritesListAssoc.as_view(), name="favorites"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
]
