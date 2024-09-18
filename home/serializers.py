from .models import Person
from rest_framework import serializers
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        # this will fetch all the field of the foreign key related to Person model.
        depth = 1

        # to serialize all the fields write
        fields = '__all__'
        # to serialize some particular fields write
        # here if the model has many attributes then only the given values in the list are required in the POST method ie here name and age is required for the POST method.
        # fields= ['name', 'age']
        # and to exclude any of the field we can write it as
        # exclude = ['name', 'age'] # in this example name and age will not be serialized in the json
    # to validate the data we can write the following code
    def validate(self, data):
        if data['age']<18:
            raise serializers.ValidationError('Age must be greater than 18.')
        special_charecters = '!@#$%^&*()_-+=<>,./?:";\'[]|'
        if any(c in special_charecters for c in data['name']):
            raise serializers.ValidationError('Name can not contain special chars.')
        # if data['name']
        return data

