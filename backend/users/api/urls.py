from django.urls import path, include
from.views import UserRegisterApi, LoginApi, UserUpdateApi, UserApi
from knox import views as knox_view

urlpatterns = [
    path('user/', UserApi.as_view()),
    path('register/', UserRegisterApi.as_view()),
    path('update/', UserUpdateApi.as_view()),
    path('login/', LoginApi.as_view()),
    path('logout/', knox_view.LogoutView.as_view())
]
