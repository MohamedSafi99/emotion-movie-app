# config/urls.py

from django.contrib import admin
from django.urls import path
from movies.views import SmartRecommendView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/smart-recommend/', SmartRecommendView.as_view()),
]
