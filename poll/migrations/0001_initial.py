# Generated by Django 4.0.1 on 2022-01-13 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('poll_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Question', models.TextField(max_length=200)),
                ('Name_1', models.CharField(max_length=100)),
                ('Name_2', models.CharField(max_length=100)),
                ('image_1', models.ImageField(blank=True, null=True, upload_to='media')),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='media')),
                ('count_1', models.IntegerField(default=0)),
                ('count_2', models.IntegerField(default=0)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
    ]
