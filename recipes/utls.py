from django.urls import path
from recipes.views import home, about, contacts

urlpatterns = [
    path('', home),
    path('sobre/', about),
    path('contato/', contacts),
]
