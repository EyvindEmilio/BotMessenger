from pprint import pprint

from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
import json
# Create your views here.
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
import requests

ACCESS_TOKEN = 'EAAZA7WeAG5PgBAHJUVeVYu82hJKwaSOZBWYLYVRYsKGmN3Up3Mj94sbOgIZCOChnjTF8vkvVP9LGreMHzer6HF0CYhzw30CWynKwDJnaDTvqEtovVJOj2rqRmzL5ikoFfVfS6gGktXzZBlkOMhrk1NH8FvZAMe8t3cl97uKCoZAgZDZD'


class BotView(generic.View):
    def get(self, request, *args, **kwargs):
        if self.request.GET['hub.verify_token'] == 'botsoydigital':
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, Access Token is Invalid!')


def reply(user_id, msg):
    data = {
        "recipient": {"id": user_id},
        "message": {"text": msg}
    }
    resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + ACCESS_TOKEN, json=data)
    print(resp.content)


@method_decorator(csrf_exempt, name='dispatch')
class MessageView(generic.View):
    def post(self, request):
        data = json.loads(request.body)
        # return JsonResponse(data)
        sender = data['entry'][0]['messaging'][0]['sender']['id']
        message = data['entry'][0]['messaging'][0]['message']['text']
        reply(sender, message[::-1])
        return "ok"

        # json_data = json.loads(request.body)
        # try:
        #     data = json_data['data']
        # except KeyError:
        #     HttpResponse(0)
        #     HttpResponse(0)
