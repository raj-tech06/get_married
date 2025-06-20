# Generated by Django 5.2.3 on 2025-06-15 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_remove_myuser_is_active_myuser_is_blocked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='is_blocked',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='phone',
        ),
        migrations.AddField(
            model_name='myuser',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='profile_image',
            field=models.ImageField(blank=True, default='profiles/default.png', null=True, upload_to='profiles/'),
        ),
    ]
