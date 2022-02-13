from rest_framework import serializers
from . models import *

class consumerSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Consumer
        fields = '__all__'

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Product
        fields = '__all__'

class orderSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Orders
        fields = '__all__'

class transactionSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Transactions
        fields = '__all__'                