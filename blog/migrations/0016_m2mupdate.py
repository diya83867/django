# Generated by Django 4.0.5 on 2022-08-30 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_alter_usernotification_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='m2mUpdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True)),
                ('number', models.IntegerField()),
                ('m2m', models.ManyToManyField(blank=True, to='blog.tag')),
            ],
            options={
                'verbose_name_plural': 'm2m-update',
            },
        ),
    ]