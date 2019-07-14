from django.conf.urls import url

from .views import *

urlpatterns=[
    url(r'^signup/$', SignupForm, name='SignUpForm'),
    url(r'^date/$',hello),
    url(r'^user_details/$',crudops,name="crudoperation"),
    url(r'^school name list/$',list_of_school,name="schools_list"),
    url(r'^school name list/(?P<id>[0-9])/$',SchoolDetails,name="schoolDetail"),
]

