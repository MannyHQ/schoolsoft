# Generated by Django 4.2.4 on 2023-09-12 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0001_initial'),
        ('teachers', '0003_remove_calification_inscription_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='calification',
            name='inscription_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='School.inscription'),
            preserve_default=False,
        ),
    ]
