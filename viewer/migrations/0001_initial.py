# Generated by Django 4.1.1 on 2024-08-30 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BodyType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_body', models.CharField(max_length=50)),
                ('description_body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_brand', models.CharField(max_length=50)),
                ('description_brand', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('engine_power', models.CharField(max_length=20)),
                ('year_of_manufature', models.IntegerField(max_length=4)),
                ('price', models.DecimalField(decimal_places=2, max_digits=11)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('name_body', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='viewer.bodytype')),
                ('name_brand', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='viewer.brand')),
            ],
        ),
    ]
