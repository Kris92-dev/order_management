from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . models import *
from . serializers import *
# Create your views here.


@api_view(['GET'])
def consumers(request):
    consumers = Consumer.objects.all()
    serializer = consumerSerializer(consumers, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addConsumer(request):
    serializer = consumerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def products(request):
    products = Product.objects.all()
    serializer = productSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addProduct(request):
    serializer = productSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

def ledger(request):
    consumers = Consumer.objects.all()
    products = Product.objects.all()
    orders = Orders.objects.all()
    transactions = Transactions.objects.all()
    context = {'consumers': consumers, 'products': products,
               'orders': orders, 'transactions': transactions}
    return render(request, 'ledger.html', context)    

# Use django admin to add orders and transactions

@api_view(['GET'])
def order(request):
    orders = Orders.objects.all()
    serializer = orderSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addOrder(request):
    serializer = orderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def transaction(request):
    transactions = Transactions.objects.all()
    serializer = transactionSerializer(transactions, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addTransaction(request):
    serializer = transactionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)    


        


