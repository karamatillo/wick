from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

class Information(models.Model):
    comp_name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to="BannerImg")
    address = models.CharField(max_length=250)
    email = models.EmailField()
    phone_number = models.CharField(max_length=30)
    working_time = models.CharField(max_length=250)
    about = models.TextField()
    fb = models.URLField()
    tg = models.URLField()
    insta = models.URLField()
    
    def __str__(self):
        return self.comp_name
    
    
class About(models.Model):
    icon = models.ImageField(upload_to='AboutImg')
    num = models.IntegerField()
    title = models.CharField(max_length=250)
    
    def __str__(self):
        return self.title
    
    
class HowWork(models.Model):
    icon = models.ImageField(upload_to='HowWorkImg')
    title = models.CharField(max_length=250)
    
    def __str__(self):
        return self.title
    
    
class Degree(models.Model):
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=7, decimal_places=4)
    
    def __str__(self):
        return self.name
    
    
class Banner(models.Model):
    img = models.ImageField(upload_to="BannerImg")
    title = models.CharField(max_length=250)
    text = models.TextField(max_length=250)
    degree = models.ManyToManyField(Degree)
    
    def __str__(self):
        return self.title
    
    
class Languages(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    
class Faculty(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='FacultyImg')
    languages = models.ManyToManyField(Languages)
    
    def __str__(self):
        return self.name


class UniversityGallery(models.Model):
    img = models.ImageField(upload_to='UniGallery')

    def __str__(self):
        return self.img.url


class Regions(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class University(models.Model):
    name = models.CharField(max_length=255)
    region = models.ForeignKey(Regions, on_delete=models.CASCADE)
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    date = models.DateField(null=True, blank=True)
    img = models.ImageField(upload_to='UniversityImg')
    banner = models.ImageField(upload_to='UniversityImg')
    desc = models.TextField()
    motto = models.CharField(max_length=100)
    rating = models.IntegerField()
    contract_price = models.DecimalField(max_digits=6, decimal_places=3)
    degree = models.ManyToManyField(Degree)
    faculty = models.ManyToManyField(Faculty)
    admission = models.CharField(max_length=300)
    edu_agency = models.CharField(max_length=300)
    gallery = models.ManyToManyField(UniversityGallery)

    def __str__(self):
        return self.name


class PersonalManager(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='PersonalManagerImg')
    position = models.CharField(max_length=100)
    about = models.TextField()
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.f_name


class Student(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    m_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    bio = models.TextField()
    university = models.ForeignKey(University, on_delete=models.CASCADE, null=True, blank=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, null=True, blank=True)
    passport = models.FileField(upload_to='StudentFiles')
    certificate = models.FileField(upload_to='StudentFiles')
    ielts = models.FloatField(default=0)
    gpa = models.FloatField(default=0)
    contract = models.FileField(upload_to='StudentFiles', null=True, blank=True)
    p_manager = models.ForeignKey(PersonalManager, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    gender = models.IntegerField(choices=(
        (1, 'Male'),
        (2, 'Female')
    ), default=1)

    def __str__(self):
        return self.f_name


class Application(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE)
    passport = models.FileField(upload_to='ApplicationFiles')
    certificate = models.FileField(upload_to='ApplicationFiles')
    language = models.ForeignKey(Languages, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    answer = models.CharField(max_length=255)
    status = models.IntegerField(choices=(
        ('1', 'received'),
        ('2', 'cancelled'),
        ('3', 'Pending'),
    ), default=3)

    def __str__(self):
        return self.student.f_name


class Testimonials(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.student.l_name


class ContactUs(models.Model):
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.phone