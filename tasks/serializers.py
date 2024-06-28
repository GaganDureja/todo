from rest_framework import serializers
from .models import Tasks
from datetime import date

class TasksSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tasks
    fields = '__all__'

  def validate_due_date(self, value):
    if value and value < date.today():
      raise serializers.ValidationError("Due date should be a future date.")
    return value