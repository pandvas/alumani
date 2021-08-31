from rest_framework import serializers
from .models import User,University,Department,Hod,Faculty,Student,Course,Event, Eventpoll, StudentPassword,Contact,Payment,Department_mapper,Faculty_mapper, Student_mapper, Rollno_mapper, Event_mapper

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','name','email','password']
        extra_kwargs={
            'password':{'write_only':True}
        }

    def create(self, validated_data):
        # Extracting the password
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model=University
        fields=['name','address','password','email']

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields=['name']

class HodSerializer(serializers.ModelSerializer):
    class Meta:
        model=Hod
        fields=['name','phone','email','id_hod','address']

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model=Faculty
        fields=['name','email','designation']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['name','email','address','contactdetails','yearofpassing']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields=['name','departmentid']

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event
        fields=['name','date','venue']

class EventpollSerializer(serializers.ModelSerializer):
    class Meta:
        model=Eventpoll
        fields=['interested','eventid','studentid']

class StudentPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentPassword
        fields=['studentid','password']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields=['name','email','description']

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Payment
        fields=['amount','status','donername','payment_id']

#--------------------------------------------------------------------

class DepartmentMapperSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department_mapper
        fields=['departmentid','universityid','hodid']

class FacultyMapperSerializer(serializers.ModelSerializer):
    class Meta:
        model=Faculty_mapper
        fields=['facultyid','departmentid','universityid']

class StudentMapperSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student_mapper
        fields=['studentid','courseid','universityid','departmentid']

class RollNoMapperSerializer(serializers.ModelSerializer):
    class Meta:
        model=Rollno_mapper
        fields=['rollno','studentid']

class EventMapperSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event_mapper
        fields=['eventid','departmentid']