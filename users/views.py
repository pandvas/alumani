from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer, UniversitySerializer, DepartmentSerializer,HodSerializer, FacultySerializer,StudentSerializer, CourseSerializer, EventSerializer, EventpollSerializer, StudentPasswordSerializer, ContactSerializer, PaymentSerializer, DepartmentMapperSerializer, FacultyMapperSerializer, StudentMapperSerializer, RollNoMapperSerializer, EventMapperSerializer
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .models import User
import jwt, datetime

class RegisterView(APIView):
    def post(self, request):
        serializer=UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class RegisterUniversityView(APIView):
    def post(self, request):
        serializer=UniversitySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class RegisterDepartmentView(APIView):
    def post(self, request):
        serializer=DepartmentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class RegisterHodView(APIView):
    def post(self, request):
        serializer=HodSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class RegisterFacultyView(APIView):
    def post(self, request):
        serializer=FacultySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class RegisterStudentView(APIView):
    def post(self, request):
        serializer=StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class RegisterCourseView(APIView):
    def post(self, request):
        serializer=CourseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class RegisterEventView(APIView):
    def post(self, request):
        serializer=EventSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class EventpollView(APIView):
    def post(self, request):
        serializer=EventpollSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class StudentPasswordView(APIView):
    def post(self, request):
        serializer=StudentPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class ContactView(APIView):
    def post(self, request):
        serializer=ContactSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class PaymentView(APIView):
    def post(self, request):
        serializer=PaymentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class DepartmentMapperView(APIView):
    def post(self, request):
        serializer=DepartmentMapperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class FacultyMapperView(APIView):
    def post(self, request):
        serializer=FacultyMapperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class StudentMapperView(APIView):
    def post(self, request):
        serializer=StudentMapperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class RollNoMapperView(APIView):
    def post(selfself, request):
        serializer=RollNoMapperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class EventMapperView(APIView):
    def post(selfself, request):
        serializer=EventMapperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        email=request.data['email']
        password=request.data['password']

        user=User.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed('User Not Found')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect Passsword')

        #generating token
        payload={
            'id':user.id,
            'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=60),
            'iat':datetime.datetime.utcnow()
        }
        token=jwt.encode(payload, 'secretMessage', algorithm='HS256')

        response=Response()

        #setting Cookie
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data={
            'jwt':token
        }
        return response


class UserView(APIView):
    def get(self, request):
        token=request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated')
        try:
            payload=jwt.decode(token, 'secretMessage', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')

        user =User.objects.filter(id=payload['id']).first()
        serializer=UserSerializer(user)
        return Response(serializer.data)

class LogoutView(APIView):
    def post(self, request):
        response=Response()
        response.delete_cookie('jwt')
        response.data={
            'message':'Logout SuccessFull'
        }
        return response