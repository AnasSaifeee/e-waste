# Generated by Django 3.2.15 on 2022-08-26 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('role', models.CharField(max_length=20, null=True)),
                ('email', models.CharField(max_length=12, null=True)),
                ('password', models.CharField(max_length=20, null=True)),
                ('username', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('role', models.CharField(max_length=20, null=True)),
                ('email', models.CharField(max_length=12, null=True)),
                ('password', models.CharField(max_length=20, null=True)),
                ('username', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=122)),
                ('address1', models.CharField(max_length=122)),
                ('address2', models.CharField(max_length=122)),
                ('district', models.CharField(max_length=122)),
                ('city', models.CharField(max_length=122)),
                ('state', models.CharField(max_length=122)),
                ('pincode', models.CharField(max_length=122)),
                ('contact_no', models.CharField(max_length=12)),
                ('ename', models.CharField(max_length=122)),
                ('EwasteType', models.CharField(max_length=122)),
                ('size', models.CharField(max_length=122)),
                ('weight', models.CharField(max_length=122)),
                ('quantity', models.CharField(max_length=122)),
                ('date_s', models.CharField(max_length=122)),
                ('time', models.CharField(max_length=122)),
                ('e_img', models.FileField(upload_to='')),
                ('e_img2', models.FileField(upload_to='')),
                ('e_img3', models.FileField(upload_to='')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=122)),
                ('district', models.CharField(max_length=122)),
                ('city', models.CharField(max_length=122)),
                ('state', models.CharField(max_length=122)),
                ('pincode', models.CharField(max_length=122)),
                ('contact_no', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Requestcollector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=122)),
                ('address1', models.CharField(max_length=122)),
                ('address2', models.CharField(max_length=122)),
                ('district', models.CharField(max_length=122)),
                ('city', models.CharField(max_length=122)),
                ('state', models.CharField(max_length=122)),
                ('pincode', models.CharField(max_length=122)),
                ('contact_no', models.CharField(max_length=12)),
                ('ename', models.CharField(max_length=122)),
                ('EwasteType', models.CharField(max_length=122)),
                ('size', models.CharField(max_length=122)),
                ('weight', models.CharField(max_length=122)),
                ('quantity', models.CharField(max_length=122)),
                ('date_s', models.CharField(max_length=122)),
                ('time', models.CharField(max_length=122)),
                ('e_img', models.FileField(upload_to='')),
                ('e_img2', models.FileField(upload_to='')),
                ('e_img3', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, null=True)),
                ('role', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
