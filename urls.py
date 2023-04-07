from django.urls import path
from . import views
from register import views as register_views
from django.contrib.auth import views as auth_views
urlpatterns = [
   path('',views.Postlistview.as_view(),name='form_home'),
   path('post/<int:pk>/',views.Postdetailview.as_view(),name='post_detail'),
   path('post/new',views.Postcreateview.as_view(),name='post_create'),
   path('post/<int:pk>/update',views.Postupdateview.as_view(),name='post_update'),
   path('post/<int:pk>/delete',views.Postdeleteview.as_view(),name='post_delete'),
   path('about/',views.about,name='form_about'),
   path('login/',auth_views.LoginView.as_view(template_name='register/login.html'),name='login'),
   path('logout/',auth_views.LogoutView.as_view(template_name='register/logout.html'),name='logout'),
   path('register/',register_views.register,name='register_register'),
   path('profile/',register_views.profile,name='profile'),
   path('password-reset/',auth_views.PasswordResetView.as_view(template_name='register/password_reset.html'),name='password_reset'),
   path('password-reset/done',auth_views.PasswordResetDoneView.as_view(template_name='register/password_reset_done.html'),name='password_reset_done'),
   path('password-reset-confirm/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='register/password_reset_confirm.html'),name='password_reset_confirm')
]