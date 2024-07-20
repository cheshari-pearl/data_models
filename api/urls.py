from django.urls import path
from .views import StudentListView
from .views import TeacherListView
from .views import CourseListView
from .views import ClassroomListView
from .views import ClassPeriodListView
from .views import StudentDetailView

urlpatterns = [
path("students/", StudentListView.as_view(), name="student_list_view"),
path("teachers/", TeacherListView.as_view(), name="teacher_list_view"),
path("courses/", CourseListView.as_view(), name="course_list_view"),
path("classrooms/", ClassroomListView.as_view(), name="classroom_list_view"),
path("periods/", ClassPeriodListView.as_view(), name="classperiod_list_view"),
path("student<int:id>/", StudentDetailView.as_view(), name="student_detail_view")

]


