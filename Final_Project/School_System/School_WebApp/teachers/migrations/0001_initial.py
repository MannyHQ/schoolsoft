# Generated by Django 4.2.3 on 2023-08-30 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('School', '0001_initial'),
    ]

    operations = [
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
