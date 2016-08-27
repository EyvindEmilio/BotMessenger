from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import generic


class BotView(generic.View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("bot")
