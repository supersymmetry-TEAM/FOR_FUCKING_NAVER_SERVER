from django.db import models


# Create your models here.

class NutData_0(models.Model):
    
    NUTR_CONT1 =  models.FloatField(default=0)
    NUTR_CONT2 =  models.FloatField(default=0)
    NUTR_CONT3 =  models.FloatField(default=0)
    NUTR_CONT4 =  models.FloatField(default=0)
    NUTR_CONT5 =  models.FloatField(default=0)
    NUTR_CONT6 =  models.FloatField(default=0)
    NUTR_CONT7 =  models.FloatField(default=0)
    NUTR_CONT8 =  models.FloatField(default=0)
    NUTR_CONT9 =  models.FloatField(default=0)
    FOOD_CD = models.FloatField(default=0)
    DESC_KOR = models.CharField(max_length=200,default="")
    SERVING_SIZE = models.FloatField(default=0)
    MAKER_NAME = models.CharField(max_length=200,default="")
    SAMPLING_MONTH_NAME = models.CharField(max_length=200,default="")
    SUB_REF_NAME = models.CharField(max_length=200,default="")
    SAMPLING_REGION_NAME = models.CharField(max_length=200,default="")
    GROUP_NAME = models.CharField(max_length=200,default="")
    RESEARCH_YEAR = models.FloatField(default=0)
    SAMPLING_REGION_CD = models.CharField(max_length=50,default="")
    SAMPLING_MONTH_CD = models.CharField(max_length=50,default="")
    NUM = models.IntegerField(default=0)
    SEARCH_SCORE = models.IntegerField(default=0)
    UNIT = models.CharField(max_length=50,default="")
    DIETARY_FIBER =  models.FloatField(default=0)
    SUGAR_ALCOHOL = models.FloatField(default=0)
    ERYTHRITOL = models.FloatField(default=0)
    def __str__(self):
        return self.DESC_KOR


class NutData(models.Model):

    NUTR_CONT1 = models.FloatField(default=0)
    NUTR_CONT2 = models.FloatField(default=0)
    NUTR_CONT3 = models.FloatField(default=0)
    NUTR_CONT4 = models.FloatField(default=0)
    NUTR_CONT5 = models.FloatField(default=0)
    NUTR_CONT6 = models.FloatField(default=0)
    NUTR_CONT7 = models.FloatField(default=0)
    NUTR_CONT8 = models.FloatField(default=0)
    NUTR_CONT9 = models.FloatField(default=0)
    FOOD_CD = models.FloatField(default=0)
    DESC_KOR = models.CharField(max_length=200,default="")
    SERVING_SIZE = models.FloatField(default=0)
    MAKER_NAME = models.CharField(max_length=200,default="")
    SAMPLING_MONTH_NAME = models.CharField(max_length=200,default="")
    SUB_REF_NAME = models.CharField(max_length=200,default="")
    SAMPLING_REGION_NAME = models.CharField(max_length=200,default="")
    GROUP_NAME = models.CharField(max_length=200,default="")
    RESEARCH_YEAR = models.FloatField(default=0)
    SAMPLING_REGION_CD = models.CharField(max_length=50,default="")
    SAMPLING_MONTH_CD = models.CharField(max_length=50,default="")
    NUM = models.IntegerField(default=0)
    SEARCH_SCORE = models.IntegerField(default=0)
    def __str__(self):
        return self.DESC_KOR
class NutData_1(models.Model):
    
    NUM = models.IntegerField(primary_key=True)
    
    PROD_NAME = models.CharField(max_length=200,default="")
    MAKER_NAME = models.CharField(max_length=200,default="")
    FOOD_GROUP = models.CharField(max_length=200,default="")
    FOOD_CLASS = models.CharField(max_length=200,default="")
 
    SERV_SIZE = models.IntegerField(default=100)
    UNIT = models.CharField(max_length=10,default="g")
    CALORIES =  models.FloatField(default=0)
 
    TOTAL_CARB =  models.FloatField(default=0)
    SUGAR =  models.FloatField(default=0)
    DIETARY_FIBER =  models.FloatField(default=0)
    SUGAR_ALCOHOL = models.FloatField(default=0)
    ERYTHRITOL = models.FloatField(default=0)
 
    PROTEIN =  models.FloatField(default=0)
 
    TOTAL_FAT =  models.FloatField(default=0)
    SATURATED_FAT =  models.FloatField(default=0)
    TRANS_FAT =  models.FloatField(default=0)
 
    CHOLESTEROL =  models.FloatField(default=0)
    NATRIUM =  models.FloatField(default=0)
 
    RESEARCH_YEAR = models.IntegerField(default=0)
    REFERENCE = models.CharField(max_length=200,default="")
    SEARCH_SCORE = models.IntegerField(default=0)
 
    def __str__(self):
        return self.PROD_NAME
