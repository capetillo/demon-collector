# Generated by Django 2.2.6 on 2019-12-17 03:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Demon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('classification', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=300)),
                ('age', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Soul',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Snack date')),
                ('body', models.CharField(choices=[('C', 'Carolina'), ('B', 'Blaine'), ('A', 'Amy'), ('S', 'Shaw'), ('M', 'Marco'), ('N', 'Morgan'), ('H', 'Chris')], default='C', max_length=1)),
                ('demon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Demon')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
