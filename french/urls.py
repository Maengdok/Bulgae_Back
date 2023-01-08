from django.urls import path

from french.views import FrenchViewSet

urlpatterns = [
    path("", FrenchViewSet.french_list, name="get_french_list"),
    path("<int:french_id>", FrenchViewSet.get_french, name="get_french"),
    path("add", FrenchViewSet.add_french, name="add_french"),
    path("update", FrenchViewSet.update_french, name="update_french"),
    path("delete/<int:french_id>", FrenchViewSet.delete_french, name="delete_french"),
]
