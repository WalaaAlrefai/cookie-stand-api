from django.urls import path
from .views import CookieStand_list, CookieStandDetail

urlpatterns = [
    path("", CookieStand_list.as_view(), name="CookieStand_list"),
    path("<int:pk>/", CookieStandDetail.as_view(), name="CookieStandDetail"),
]
