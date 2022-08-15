# Generated by Django 3.2 on 2022-05-12 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('port_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_Approval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1000)),
                ('is_approved', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='is_approve',
            field=models.BooleanField(default=False),
        ),
    ]
