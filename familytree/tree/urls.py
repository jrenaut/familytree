from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^junk/', JunkView.as_view(), name='junk'),
    url(r'^yay/', yay, name='yay'),
    url(r'^gedcom/upload', upload_gedcom, name='upload_gedcom'),
    url(r'^gedcom/show', show_gedcom, name='show_gedcom'),
    url(r'^people/list', list_people, name="list_people"),
    url(r'^person/(?P<id>[^/]+)/show', person_show, name="person_show"),
]
