from django.urls import path
from .views import StudentListView
from .views import TeacherListView
from .views import CourseListView
from .views import ClassroomListView
from .views import ClassPeriodListView
from .views import StudentDetailView
from .views import TeacherDetailView
from .views import CourseDetailView
from .views import ClassroomDetailView
from .views import ClassPeriodDetailView
# from .views import TimetableListView


urlpatterns = [
path("students/", StudentListView.as_view(), name="student_list_view"),
path("teachers/", TeacherListView.as_view(), name="teacher_list_view"),
path("courses/", CourseListView.as_view(), name="course_list_view"),
path("classrooms/", ClassroomListView.as_view(), name="classroom_list_view"),
path("periods/", ClassPeriodListView.as_view(), name="classperiod_list_view"),
path("student/<int:id>/", StudentDetailView.as_view(), name="student_detail_view"),
path("teacher/<int:id>/", TeacherDetailView.as_view(), name="teacher"),
path("course/<int:id>/", CourseDetailView.as_view(), name="course"),
path("classroom/<int:id>/", ClassroomDetailView.as_view(), name="classroom"),
path("period/<int:id>/", ClassPeriodDetailView.as_view(), name="period"),
# path("timetables/", TimetableListView.as_view(), name="timetable_list_view"),

]