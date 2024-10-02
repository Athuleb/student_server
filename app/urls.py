from django.urls import path
from .views import studentView, GradingView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('std/', studentView.as_view()),  # For listing and creating students
    path('std/<int:pk>/', studentView.as_view()),  # For retrieving, updating, and deleting students by id
    path('grade/', GradingView.as_view(), name='grading'),  # Grading route
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
