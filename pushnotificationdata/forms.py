
from django.forms import ModelForm
from .models import SendHistory

class SendHistoryForm(ModelForm):
    class Meta:
        model = SendHistory
        fields = ['message','title']
