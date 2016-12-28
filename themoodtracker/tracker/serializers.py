from rest_framework import serializers
from tracker.models import Mood

class MoodSerializer(serializers.ModelSerializer):
	# name = serializers.CharField(max_length=128, null=False, blank=False)
	# date_added = serializers.DateField()
	class Meta:
		model = Mood
		fields = ('name',)