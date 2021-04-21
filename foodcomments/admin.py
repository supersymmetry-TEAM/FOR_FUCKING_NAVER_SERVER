from django.contrib import admin
from foodcomments.models import Foodcomment

class FoodCommentAdmin(admin.ModelAdmin):

    fields = ['food', 'author', 'text','up','down',"token", "is_up_list", "is_down_list",]

    search_fields = ('food',)

admin.site.register(Foodcomment, FoodCommentAdmin)

    # food = models.CharField(max_length=300)
    # token = models.CharField(max_length=500)
    # author = models.CharField(max_length=500)
    # text = models.TextField()
    # created_date = models.DateTimeField(auto_now_add=True)
