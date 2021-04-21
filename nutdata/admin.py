from django.contrib import admin
from .models import NutData_0, NutData_1
from import_export.admin import ImportExportModelAdmin
from import_export import resources
    
class NutDataResource_1(resources.ModelResource):
    class Meta:
        model = NutData_1
        import_id_fields = ('NUM',)
        fields = ['NUM', 
 
    'PROD_NAME', 
    'MAKER_NAME', 
    'FOOD_GROUP',
    'FOOD_CLASS', 
 
    'SERV_SIZE', 
    'UNIT' ,
    'CALORIES', 
 
    'TOTAL_CARB', 
    'SUGAR', 
    'DIETARY_FIBER', 
    'SUGAR_ALCOHOL', 
    'ERYTHRITOL' ,
 
    'PROTEIN' ,
 
    'TOTAL_FAT', 
    'SATURATED_FAT', 
    'TRANS_FAT', 
 
    'CHOLESTEROL', 
    'NATRIUM' ,
 
    'RESEARCH_YEAR', 
    'REFERENCE', 
    'SEARCH_SCORE',] 



  
class NutDataAdmin_1(ImportExportModelAdmin):
    resource_class = NutDataResource_1

admin.site.register(NutData_1,NutDataAdmin_1)

# Register your models here.
