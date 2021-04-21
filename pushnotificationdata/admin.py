from django.contrib import admin
from .models import ExpoPushToken
from .forms import SendHistoryForm
from exponent_server_sdk import (
    DeviceNotRegisteredError,
    PushMessage,
    PushClient,
    PushServerError,PushTicketError,
)
from requests.exceptions import ConnectionError, HTTPError

class ExpoPushTokenAdmin(admin.ModelAdmin):
    list_display = ['userId', 'expotoken']
    fields = ['userId', 'expotoken']
    def changelist_view(self, request, extra_context=None):
        send_form = SendHistoryForm()
        extra_context = extra_context or {"form": send_form}
        if request.method == 'POST':
            title = request.POST.getlist('title')[0]
            message = request.POST.getlist('message')[0]
            send_push_message(message,title)
            return super().changelist_view(request,extra_context=extra_context)
        return super().changelist_view(request, extra_context=extra_context)

admin.site.register(ExpoPushToken, ExpoPushTokenAdmin)

def send_push_message(message,title ,extra=None):
    try:
        expotoken = [Object.expotoken for Object in ExpoPushToken.objects.all()]
        PushMessage_packet = []
        for token_packet in expotoken:
            PushMessage_packet.append(            
                PushMessage(
                        to=token_packet,
                        title=title,
                        display_in_foreground=True,
                        body=message,
                        data=extra))

        response_wow = PushClient().publish_multiple(PushMessage_packet)
#        for response_element in response_wow:
#            response_element.validate_response()

    except PushServerError as exc:
        print("PushServerError")
    except (ConnectionError, HTTPError) as exc:
        print("ConnectionError")
    try:
        # We got a response back, but we don't know whether it's an error yet.
        # This call raises errors so we can handle them with normal exception
        # flows.
         for response_element in response_wow:
            response_element.validate_response()
    except DeviceNotRegisteredError as exc:
        print("DeviceNotRegisterdError")
    except PushTicketError as exc:
        print("PushTicketError")
# Register your models here.
