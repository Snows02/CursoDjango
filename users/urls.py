"""Users URLs."""

# Django
from django.urls import path

# Views
from users import views

urlpatterns = [

    # Management
    path(
        route='login/',
        view=views.LoginView.as_view(),
        name='login'
    ),
    path(
        route='logout/',
        view=views.Logout.as_view(),
        name='logout'
    ),
    path(
        route='signup/',
        view=views.SingupView.as_view(),
        name='signup'
    ),
    path(
        route='me/profile/',
        view=views.ProfileUpdateView.as_view(),
        name='update'
    ),

    # Posts
    path(
        route='<str:username>/',
        view=views.UserDetailView.as_view(),
        name='detail'
    )
]
