# Generated by Django 4.2 on 2023-05-10 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Material')),
            ],
        ),
        migrations.CreateModel(
            name='Placement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Placement')),
            ],
        ),
        migrations.CreateModel(
            name='Thickness',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thickness', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Piercing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.material')),
                ('placement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.placement')),
                ('thickness', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.thickness')),
            ],
        ),
    ]
