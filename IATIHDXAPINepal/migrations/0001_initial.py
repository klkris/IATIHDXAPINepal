# Generated by Django 2.0 on 2017-12-20 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HXLData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=50)),
                ('population', models.IntegerField(default=0)),
                ('peopleInjured', models.IntegerField(default=0)),
                ('femalesInjured', models.IntegerField(default=0)),
                ('malesInjured', models.IntegerField(default=0)),
                ('peopleDead', models.IntegerField(default=0)),
                ('femalesDead', models.IntegerField(default=0)),
                ('malesDead', models.IntegerField(default=0)),
                ('housesDamaged', models.IntegerField(default=0)),
                ('housesDestroyed', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='IATIData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iatiId', models.CharField(max_length=2000)),
                ('title', models.CharField(max_length=2000)),
                ('reportingOrg', models.CharField(max_length=2000)),
                ('telephone', models.CharField(default='', max_length=2000)),
                ('email', models.CharField(default='', max_length=2000)),
                ('website', models.CharField(default='', max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='ShelterData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=50)),
                ('blankets', models.IntegerField(default=0)),
                ('cgi', models.IntegerField(default=0)),
                ('clothes', models.IntegerField(default=0)),
                ('kitchenSets', models.IntegerField(default=0)),
                ('tarpaulin', models.IntegerField(default=0)),
                ('tents', models.IntegerField(default=0)),
            ],
        ),
    ]
