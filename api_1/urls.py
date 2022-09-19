from django.urls import path

from api_1.views import *

app_name = 'api_1'

urlpatterns = [
    path('add/', add_view),
    path('subtract/', subtract_view),
    path('multiply/', multiply_view),
    path('divide/', divide_view),
]
