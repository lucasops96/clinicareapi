# Generated by Django 5.0.1 on 2024-01-25 22:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinicareapi', '0006_alter_customuser_cpf'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_custom',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_custom', to=settings.AUTH_USER_MODEL),
        ),
    ]
