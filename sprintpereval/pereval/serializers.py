import serializers as serializers
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Coords, Level, PerevalAdded, Images, Users



class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = '__all__'
        verbose_name = 'Координаты'


class LevelSerialize(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'


class UsersSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='first_name')
    fam = serializers.CharField(source='last_name')
    otc = serializers.CharField(source='patronymic')
    email = serializers.CharField()
    phone = serializers.CharField()
    
    class Meta:
        model = User
        fields = ('email', 'fam', 'name', 'otc', 'phone')
        verbose_name = 'Пользователь'
    


class ImagesSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Images
        fields = ('data', 'title')
        verbose_name = 'Изображение'


class PerevalSerializer(serializers.ModelSerializer):
    user = UsersSerializer()
    coords = CoordsSerializer()
    level = LevelSerialize()
    images = ImagesSerializer(many=True)

    class Meta:
        model = PerevalAdded
        exclude = ('id', 'status')
    
class PerevalSubmitDataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PerevalAdded
        fields = '__all__'
        
class PerevalSubmitDataUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Users
        exclude = ('fam', 'email', 'phone')


class PerevalSubmitDataListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'