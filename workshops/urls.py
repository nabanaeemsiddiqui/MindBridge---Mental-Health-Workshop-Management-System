from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name='home'),

    path('signup/', views.signup, name='signup'),

    path(
        'login/',
        LoginView.as_view(template_name='login.html'),
        name='login'
    ),

    path(
        'logout/',
        LogoutView.as_view(next_page='home'),
        name='logout'
    ),

    path('enroll/<int:workshop_id>/', 
         views.enroll, 
         name='enroll'),
    
    path(
    'my-workshops/',
    views.my_workshops,
    name='my_workshops'
),

path(
    'feedback/<int:workshop_id>/',
    views.give_feedback,
    name='feedback'
),

]