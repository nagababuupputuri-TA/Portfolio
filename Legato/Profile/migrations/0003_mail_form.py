# Generated by Django 3.2.4 on 2021-06-10 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0002_alter_header_resume'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mail_form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('header', models.CharField(max_length=254)),
                ('body', models.CharField(max_length=254)),
            ],
        ),
    ]