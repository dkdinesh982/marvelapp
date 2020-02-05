# Generated by Django 3.0.2 on 2020-01-12 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctordemo', '0002_pharmacy_pharmacy_details'),
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnostcms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.CharField(max_length=100)),
                ('testamount', models.FloatField()),
                ('action', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Fees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('charge', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='HospitalRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('time', models.DateTimeField()),
                ('documents_and_files', models.FileField(blank=True, null=True, upload_to='documents_and_files')),
            ],
        ),
        migrations.CreateModel(
            name='NurseData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=13)),
                ('exprience', models.CharField(max_length=100)),
                ('hospital', models.CharField(max_length=100)),
                ('fees', models.FloatField()),
                ('caretype', models.CharField(max_length=100)),
                ('natureofcare', models.CharField(max_length=100)),
                ('typing', models.CharField(max_length=100)),
                ('days', models.CharField(max_length=100)),
                ('nursedoctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='datadoctornurse', to='doctordemo.Doctor_profiles')),
            ],
        ),
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speciality_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='NurseReportdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('files', models.FileField(upload_to='')),
                ('nursedata', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nurse', to='doctorhome.NurseData')),
            ],
        ),
        migrations.CreateModel(
            name='Electrocardgram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtest', models.CharField(max_length=100)),
                ('amount', models.FloatField()),
                ('diagnost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='electrogram', to='doctorhome.Diagnostcms')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor_at_home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_id', models.IntegerField()),
                ('charge', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=10)),
                ('file_name', models.FileField(null=True, upload_to='doctor_at_home')),
                ('doctor_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctorhome', to='doctordemo.Doctor_profiles')),
                ('patients_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patienthome', to='patients.Patients')),
            ],
        ),
    ]
