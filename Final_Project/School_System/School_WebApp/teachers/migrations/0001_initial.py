# Generated by Django 4.2.4 on 2023-09-11 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('School', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('note', models.CharField(max_length=1000)),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='School.teachers')),
            ],
        ),
        migrations.CreateModel(
            name='calification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstPeriod', models.IntegerField(null=True)),
                ('secondPeriod', models.IntegerField(null=True)),
                ('thirdPeriod', models.IntegerField(null=True)),
                ('fourthPeriod', models.IntegerField(null=True)),
                ('finish', models.IntegerField(null=True)),
                ('Subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='School.subject')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='School.students')),
            ],
        ),
    ]
