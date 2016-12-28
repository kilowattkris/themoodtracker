from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from tracker.models import Mood
from datetime import datetime
from tracker.serializers import MoodSerializer
from rest_framework import generics
import json

# Create your views here. generics.RetrieveUpdateDestroyAPIView
def mood(request, year, month, day):
    datestring = year+'-'+month+'-'+day
    date = datetime.strptime(datestring, '%Y-%m-%d')
    mood = Mood.objects.filter(date_added = date)
    serializers = MoodSerializer
    data = serializers.serialize('json', mood)
    return HttpResponse(data)
    # serializer.data

def moods(request):
    return render(request, 'tracker/moods.html')

class MoodList(generics.ListAPIView):
    serializer_class = MoodSerializer

    # def get(self, request, *args, **kwargs):
    #   year = self.kwargs['year']
    #   month = self.kwargs['month']
    #   day = self.kwargs['day']
    #   datestring = year+'-'+month+'-'+day
    #   date = datetime.strptime(datestring, '%Y-%m-%d')
    #   mood = Mood.objects.filter(date_added = date)

    def get_queryset(self):
        queryset = Mood.objects.all()
        # username = self.request.query_params.get('username', None)
        datestring = self.request.query_params.get('date', None)
        # if username is not None:
        #     queryset = queryset.filter(username=username)
        if datestring is not None: 
            date = datetime.strptime(datestring, '%Y-%m-%d')
            queryset = queryset.filter(date_added=date)
        return queryset
