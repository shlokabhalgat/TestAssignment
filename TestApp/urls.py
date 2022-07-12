from django.urls import path
from . import views

app_name = "main"


urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
    path("thought_post", views.post_create, name="thought_post"),
    path("dashboard", views.view_posts, name="dashboard"),
]