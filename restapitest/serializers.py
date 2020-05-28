from rest_framework import serializers
from .models import Test



class testserializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ('name', 'email', 'message', 'created_at')



    def create(self, validated_data):
        return Test.object.create(validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.message = validated_data.get('message', instance.message)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.save()
        return instance