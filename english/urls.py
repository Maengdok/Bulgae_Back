from django.urls import path

from english.views import ListEnglishAPIView

urlpatterns = [
    path("", ListEnglishAPIView.as_view(), name="english_list")
]