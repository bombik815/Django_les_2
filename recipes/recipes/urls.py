from django.urls import path
from calculator.views import recipes

urlpatterns = [
    # здесь зарегистрируйте вашу view-функцию
    path('omlet/', recipes, name='omlet'),
    path('pasta/', recipes, name='pasta'),
    path('buter/', recipes, name='buter')
]
