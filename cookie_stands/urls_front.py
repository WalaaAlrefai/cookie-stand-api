from django.urls import path
from .views_front import (
    CookieStandCreateView,
    CookieStandDeleteView,
    CookieStandDetailView,
    CookieStand_listView,
    CookieStandUpdateView,
)

urlpatterns = [
    path("", CookieStand_listView.as_view(), name="CookieStand_list"),
    path("<int:pk>/", CookieStandDetailView.as_view(), name="CookieStandDetail"),
    path("create/", CookieStandCreateView.as_view(), name="CookieStand_create"),
    path("<int:pk>/update/", CookieStandUpdateView.as_view(), name="CookieStand_update"),
    path("<int:pk>/delete/", CookieStandDeleteView.as_view(), name="CookieStand_delete"),
]
