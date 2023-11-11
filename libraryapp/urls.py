from django.urls import path
from libraryapp import views

urlpatterns = [
        path('indexpage/',views.indexpage,name="indexpage"),
        path('books/', views.books, name="books"),
        path('savebook/', views.savebook, name="savebook"),
        path('addbooks/', views.addbooks, name="addbooks"),
        path('loginpage/', views.loginpage, name="loginpage"),
        path('bookdetails/<int:bookid>/', views.bookdetails, name="bookdetails"),

]