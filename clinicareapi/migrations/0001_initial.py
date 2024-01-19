# Generated by Django 5.0.1 on 2024-01-19 01:31

import django.contrib.auth.validators
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conselho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rua', models.CharField(max_length=255)),
                ('numero', models.CharField(max_length=10)),
                ('complemento', models.CharField(blank=True, max_length=255, null=True)),
                ('cidade', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=100)),
                ('cep', models.CharField(blank=True, max_length=50, null=True)),
                ('pais', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('telefone', models.CharField(blank=True, max_length=15, null=True)),
                ('is_profissional_saude', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, related_name='customuser_set', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='customuser_set', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idade', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('peso', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0)])),
                ('sexo', models.CharField(max_length=20)),
                ('endereco', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='clinicareapi.endereco')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='clinicareapi.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='ProfissionalSaude',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especialidade', models.CharField(max_length=100)),
                ('numero_conselho', models.CharField(blank=True, max_length=50, null=True)),
                ('conselho', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='clinicareapi.conselho')),
                ('enderecos_atendimento', models.ManyToManyField(related_name='profissionais_atendimento', to='clinicareapi.endereco')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='clinicareapi.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_hora', models.DateField()),
                ('descricao', models.TextField()),
                ('local_atendimento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='clinicareapi.endereco')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consultas', to='clinicareapi.paciente')),
                ('profissional_saude', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consultas', to='clinicareapi.profissionalsaude')),
            ],
            options={
                'ordering': ['-data_hora'],
            },
        ),
    ]
