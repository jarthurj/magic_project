from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('name_search', views.name_search),
    path('name_search_return', views.name_search_return),
    path('advanced',views.advanced_search),
    path('advanced_search', views.advanced_search_process),
    path('advanced_search_return', views.advanced_search_return),
    path('single_card/<int:card_id>', views.single_card_return),
]