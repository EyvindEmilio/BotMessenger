from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import generic


class BotView(generic.View):
    def get(self, request, *args, **kwargs):
        if self.request.GET['hub.verify_token'] == 'botsoydigital':
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, Access Token is Invalid!')
