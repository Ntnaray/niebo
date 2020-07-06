# Generated by Django 2.2 on 2020-07-06 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('renting', '0005_auto_20200706_0807'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal_allowed', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('smoking_allowed', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('musical_instrument', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('nrh', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='renting.NewRentalHouse')),
            ],
        ),
        migrations.CreateModel(
            name='PreferredTenant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE'), ('O', 'OTHERS')], max_length=1)),
                ('couple_friendly', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('bachelor_allowed', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('nrh', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='renting.NewRentalHouse')),
            ],
        ),
        migrations.CreateModel(
            name='HouseHas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bedroom', models.IntegerField()),
                ('kitchen', models.CharField(choices=[('Pr', 'Private'), ('Sh', 'Shared'), ('No', 'Not Available')], max_length=2)),
                ('bathroom', models.CharField(choices=[('Pr', 'Private'), ('Sh', 'Shared'), ('No', 'Not Available')], max_length=2)),
                ('living_room', models.CharField(choices=[('Pr', 'Private'), ('Sh', 'Shared'), ('No', 'Not Available')], max_length=2)),
                ('toilet', models.CharField(choices=[('Pr', 'Private'), ('Sh', 'Shared'), ('No', 'Not Available')], max_length=2)),
                ('balcony', models.CharField(choices=[('Pr', 'Private'), ('Sh', 'Shared'), ('No', 'Not Available')], max_length=2)),
                ('terrace', models.CharField(choices=[('Pr', 'Private'), ('Sh', 'Shared'), ('No', 'Not Available')], max_length=2)),
                ('garden', models.CharField(choices=[('Pr', 'Private'), ('Sh', 'Shared'), ('No', 'Not Available')], max_length=2)),
                ('basement', models.CharField(choices=[('Pr', 'Private'), ('Sh', 'Shared'), ('No', 'Not Available')], max_length=2)),
                ('parking', models.CharField(choices=[('Pr', 'Private'), ('Sh', 'Shared'), ('No', 'Not Available')], max_length=2)),
                ('wheelchair_accessible', models.CharField(choices=[('Pr', 'Private'), ('Sh', 'Shared'), ('No', 'Not Available')], max_length=2)),
                ('nrh', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='renting.NewRentalHouse')),
            ],
        ),
        migrations.CreateModel(
            name='Amenities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desk', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('closet', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('tv', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('washing_machine', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('dryer', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('dishwasher', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('kitchenware', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('wifi', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('heating', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('air_conditioning', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('bed', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('furnished', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('nrh', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='renting.NewRentalHouse')),
            ],
        ),
    ]
