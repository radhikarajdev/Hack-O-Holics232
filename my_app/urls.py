from django.urls import path
from .views import Dashboard,Login,Signup,Test,Contactus
urlpatterns = [
    path('dashboard/',Dashboard.as_view(),name="dashboard"),
    path('',Login.as_view(),name="login"),
    path('signup/',Signup.as_view(),name="signup"),
    path('dashboard/test/',Test.as_view(),name="test"),
    path('dashboard/contactus/',Contactus.as_view(),name="contactus"),
    ]