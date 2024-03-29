# Generated by Django 4.2 on 2024-02-26 08:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='AboutImg')),
                ('num', models.IntegerField()),
                ('title', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('price', models.DecimalField(decimal_places=4, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='FacultyImg')),
            ],
        ),
        migrations.CreateModel(
            name='HowWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='HowWorkImg')),
                ('title', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comp_name', models.CharField(max_length=50)),
                ('logo', models.ImageField(upload_to='BannerImg')),
                ('addres', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=30)),
                ('working_time', models.CharField(max_length=250)),
                ('about', models.TextField()),
                ('fb', models.URLField()),
                ('tg', models.URLField()),
                ('insta', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=100)),
                ('l_name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='PersonalManagerImg')),
                ('position', models.CharField(max_length=100)),
                ('about', models.TextField()),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Regions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=100)),
                ('l_name', models.CharField(max_length=100)),
                ('m_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('bio', models.TextField()),
                ('passport', models.FileField(upload_to='StudentFiles')),
                ('certificate', models.FileField(upload_to='StudentFiles')),
                ('ielts', models.FloatField(default=0)),
                ('gpa', models.FloatField(default=0)),
                ('contract', models.FileField(blank=True, null=True, upload_to='StudentFiles')),
                ('date', models.DateField(auto_now=True)),
                ('gender', models.IntegerField(choices=[(1, 'Male'), (2, 'Female')], default=1)),
                ('faculty', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mein.faculty')),
                ('p_manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mein.personalmanager')),
            ],
        ),
        migrations.CreateModel(
            name='UniversityGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='UniGallery')),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('date', models.DateField(blank=True, null=True)),
                ('img', models.ImageField(upload_to='UniversityImg')),
                ('banner', models.ImageField(upload_to='UniversityImg')),
                ('desc', models.TextField()),
                ('motto', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
                ('contract_price', models.DecimalField(decimal_places=3, max_digits=6)),
                ('admission', models.CharField(max_length=300)),
                ('edu_agency', models.CharField(max_length=300)),
                ('degree', models.ManyToManyField(to='mein.degree')),
                ('faculty', models.ManyToManyField(to='mein.faculty')),
                ('gallery', models.ManyToManyField(to='mein.universitygallery')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mein.regions')),
            ],
        ),
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mein.student')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='university',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mein.university'),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uzer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='faculty',
            name='languages',
            field=models.ManyToManyField(to='mein.languages'),
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='BannerImg')),
                ('title', models.CharField(max_length=250)),
                ('text', models.TextField(max_length=250)),
                ('degree', models.ManyToManyField(to='mein.degree')),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passport', models.FileField(upload_to='ApplicationFiles')),
                ('certificate', models.FileField(upload_to='ApplicationFiles')),
                ('date', models.DateField(auto_now=True)),
                ('answer', models.CharField(max_length=255)),
                ('status', models.IntegerField(choices=[('1', 'received'), ('2', 'cancelled'), ('3', 'Pending')], default=3)),
                ('degree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mein.degree')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mein.faculty')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mein.languages')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mein.student')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mein.university')),
            ],
        ),
    ]
