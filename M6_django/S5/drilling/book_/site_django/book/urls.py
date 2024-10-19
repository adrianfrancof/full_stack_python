from django.urls import path
from . import views
from .views import IndexPageView

urlpatterns = [
    path('', IndexPageView.as_view(),name="index"),
]