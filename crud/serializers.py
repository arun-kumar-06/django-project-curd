from rest_framework import serializers #importing restfrmaework
from .models import *
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields =["id","title","content","slug"]
    def to_internal_value(self, data):
        if data.get('title', None) == '':
            data.pop('title')
        return super(PostSerializer, self).to_internal_value(data)
