# Generated by Django 4.2.3 on 2023-09-10 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
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
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Grade', models.CharField(max_length=50)),
                ('asignature_id', models.IntegerField()),
                ('aprove', models.CharField(max_length=15)),
                ('note', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachers.calification')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.students')),
            ],
        ),
    ]