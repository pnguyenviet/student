from django.conf.urls import url, include
from student import views
from student.views import StudentList, AuthStudentActions
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^students/$', StudentList.as_view()),
    url(r'^students/(?P<pk>\d+)$', AuthStudentActions.as_view()),
    url('api-auth/', include('rest_framework.urls')),
    url(r'^api-token-auth/', obtain_jwt_token),
    # url(r'^studentcreate/', AuthStudentActions.as_view()),
]