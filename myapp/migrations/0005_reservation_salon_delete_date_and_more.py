# Generated by Django 4.2 on 2023-05-10 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_material_placement_thickness_piercing'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Salon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Date',
        ),
        migrations.AlterModelOptions(
            name='thickness',
            options={'verbose_name_plural': 'Thicknesses'},
        ),
        migrations.AddField(
            model_name='reservation',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.salon'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.client'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='piercer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.piercer'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='piercing',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.piercing'),
        ),
    ]
