from rest_framework import serializers
from .models import Event



class testserializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('title', 'naam', 'beschrijving', 'begin_datum', 'eind_datum', 'start_tijd', 'eind_tijd')


    def create(self, validated_data):
        return Event.object.create(validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.naam = validated_data.get('naam', instance.naam)
        instance.beschrijving = validated_data.get('beschrijving', instance.beschrijving)
        instance.begin_datum = validated_data.get('begin_datum', instance.begin_datum)
        instance.eind_datum = validated_data.get('eind_datum', instance.eind_datum)
        instance.start_tijd = validated_data.get('start_tijd', instance.start_tijd)
        instance.eind_tijd = validated_data.get('eind_tijd', instance.eind_tijd)

        instance.save()
        return instance