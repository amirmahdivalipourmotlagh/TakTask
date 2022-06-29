from dataclasses import fields
from rest_framework import serializers
from user.models import *
from Task.models import *
from django.core import serializers as ser

class userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields='__all__'
class user_describtionserializer(serializers.ModelSerializer):
    user = userserializer(many=False)
    class Meta:
        model = User_describtion
        fields = '__all__'

class userforteamserializer(serializers.ModelSerializer):
    class Meta:
        model = User_describtion
        fields = ['username','id']

class teamserializer(serializers.ModelSerializer):
    # manager = user_describtionserializer(many=False)
    users=userforteamserializer(many=True)
    class Meta:
        model = Team
        fields = '__all__'

class spendserializer(serializers.ModelSerializer):
    class Meta:
        model = SpentTime
        fields = ['id','start_time','start_date','spended']

# class spendserializer(serializers.ModelSerializer):
#     class Meta:
#         model = SpentTime
#         fields = '__all__'

class taskserializer(serializers.ModelSerializer):
    # category_name = serializers.RelatedField(source='category', read_only=True)
    time_spented_up = spendserializer(many=True)
    class Meta:
        model = task
        fields = '__all__'

