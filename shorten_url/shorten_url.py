from django.urls import path
from . import views

urlpatterns = [
    path('<path:shortened_url>/', views.get_original_url, name='redirect_original_url'),
]