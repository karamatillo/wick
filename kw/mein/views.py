from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.status import HTTP_500_INTERNAL_SERVER_ERROR, HTTP_201_CREATED, HTTP_200_OK
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


from .models import Information, Banner, AboutUs, Degree, Faculty, Regions, University, HowWork, Student, Application, \
    Testimonials, ContactUs

from .serializer import ContactSerializer, BannerSerializer, AboutUsSerializer, DegreeSerializer, FacultySerializer, \
    UniversitySerializer, HowWorkSerializer, StudentSerializer, PersonalManagerSerializer, TestimonialsSerializer, \
    ApplicationSerializer, InformationSerializer


@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if not username or not password:
        return Response({'error': 'Please provide both username and password'}, status=status.HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def information_view(request):
    info = Information.objects.last()
    return Response(InformationSerializer(info).data)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def banner_view(request):
    banner = Banner.objects.last()
    degree = Degree.objects.last()
    data = {
        'banner': BannerSerializer(banner).data,
        'degree': DegreeSerializer(degree).data,
    }
    return Response(data)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def about_view(request):
    about = AboutUs.objects.all().order_by('-id')[:4]
    return Response(AboutUsSerializer(about, many=True).data)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def popular_universities_view(request):
    popular_u = University.objects.all().order_by('rating')[:6]
    return Response(UniversitySerializer(popular_u, many=True).data)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def popular_faculties_view(request):
    faculties = Faculty.objects.all().order_by('-application')[:9]
    return Response(FacultySerializer(faculties, many=True).data)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def how_works_view(request):
    try:
        how_works = HowWork.objects.all().order_by('-id')[:6]
        data = {
            'success': True,
            'message': HowWorkSerializer(how_works).data
        }
        sta = HTTP_200_OK
    except Exception as e:
        data = {
            'success': False,
            'message': f'{e}'
        }
        sta = HTTP_500_INTERNAL_SERVER_ERROR
    return Response(data, sta)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def testimonials_view(request):
    testimonials = Testimonials.objects.all().order_by('-id')[:6]
    return Response(TestimonialsSerializer(testimonials, many=True).data)


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create_contact_view(request):
    try:
        phone = request.POST.get('phone')
        contact_us = ContactUs.objects.create(phone=phone)
        contact_us.save()
        data = {
            'success': True,
            'message': ContactSerializer(contact_us).data
        }
        sta = HTTP_201_CREATED
    except Exception as e:
        data = {
            'success': False,
            'message': f'{e}'
        }
        sta = HTTP_500_INTERNAL_SERVER_ERROR
    return Response(data, sta)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def university_filter_view(request):
    try:
        university = University.objects.all()
        if request.GET.get('region'):
            university = University.objects.filter(region__name=request.GET.get('region'))
        if request.GET.get('degree'):
            university = university.filter(degree__name=request.GET.get('degree'))
        if request.GET.get('faculty'):
            university = university.filter(faculty__name=request.GET.get('faculty'))
        data = {'success': True,
                'message': UniversitySerializer(university, many=True).data
                }
    except Exception as e:
        data = {
            'success': False,
            'message': f'{e}'
        }
    return Response(data)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def uni_details_view(request, pk):
    uni_details = University.objects.get(id=pk)
    return Response(UniversitySerializer(uni_details).data)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def student_cabinet_view(request, pk):
    student = Student.objects.get(id=pk)
    return Response(StudentSerializer(student).data)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def student_applied_universities(request, pk):
    university = Application.objects.filter(student_id=pk).order_by('-id')
    return Response(ApplicationSerializer(university, many=True).data)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def student_applied_university_single(request, pk):
    university = Application.objects.get(student_id=pk)
    return Response(ApplicationSerializer(university).data)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def student_personal_manager_view(request, pk):
    student = Student.objects.get(id=pk)
    p_manager = student.p_manager
    return Response(PersonalManagerSerializer(p_manager).data)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def uni_admin_view(request, pk):
    university = University.objects.get(id=pk)
    total_students = Student.objects.filter(university_id=pk).count()
    invoices = Application.objects.filter(university_id=pk).count()
    received = Application.objects.filter(status=1).count()
    cancelled = Application.objects.filter(status=2).count()
    students = Student.objects.filter(university_id=pk)
    male = students.filter(gender=1).count()
    female = students.filter(gender=2).count()
    data = {
        'university': university,
        'total_students': total_students,
        'invoices': invoices,
        'received': received,
        'cancelled': cancelled,
        'gender': {
            'male': male,
            'female': female,
        }
    }
    return Response(data)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def university_students(request, pk):
    students = Student.objects.filter(university_id=pk)
    ser = StudentSerializer(students, many=True).data
    if request.GET.get('f_name'):
        search_student = students.filter(f_name=request.GET.get('f_name'))
        ser = StudentSerializer(search_student, many=True).data
    if request.GET.get('start_date') and request.GET.get('end_date'):
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        filter_objects = students.filter(date__gte=start_date, date__lte=end_date)
        ser = StudentSerializer(filter_objects, many=True).data
    return Response(ser)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def university_invoices(request, pk):
    invoices = Application.objects.filter(university_id=pk)
    ser = ApplicationSerializer(invoices, many=True).data
    if request.GET.get('f_name'):
        search_invoice = invoices.filter(student__f_name=request.GET.get('f_name'))
        ser = ApplicationSerializer(search_invoice, many=True).data
    if request.GET.get('start_date') and request.GET.get('end_date'):
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        filter_objects = invoices.filter(student__date__gte=start_date, student__date__lte=end_date, status=3)
        ser = ApplicationSerializer(filter_objects, many=True).data
    return Response(ser)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def university_student_info(request, pk):
    student = Application.objects.get(student_id=pk)
    return Response(ApplicationSerializer(student).data)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def replying_to_student(request, pk):
    try:
        invoice = Application.objects.get(student_id=pk)
    except Application.DoesNotExist:
        return Response({'success': False, 'message': 'Application not found'}, status=404)
    invoice.status = request.GET.get('status')
    invoice.save()
    if invoice.status == '1':
        data = {
            'success': True,
            'message': 'You have been successfully accepted by the University',
            'acceptance_date': invoice.date
        }
    elif invoice.status == '2':
        data = {
            'success': False,
            'message': 'Your application has been rejected by the University'
        }
    return Response(data)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def university_cabinet(request, pk):
    university = University.objects.get(id=pk)
    return Response(UniversitySerializer(university).data)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def backoffice_view(request):
    students = Student.objects.all().count()
    university = University.objects.all().count()
    region = Regions.objects.all().count()
    faculty = Faculty.objects.all().count()
    male = Student.objects.filter(gender=1).count()
    female = Student.objects.filter(gender=2).count()
    context = {
        'students': students,
        'university': university,
        'region': region,
        'faculty': faculty,
        'male': male,
        'female': female
    }
    return Response(context)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def backoffice_universities(request):
    university = University.objects.all().order_by('-id')
    ser = UniversitySerializer(university, many=True).data
    if request.GET.get('region'):
        university = University.objects.filter(region__name=request.GET.get('region'))
        ser = UniversitySerializer(university, many=True).data
    if request.GET.get('city'):
        university = university.filter(city=request.GET.get('city'))
        ser = UniversitySerializer(university, many=True).data
    if request.GET.get('start_date') and request.GET.get('end_date'):
        university = university.filter(date__gte=request.GET.get('start_date'), date__lte=request.GET.get('end_date'))
        ser = UniversitySerializer(university, many=True).data
    return Response(ser)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def dashboard_students(request):
    student = Student.objects.all().order_by('-id')
    ser = StudentSerializer(student, many=True).data
    if request.GET.get('f_name'):
        searched_student = Student.objects.filter(f_name=request.GET.get('f_name'))
        ser = StudentSerializer(searched_student, many=True).data
    if request.GET.get('start_date') and request.GET.get('end_date'):
        filter_student = Student.objects.filter(date__gte=request.GET.get('start_date'),
                                                date__lte=request.GET.get('end_date'))
        ser = StudentSerializer(filter_student, many=True).data
    return Response(ser)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def dashboard_university_info(request, pk):
    university = University.objects.get(id=pk)
    return Response(UniversitySerializer(university).data)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def dashboard_student_info(request, pk):
    student = Student.objects.get(student_id=pk)
    return Response(StudentSerializer(student).data)
