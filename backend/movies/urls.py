# backend/movies/urls.py
from django.urls import path
from .views import EmotionBasedRecommendation

urlpatterns = [
    path("smart-recommend/", EmotionBasedRecommendation.as_view()),
]
