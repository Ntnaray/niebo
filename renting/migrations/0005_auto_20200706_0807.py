# Generated by Django 2.2 on 2020-07-06 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('renting', '0004_auto_20200706_0743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newrentalhouse',
            name='state',
            field=models.CharField(choices=[('Lower Silesia', 'Lower Silesia'), ('Kujawsko_Pomorskie', 'Kujawsko_Pomorskie'), ('Łódź Province', 'Łódź Province'), ('Lublin Province', 'Lublin Province'), ('Lubuskie Province', 'Lubuskie Province'), ('Małopolska Province', 'Małopolska Province'), ('Masovia Province', 'Masovia Province'), ('Masovia Province', 'Masovia Province'), ('Podkarpackie Province', 'Podkarpackie Province'), ('Podlasie Province', 'Podlasie Province'), ('Pomerania Province', 'Pomerania Province'), ('Silesia Province', 'Silesia Province'), ('Holy Cross Province', 'Holy Cross Province'), ('Warmia_Masuria', 'Warmia_Masuria'), ('Wielkopolska Province', 'Wielkopolska Province'), ('West Pomerania', 'West Pomerania')], max_length=1),
        ),
    ]
