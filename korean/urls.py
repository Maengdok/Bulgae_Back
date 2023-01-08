from django.urls import path

from korean.views import KoreanViewSet

urlpatterns = [
    path("", KoreanViewSet.korean_list, name="get_korean_list"),
    path("<int:korean_id>", KoreanViewSet.get_korean, name="get_korean"),
    path("add", KoreanViewSet.add_korean, name="add_korean"),
    path("update", KoreanViewSet.update_korean, name="update_korean"),
    path("delete/<int:korean_id>", KoreanViewSet.delete_korean, name="delete_korean"),
]
