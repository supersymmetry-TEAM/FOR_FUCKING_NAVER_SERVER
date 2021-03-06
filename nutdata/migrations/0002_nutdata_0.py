# Generated by Django 3.1.1 on 2021-03-15 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutdata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NutData_0',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NUTR_CONT1', models.FloatField(default=0)),
                ('NUTR_CONT2', models.FloatField(default=0)),
                ('NUTR_CONT3', models.FloatField(default=0)),
                ('NUTR_CONT4', models.FloatField(default=0)),
                ('NUTR_CONT5', models.FloatField(default=0)),
                ('NUTR_CONT6', models.FloatField(default=0)),
                ('NUTR_CONT7', models.FloatField(default=0)),
                ('NUTR_CONT8', models.FloatField(default=0)),
                ('NUTR_CONT9', models.FloatField(default=0)),
                ('FOOD_CD', models.FloatField(default=0)),
                ('DESC_KOR', models.CharField(default='', max_length=200)),
                ('SERVING_SIZE', models.FloatField(default=0)),
                ('MAKER_NAME', models.CharField(default='', max_length=200)),
                ('SAMPLING_MONTH_NAME', models.CharField(default='', max_length=200)),
                ('SUB_REF_NAME', models.CharField(default='', max_length=200)),
                ('SAMPLING_REGION_NAME', models.CharField(default='', max_length=200)),
                ('GROUP_NAME', models.CharField(default='', max_length=200)),
                ('RESEARCH_YEAR', models.FloatField(default=0)),
                ('SAMPLING_REGION_CD', models.CharField(default='', max_length=50)),
                ('SAMPLING_MONTH_CD', models.CharField(default='', max_length=50)),
                ('NUM', models.IntegerField(default=0)),
                ('SEARCH_SCORE', models.IntegerField(default=0)),
            ],
        ),
    ]
