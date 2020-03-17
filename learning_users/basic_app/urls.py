from django.urls import path
from . import views
from django.conf.urls import url

# SET THE NAMESPACE!
app_name = 'basic_app'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url('register/',views.register,name='register'),
    url('user_login',views.user_login,name='user_login')
]
