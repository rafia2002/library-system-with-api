from django.urls import path
from . import views

app_name='userapp'

urlpatterns=[
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('home/',views.user_home,name='home'),
    path('download/<int:book_id>/',views.download_book,name='download'),
]