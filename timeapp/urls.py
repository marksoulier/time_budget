# urls.py
from django.urls import path, re_path
from .views import signup, home, index, signout, login_view, send_test_email, test
from django.conf import settings
from .views import serve_react
from django.views.generic import TemplateView

urlpatterns = [
    # path('index/', TemplateView.as_view(template_name='index.html'), name='index'),
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    # path('index/', index, name='index'),
    path('signout/', signout, name='signout'),
    path('send-test-email/', send_test_email, name='send_test_email'),
    # Catch-all pattern for serving the React app
    # re_path(r"^(?P<path>.*)$", serve_react, {"document_root": settings.REACT_APP_BUILD_PATH}, name='index'),
]