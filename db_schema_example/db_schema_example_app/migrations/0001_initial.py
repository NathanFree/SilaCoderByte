# Generated by Django 3.2.5 on 2021-08-15 02:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'emailAddress',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('emailAddress', models.ForeignKey(max_length=64, null=True, on_delete=django.db.models.deletion.SET_NULL, to='db_schema_example_app.emailaddress')),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
