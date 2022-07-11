from django.urls import path, include
from .views import SignUpView

app_name = 'accounts'

urlpatterns = [
    path('/', include('django.contrib.auth.urls')),
    path('/register', SignUpView.as_view(), name='register'),
]
