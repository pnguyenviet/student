from django.conf.urls import url
from student import views
from student.views import SnippetList, AuthStudentActions

urlpatterns = [
    url(r'^students/$', SnippetList.as_view()),
    url(r'^studentdetail/(?P<pk>\d+)$', AuthStudentActions.as_view()),
    url(r'^studentcreate/', AuthStudentActions.as_view()),
]