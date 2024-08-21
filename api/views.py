from rest_framework.views import APIView
from rest_framework.response import Response
from student.models import Student
from .serializers import StudentSerializer
from rest_framework import status
from classperiod.models import ClassPeriod
from .serializers import ClassPeriodSerializer
from classroom.models import Classroom
from .serializers import ClassroomSerializer
from course.models import Course
from .serializers import CourseSerializer
from teacher.models import Teacher
from .serializers import TeacherSerializer
from .serializers import MinimalStudentSerializer
from .serializers import MinimalCourseSerializer
from .serializers import MinimalTeacherSerializer
from .serializers import MinimalClassroomSerializer
from .serializers import MinimalClassPeriodSerializer


class StudentListView(APIView):
    def get(self, request):
        student = Student.objects.all()
        first_name = request.query_params.get("first_name")
        if first_name: 
            Students = Students.filter(first_name = first_name)
        country = request.query_params.get("country")
        if country:
            Students = Students.filter(country = country)
        serializer = StudentSerializer(student, many=True)
        serializer = MinimalStudentSerializer(student, many = True)
        return Response(serializer.data)
    
        
        
    def post(self,request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDetailView(APIView):
    def enroll(self,student,course_id):
        course = Course.objects.get(id=course_id)
        student.courses.add(course)

    def unenroll(self, student, course_id):
        course = Course.objects.get(id=course_id)
        student.courses.remove(course)

    def add_to_class(self, student, class_id):
        student_class = Student_Class.objects.get(id=class_id)
        student_class.students.add(student)

    def post(self,request,id):
        student=Student.objects.get(id=id)
        action = request.data.get("action")
        if action=="enroll":
            course_id=request.data.get("course_id")
            self.enroll(student,course_id)
            return Response(status=status.HTTP_201_CREATED)
        elif action == "unenroll":
            course_id = request.data.get("course_id")
            self.unenroll(student, course_id)
            return Response(status=status.HTTP_200_OK)
        elif action == "add_to_class":
            class_id = request.data.get("class_id")
            self.add_to_class(student, class_id)
            return Response(status=status.HTTP_201_CREATED)
        else:
         return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,id):
        student=Student.objects.get(id=id)
        serializer=StudentSerializer(student)
        return Response(serializer.data)

    def put(self,request,id):
        student=Student.objects.get(id=id)
        serializer = StudentSerializer(student,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        
    def delete(self,request,id):
        student=Student.objects.get(id=id)
        student.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

class ClassPeriodListView(APIView):
       
    def get(self,request):
        periods=ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(periods,many=True)
        serializer = MinimalClassPeriodSerializer(periods,many=True)

        return Response(serializer.data)
    def post(self,request):
        serializer=ClassPeriodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
   
class ClassPeriodDetailView(APIView):

    def enroll(self,period,teacher_id):
        teacher = Teacher.objects.get(id=teacher_id)
        period.Teachers.add(teacher)
    def post(self,request,id):
        classperiod=ClassPeriod.objects.get(id=id)
        action = request.data.get("action")
        if action=="enroll":
            teacher_id=request.data.get("teacher_id")
            self.enroll(period,teacher_id)
            return Response(status=status.HTTP_201_CREATED)
        
    def enroll(self,period,course_id):
        course = Course.objects.get(id=course_id)
        period.Course.add(course)
    def post(self,request,id):
        period=ClassPeriod.objects.get(id=id)
        action = request.data.get("action")
        if action=="enroll":
            course_id=request.data.get("course_id")
            self.enroll(period,course_id)
            return Response(status=status.HTTP_201_CREATED)


    def get(self,request,id):
        period=ClassPeriod.objects.get(id=id)
        serializer=ClassPeriodSerializer(period)
        return Response(serializer.data)

    def put(self,request,id):
        period=ClassPeriod.objects.get(id=id)
        serializer = ClassPeriodSerializer(period,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        
    def delete(self,request,id):
        period= ClassPeriod.objects.get(id=id)
        period.delete()
        return Response(status=status.HTTP_202_ACCEPTED)


class ClassroomListView(APIView):
    def get(self, request):
        classrooms = Classroom.objects.all()
        serializer = ClassroomSerializer(classrooms, many=True)
        serializer= MinimalClassroomSerializer(classrooms, many = True)

        return Response(serializer.data)
    def post(self,request):
        serializer=ClassroomSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ClassroomDetailView(APIView):
    def enroll(self,classroom,teacher_id):
        teacher = Teacher.objects.get(id=teacher_id)
        classroom.Teachers.add(teacher)
    def post(self,request,id):
        classroom=Classroom.objects.get(id=id)
        action = request.data.get(" action")
        if action=="enroll":
            teacher_id=request.data.get("teacher_id")
            self.enroll(classroom,teacher_id)
            return Response(status=status.HTTP_201_CREATED)
    def get(self,request,id):
        classroom=Classroom.objects.get(id=id)
        serializer=ClassroomSerializer(classroom)
        return Response(serializer.data) 
    def put(self,request,id):
        classroom=Classroom.objects.get(id=id)
        serializer = ClassroomSerializer(classroom,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        classroom=Classroom.objects.get(id=id)
        classroom.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

class CourseListView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        serializer=MinimalCourseSerializer(courses,many=True)

        return Response(serializer.data)
    def post(self,request):
        serializer=CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class CourseDetailView(APIView):
    def enroll(self,course,teacher_id):
        teacher = Teacher.objects.get(id=teacher_id)
        course.Teachers.add(teacher)
    def post(self,request,id):
        course=Course.objects.get(id=id)
        action = request.data.get("action")
        if action=="enroll":
            teacher_id=request.data.get("teacher_id")
            self.enroll(course,teacher_id)
            return Response(status=status.HTTP_201_CREATED)
    def get(self,request,id):
        course=Course.objects.get(id=id)
        serializer=CourseSerializer(course)
        return Response(serializer.data)
    def put(self,request,id):
        course=Course.objects.get(id=id)
        serializer = CourseSerializer(course,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        course=Course.objects.get(id=id)
        course.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

class TeacherListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        serializer=MinimalTeacherSerializer(teachers,many=True)

        return Response(serializer.data)
    
    def post(self,request):
        serializer=TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class TeacherDetailView(APIView):
    def get(self,request,id):
        #retrieving a single object
        teacher=Teacher.objects.get(id=id)
        serializer=TeacherSerializer(teacher)
        return Response(serializer.data)
    def put(self,request,id):
        teacher=Teacher.objects.get(id=id)
        serializer = TeacherSerializer(teacher,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        teacher=Teacher.objects.get(id=id)
        teacher.delete()
        return Response(status=status.HTTP_202_ACCEPTED)