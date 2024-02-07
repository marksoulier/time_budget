# urls.py
from django.urls import path
from .views import signup, home, index, signout, login_view, send_test_email, test, serve_react
from django.conf import settings
from django.urls import re_path


urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    re_path("index/", serve_react, {"document_root": settings.REACT_APP_BUILD_PATH}, name='index'),
    path('signout/', signout, name='signout'),
    path('send-test-email/', send_test_email, name='send_test_email'),
]