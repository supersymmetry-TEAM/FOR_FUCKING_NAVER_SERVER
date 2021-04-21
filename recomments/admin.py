from django.contrib import admin
from recomments.models import Refoodcomment

class ReFoodCommentAdmin(admin.ModelAdmin):

    fields = ["foodcomment", 'author', 'text','up','down',"token",]


    search_fields = ('food','author',)

admin.site.register(Refoodcomment, ReFoodCommentAdmin)

    # token = models.CharField(max_length=500)
    # comment_id = models.ForeignKey(FoodComment,on_delete=models.CASCADE)
    # text = models.TextField()
    # created_date = models.DateTimeField(auto_now_add=True)
    # token = models.CharField(max_length=500)
    # author = models.CharField(max_length=500)
