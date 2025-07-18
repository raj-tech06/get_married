# Generated by Django 5.2.3 on 2025-07-08 18:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoysProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('caste', models.CharField(blank=True, max_length=100, null=True)),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=10, null=True)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('image', models.ImageField(default='profiles/default.png', upload_to='profiles/')),
                ('dob', models.DateField(blank=True, null=True)),
                ('birth_place', models.CharField(blank=True, max_length=100, null=True)),
                ('birth_time', models.TimeField(blank=True, null=True)),
                ('about', models.TextField(blank=True, null=True)),
                ('height', models.CharField(blank=True, max_length=10, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('education', models.CharField(blank=True, max_length=100, null=True)),
                ('occupation', models.CharField(blank=True, max_length=100, null=True)),
                ('father_name', models.CharField(blank=True, max_length=100, null=True)),
                ('mother_name', models.CharField(blank=True, max_length=100, null=True)),
                ('is_approved', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='DisabledProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('caste', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('phone', models.CharField(blank=True, max_length=10, null=True)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('image', models.ImageField(default='profiles/default.png', upload_to='profiles/')),
                ('dob', models.DateField(blank=True, null=True)),
                ('birth_place', models.CharField(blank=True, max_length=100, null=True)),
                ('birth_time', models.TimeField(blank=True, null=True)),
                ('about', models.TextField(blank=True, null=True)),
                ('height', models.CharField(blank=True, max_length=10, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('education', models.CharField(blank=True, max_length=100, null=True)),
                ('occupation', models.CharField(blank=True, max_length=100, null=True)),
                ('father_name', models.CharField(blank=True, max_length=100, null=True)),
                ('mother_name', models.CharField(blank=True, max_length=100, null=True)),
                ('is_approved', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='DivorcedProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('caste', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('phone', models.CharField(blank=True, max_length=10, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('image', models.ImageField(default='profiles/default.png', upload_to='divorced_profiles/')),
                ('dob', models.DateField(blank=True, null=True)),
                ('birth_place', models.CharField(blank=True, max_length=100, null=True)),
                ('birth_time', models.TimeField(blank=True, null=True)),
                ('about', models.TextField(blank=True, null=True)),
                ('height', models.CharField(blank=True, max_length=10, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('education', models.CharField(blank=True, max_length=100, null=True)),
                ('occupation', models.CharField(blank=True, max_length=100, null=True)),
                ('father_name', models.CharField(blank=True, max_length=100, null=True)),
                ('mother_name', models.CharField(blank=True, max_length=100, null=True)),
                ('is_approved', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='GirlsProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('caste', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('phone', models.CharField(blank=True, max_length=10, null=True)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('image', models.ImageField(default='profiles/default.png', upload_to='profiles/')),
                ('dob', models.DateField(blank=True, null=True)),
                ('birth_place', models.CharField(blank=True, max_length=100, null=True)),
                ('birth_time', models.TimeField(blank=True, null=True)),
                ('about', models.TextField(blank=True, null=True)),
                ('height', models.CharField(blank=True, max_length=10, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('education', models.CharField(blank=True, max_length=100, null=True)),
                ('occupation', models.CharField(blank=True, max_length=100, null=True)),
                ('father_name', models.CharField(blank=True, max_length=100, null=True)),
                ('mother_name', models.CharField(blank=True, max_length=100, null=True)),
                ('is_approved', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('caste', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(max_length=10, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('dob', models.DateField(blank=True, null=True)),
                ('birth_place', models.CharField(blank=True, max_length=100, null=True)),
                ('birth_time', models.TimeField(blank=True, null=True)),
                ('about', models.TextField(blank=True, null=True)),
                ('height', models.CharField(blank=True, max_length=10, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('education', models.CharField(blank=True, max_length=100, null=True)),
                ('occupation', models.CharField(blank=True, max_length=100, null=True)),
                ('father_name', models.CharField(blank=True, max_length=100, null=True)),
                ('mother_name', models.CharField(blank=True, max_length=100, null=True)),
                ('password', models.CharField(max_length=100)),
                ('address', models.TextField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10, null=True)),
                ('profile_image', models.ImageField(blank=True, default='profiles/default.png', null=True, upload_to='profiles/')),
                ('category', models.CharField(blank=True, choices=[('girls', 'Girls'), ('boys', 'Boys'), ('disabled', 'Disabled'), ('divorced', 'Divorced')], max_length=20, null=True)),
                ('is_blocked', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='RegistrationNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('RRnumber', models.EmailField(max_length=254)),
                ('is_read', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='BoyProfilePhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='more_photos/')),
                ('boy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='myapp.boysprofile')),
            ],
        ),
        migrations.CreateModel(
            name='DisabledProfilePhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='more_photos/')),
                ('disabled', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='myapp.disabledprofile')),
            ],
        ),
        migrations.CreateModel(
            name='DivorcedProfilePhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='more_photos/')),
                ('divorced', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='myapp.divorcedprofile')),
            ],
        ),
        migrations.CreateModel(
            name='GirlProfilePhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='more_photos/')),
                ('girl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='myapp.girlsprofile')),
            ],
        ),
        migrations.CreateModel(
            name='ProfilePermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('boys', 'Boys'), ('girls', 'Girls'), ('disabled', 'Disabled'), ('divorced', 'Divorced')], max_length=20)),
                ('profile_email', models.EmailField(max_length=254)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.myuser')),
            ],
        ),
        migrations.CreateModel(
            name='UserPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='user_photos/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='myapp.myuser')),
            ],
        ),
    ]
