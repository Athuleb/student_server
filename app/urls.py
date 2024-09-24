from django.urls import path
from .views import studentView

urlpatterns = [
    path('std/',studentView.as_view(),name='post'),
    path('std/<int:pk>',studentView.as_view())
]