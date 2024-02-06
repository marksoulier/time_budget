# urls.py
from django.urls import path
from .views import signup, home, index, signout, login_view, send_test_email, test

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('index/', index, name='index'),
    path('signout/', signout, name='signout'),
    path('send-test-email/', send_test_email, name='send_test_email'),
]