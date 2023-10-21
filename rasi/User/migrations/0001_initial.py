# Generated by Django 4.2.5 on 2023-09-30 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registerUser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('identification', models.CharField(max_length=15, unique=True)),
                ('regimen', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=10)),
                ('entity', models.CharField(max_length=50, null=True)),
                ('tipoIdentificacion', models.CharField(max_length=50)),
                ('correo', models.CharField(max_length=50, unique=True)),
                ('register', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='registerUser.registeruser')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emergencyContact', models.CharField(max_length=10)),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='User.user')),
            ],
        ),
        migrations.CreateModel(
            name='MedicalProfessional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='User.user')),
            ],
        ),
    ]