# Generated by Django 4.2 on 2023-06-19 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_alter_client_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='piercing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.piercing'),
        ),
    ]