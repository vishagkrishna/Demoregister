# Generated by Django 4.2.4 on 2023-08-08 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0002_alter_user_gender_alter_user_material'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='account',
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='material',
            field=models.CharField(max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='account',
            field=models.ManyToManyField(to='bankapp.place'),
        ),
    ]
