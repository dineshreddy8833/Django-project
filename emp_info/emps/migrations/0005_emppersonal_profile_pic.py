# Generated by Django 3.2.2 on 2021-07-14 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emps', '0004_alter_emppersonal_per_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='emppersonal',
            name='profile_pic',
            field=models.FileField(default='', upload_to='media'),
        ),
    ]
