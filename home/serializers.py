from .models import *
from django.contrib.auth.models import User
from rest_framework import serializers
class RegisterSerializer (serializers.Serializer):
    username= serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    def validate(self, data):
        if data['username']:
            if User.objects.filter(username = data['username']).exists():
                raise serializers.ValidationError('username is taken.')
        if data['email']:
            if User.objects.filter(email = data['email']).exists():
                raise serializers.ValidationError('email is taken.')
        return data
    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'], 
            email = validated_data['email']
            )
        user.set_password(validated_data['password'])
        return validated_data

class LoginSerializer (serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields =['color_name']
class PersonSerializer(serializers.ModelSerializer):
    # SERIALIZER METHOD FIELLD
    # color_info = serializers.SerializerMethodField()
    # def get_color_info(self, object):
    #     color = Color.objects.get(id= object.color.id)
    #     return {'color_name':color.color_name,'hex_code':'#FF0000'}
        # return 'INDIA'

    # color = ColorSerializer() # this will cause the api to pass data in the api what was defined in the colorSerializer class.
    class Meta:
        model = Person
        # this will fetch all the field of the foreign key related to Person model.
        # depth = 1

        # to serialize all the fields write
        fields = '__all__'
        # to serialize some particular fields write
        # here if the model has many attributes then only the given values in the list are required in the POST method ie here name and age is required for the POST method.
        # fields= ['name', 'age']
        # and to exclude any of the field we can write it as
        # exclude = ['name', 'age'] # in this example name and age will not be serialized in the json
    # to validate the data we can write the following code
    # def validate(self, data):
    #     special_charecters = '!@#$%^&*()_-+=<>,./?:";\'[]|'
    #     if any(c in special_charecters for c in data['name']):
    #         raise serializers.ValidationError('Name can not contain special chars.')
    #     if data['age']<18:
    #         raise serializers.ValidationError('Age must be greater than 18.')
    #     # if data['name']
    #     return data

