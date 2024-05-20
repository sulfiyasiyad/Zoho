# Generated by Django 3.2.23 on 2024-02-08 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Register_Login', '0015_remove_paymenttermsupdates_interested_to_continue'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company_Payment_Term',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term_name', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('days', models.IntegerField(default=0, null=True)),
                ('status', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
            ],
        ),
    ]
