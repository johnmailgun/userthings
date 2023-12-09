from django.urls import path
from django.views.generic import TemplateView
from .views import user_login, user_logout, user_register, user_profile

app_name = "userthings"

urlpatterns = [
    path('login/', user_login , name="user_login"),
    path('logout/', user_logout , name="user_logout"),
    path('register/', user_register, name="user_register"),
    path('', user_profile , name="user_profile"),

]