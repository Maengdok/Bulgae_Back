from django.urls import path

from english.views import EnglishViewSet

urlpatterns = [
    path("", EnglishViewSet.english_list, name="get_english_list"),
    path("<int:english_id>", EnglishViewSet.get_english, name="get_english"),
    path("add", EnglishViewSet.add_english, name="add_english"),
    path("update", EnglishViewSet.update_english, name="update_english"),
    path("delete/<int:english_id>", EnglishViewSet.delete_english, name="delete_english"),
]
