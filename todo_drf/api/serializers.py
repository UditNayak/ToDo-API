# Now, let’s start to dive deep into the serialization part of the data. We need to tell the REST Framework about our Task model and how to serialize it.

# To do so, let’s create a new file api/serializers.py.

# In this new file we have to do a few things:

# import our models
# import serializer from REST Framework
# Create a new class that links the Task with its serializer.

from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'