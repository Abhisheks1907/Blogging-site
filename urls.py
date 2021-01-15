from django.urls import path
from . import views
from .views import PostListView , PostDetailView , PostCreateView , UserPostListView
from django.contrib.auth import views as auth_views



urlpatterns=[
    path('',views.index,name='index'),
    path('login',views.login_view,name='login'),
    path('register',views.register,name="Login now"),
    path('logout',views.logout_view,name='logout'),
    path('profile', views.profile,name='profile'),
    path('home',PostListView.as_view(),name='home'),
    path('edit_profile',views.profile_change,name='profile_change'),
    path('post/<int:pk>/',PostDetailView.as_view(),name ='post-detail'),
    path('post/new/',PostCreateView.as_view(),name ='post-create'),
    # path('profile',profile_list_view.as_view(),name ='Profile'),
    path('user/<str:username>',UserPostListView.as_view(),name='user-posts'),
    path('password_reset',
        auth_views.PasswordResetView.as_view(template_name='password_reset.html'),
        name='password_reset'),

    path('password_reset/done',
        auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        name='password_reset_done'),

    path('password_reset_confirm/<uid64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_done.html'),
        name='password_reset_confirm'),
    


    # path('password_change/',
    # auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
    # name='password_change'),

    # path('password_change/done',
    # auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
    # name='password_change_done'),


    
]