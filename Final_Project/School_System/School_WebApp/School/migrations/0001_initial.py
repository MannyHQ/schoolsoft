# Generated by Django 4.2.4 on 2023-09-04 17:55

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
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Parents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('id_number', models.CharField(max_length=11, verbose_name='cedula')),
                ('mail', models.CharField(max_length=200)),
                ('phone_number', models.BigIntegerField()),
                ('status', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('birthdate', models.DateField()),
                ('gender', models.CharField(max_length=11, verbose_name='genero')),
                ('id_number', models.CharField(max_length=11, verbose_name='matricula')),
                ('mail', models.CharField(max_length=200)),
                ('phone_number', models.BigIntegerField()),
                ('status', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('start_date', models.DateTimeField()),
                ('description', models.CharField(max_length=200)),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='School.course')),
            ],
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('code', models.IntegerField()),
                ('mail', models.CharField(max_length=200)),
                ('phone_number', models.BigIntegerField()),
                ('id_number', models.CharField(max_length=11, verbose_name='cedula')),
                ('status', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UnassignedUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TeacherUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ter', to='School.teachers')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tur', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher_VS_Subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='School.subject')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='School.teachers')),
            ],
        ),
        migrations.CreateModel(
            name='StudentUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ser', to='School.students')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sur', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ParentUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='per', to='School.parents')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pur', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Inscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_inscription', models.DateTimeField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('inscription_status', models.SmallIntegerField()),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ics', to='School.course')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ist', to='School.students')),
            ],
        ),
    ]
