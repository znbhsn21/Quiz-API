from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('questions/', views.get_questions, name = 'get_questions'),  
    path('add_questions/', views.add_questions, name = 'add_questions'),
    path('submit/', views.submit, name = 'submit'),
    path('register/', views.register_view, name="register"),
    path('token/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
]