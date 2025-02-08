from django.urls import path
from .views import data_efis,data_ecam,data_pfd

urlpatterns = [
    # handles all get, post and delete of efis ecam and pfd
    path('efis/', data_efis, name='get_user_efis'),
    path('ecam/', data_ecam, name='get_user_ecam'),
    path('pfd/', data_pfd, name='get_user_pfd'),
]
