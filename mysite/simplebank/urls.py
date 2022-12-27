from django.urls import path

from .views import homePageView, addView, loginView, logoutView, loginActionView

urlpatterns = [
    path('', homePageView, name='home'),
    path('add/', addView, name='add'),
	path('login/', loginView, name='login'),
	path('logout/', logoutView, name='logout'),
    path('login/loginAction/', loginActionView, name='loginAction')
]
