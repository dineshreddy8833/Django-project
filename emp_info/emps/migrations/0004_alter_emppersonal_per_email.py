# Generated by Django 3.2.2 on 2021-07-13 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emps', '0003_emppersonal_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emppersonal',
            name='per_email',
            field=models.CharField(max_length=30),
        ),
    ]