from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from home.models import Person
from home.serializers import *
from rest_framework import viewsets
from rest_framework import status
from django.contrib.auth.models import User
class RegisterAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data,)
        if not serializer.is_valid():
            return Response({'status':False, 
            'message':serializer.errors},
            status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response({
            'status':True, 
            'message':'user created'}, status.HTTP_201_CREATED)
class PersonViewSet(viewsets.ModelViewSet):
    serializer_class= PersonSerializer
    queryset= Person.objects.all()
    # to define search finctionality here...
    def list(self, request):
        search = request.GET.get('search')
        queryset=self.queryset
        if search:
            queryset= queryset.filter(name__contains= search)
        serializer = PersonSerializer(queryset, many = True)
        return Response({'status':status.HTTP_200_OK, 'data':serializer.data})

class PersonAPI(APIView):
    def get(self, request):
        objects = Person.objects.filter(color__isnull= False)
        # here many= True means that the data being passed as an object has length of more than one.
        serializer = PersonSerializer(objects, many = True)
        return Response(serializer.data)
        # return Response({'message':'this is a get method'})
    def post(self, request):
        data = request.data
        # to check the validity of the data from the post method
        serializer= PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
        # return Response({'message':'this is a post method'})
    def put(self, request):
        data= request.data
        object = Person.objects.get(id = data['id'])
        serializer= PersonSerializer(object, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
        # return Response({'message':'this is a put method'})
    def patch(self, request):
        data = request.data
        object = Person.objects.get(id = data['id'])
        serializer = PersonSerializer(object,  data=data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
        # return Response({'message':'this is a patch method'})
    def delete(self, request):
        data = request.data
        try:
            object= Person.objects.get(id = data['id'])
            object.delete()
            return Response({'message':f'{object.name} is deleted.'})
        except Person.DoesNotExist:
            return Response({
                'message':'This person does not exist in our database.',
                'status':404})
        # return Response({'message':'this is a delete method'})
@api_view(['GET', 'POST', 'PUT'])
def login(request):
    data = request.data
    serializer = LoginSerializer(data= data)
    if serializer.is_valid():
        data = serializer.validated_data
        return Response({'message':'passed'})
@api_view(['GET', 'POST', 'PUT', 'PATCH','DELETE'])
def index(request):
    courses = {
        'course_name':'Python',
        'learn':['flask', 'django', 'Tornado', 'FastAPI'],
        'course_provider':'Scaler'
    }
    if request.method=='GET':
        # to fetch data from the GET method use the following code the url for this is http://127.0.0.1:8000/api/index/?search=Himanshu+Chaurasiya here the + sign in the name will result into spaces

        # print(request.GET.get('search'))
        print(request.GET.get('username'))
        print(request.GET.get('password'))
        return Response(courses)
    elif request.method =='POST':
        data = request.data
        print(data)
        return Response({
            'course_name':'Python POST',
        'learn':['flask', 'django', 'Tornado', 'FastAPI'],
        'course_provider':'Scaler POST'
        })
@api_view(['GET', 'POST', 'PUT', 'PATCH','DELETE'])
def person(request):
    if request.method =='GET':
        objects = Person.objects.filter(color__isnull= False)
        # here many= True means that the data being passed as an object has length of more than one.
        serializer = PersonSerializer(objects, many = True)
        return Response(serializer.data)
    elif request.method=='POST':
        data = request.data
        # to check the validity of the data from the post method
        serializer= PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    # PUT method does not support partial update unlike PATCH
    elif request.method =='PUT':
        data= request.data
        object = Person.objects.get(id = data['id'])
        serializer= PersonSerializer(object, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    # PATCH method supports partial update unlike PUT
    elif request.method=='PATCH':
        data = request.data
        object = Person.objects.get(id = data['id'])
        serializer = PersonSerializer(object,  data=data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        data = request.data
        try:
            object= Person.objects.get(id = data['id'])
            object.delete()
            return Response({'message':f'{object.name} is deleted.'})
        except Person.DoesNotExist:
            return Response({
                'message':'This person does not exist in our database.',
                'status':404})
       
    