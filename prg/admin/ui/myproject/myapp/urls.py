# # myapp/urls.py
from django.urls import path
from .views import my_form
from .views import issue_credentials
from .views import *


urlpatterns = [
    path('', my_form, name='my_form'),
    path('1', issue_credentials, name='issue_credentials'),
    path('generate_qr_code/<str:data>/', generate_qr_code, name='generate_qr_code'),

]
    # path('ss/', ss, name='ss'),  # Change the name to 'ss'



