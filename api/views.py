from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from api.serializers import *
from django.contrib.auth import authenticate
from rest_framework import viewsets
from .models import Area_Cities, State, Destination, Pick_Up, Drop, Transfer, Activities, Trip_Detail



class UserRegistrationView(APIView):
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response({'msg':'Registration Success'}, status=status.HTTP_201_CREATED)
        return Response({'msg':'Registration Success'})

class UserLoginView(APIView):
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                return Response({'msg':'Login Success'}, status=status.HTTP_200_OK)
            else:
                return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
 
class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer

class Area_CitiesViewSet(viewsets.ModelViewSet):
    queryset = Area_Cities.objects.all()
    serializer_class = Area_CitiesSerializer

class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

class Pick_UpViewset(viewsets.ModelViewSet):
    queryset = Pick_Up.objects.all()
    serializer_class = Pick_UpSerializer

class DropViewset(viewsets.ModelViewSet):
    queryset = Drop.objects.all()
    serializer_class = DropSerializer

class TransferViewset(viewsets.ModelViewSet):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer

class ActivitiesViewset(viewsets.ModelViewSet):
    queryset = Activities.objects.all()
    serializer_class = ActivitiesSerializer

class Trip_DetailViewset(viewsets.ModelViewSet):
    queryset = Trip_Detail.objects.all()
    serializer_class = Trip_DetailSerializer