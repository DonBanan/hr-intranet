# Generated by Django 4.0.4 on 2022-05-30 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_historicaluser_is_ses_user_is_ses'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicaluser',
            name='gender',
            field=models.BooleanField(null=True, verbose_name='Gender'),
        ),
        migrations.AddField(
            model_name='historicaluser',
            name='seen_welcome',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='historicaluser',
            name='user_locked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='historicaluser',
            name='user_type',
            field=models.CharField(choices=[('admin', 'Admin'), ('hrg', 'HR-generalist'), ('employee', 'Employee'), ('service', 'Service Account')], default='employee', max_length=60),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.BooleanField(null=True, verbose_name='Gender'),
        ),
        migrations.AddField(
            model_name='user',
            name='seen_welcome',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='user_locked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('admin', 'Admin'), ('hrg', 'HR-generalist'), ('employee', 'Employee'), ('service', 'Service Account')], default='employee', max_length=60),
        ),
    ]