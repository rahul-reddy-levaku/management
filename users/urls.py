from .views import login_view, logout_view, dashboard_view
from . import views
from django.urls import path
from .views import home_view

urlpatterns = [
    path('', home_view, name='home'),  # Home page URL pattern
    path('dashboard/', views.dashboard, name='dashboard'),
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),  # Dashboard URL pattern
    # Other URL patterns
]
