from django.urls import path
from index.views import index, contact

app_name = 'index'

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
]
