# Generated by Django 4.0.6 on 2022-08-09 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projects', models.CharField(db_index=True, max_length=150)),
                ('date_of_creation', models.DateField()),
                ('awards', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name': 'company',
            },
        ),
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='icons')),
                ('client_partner', models.URLField()),
                ('date_for_sort', models.DateTimeField()),
                ('num_for_sort', models.IntegerField(unique=True)),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
                'ordering': ('num_for_sort',),
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255)),
                ('title_ru', models.CharField(db_index=True, max_length=255, null=True)),
                ('title_en', models.CharField(db_index=True, max_length=255, null=True)),
                ('title_ky', models.CharField(db_index=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='project_img')),
                ('created', models.DateTimeField()),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('description_ru', models.TextField(blank=True, max_length=1000, null=True)),
                ('description_en', models.TextField(blank=True, max_length=1000, null=True)),
                ('description_ky', models.TextField(blank=True, max_length=1000, null=True)),
                ('site_url', models.URLField()),
                ('instagram_url', models.URLField()),
                ('title_url', models.URLField()),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='services')),
                ('title', models.CharField(db_index=True, max_length=200)),
                ('title_ru', models.CharField(db_index=True, max_length=200, null=True)),
                ('title_en', models.CharField(db_index=True, max_length=200, null=True)),
                ('title_ky', models.CharField(db_index=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'service',
                'verbose_name_plural': 'services',
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='agency_api.project')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
                'ordering': ('id',),
            },
        ),
    ]
