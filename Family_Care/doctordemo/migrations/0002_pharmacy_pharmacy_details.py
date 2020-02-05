# Generated by Django 3.0.2 on 2020-01-11 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
        ('doctordemo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pharmacy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('charge', models.IntegerField()),
                ('action', models.FileField(null=True, upload_to='pharmacy_fields')),
            ],
        ),
        migrations.CreateModel(
            name='Pharmacy_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('quantity', models.CharField(max_length=10)),
                ('file_name', models.CharField(max_length=100)),
                ('files', models.FileField(null=True, upload_to='pharmacy_details')),
                ('patientsdata', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patientsdata', to='patients.Patients')),
                ('pharmacydata', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pharmacydata', to='doctordemo.Pharmacy')),
            ],
        ),
    ]