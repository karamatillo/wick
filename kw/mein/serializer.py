from rest_framework import serializers
from .models import Information, Banner, About, Degree, Faculty, University, HowWork, Student, Application, \
    PersonalManager, Testimonials, ContactUs


class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = '__all__'


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'
        depth = 1


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'


class DegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Degree
        fields = '__all__'


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = University
        fields = '__all__'


class HowWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = HowWork
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        depth = 1
        fields = '__all__'


class PersonalManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalManager
        fields = '__all__'


class TestimonialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonials
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'
