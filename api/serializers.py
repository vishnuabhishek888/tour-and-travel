from rest_framework import serializers
from api.models import User, Area_Cities, State, Destination, Pick_Up, Drop, Transfer, Activities, Trip_Detail

class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
      model = User
      fields=['email','name','password','password2','tc']
      extra_kwargs={
         'password':{'write_only':True}
      }


    def validate(self, attrs):
      password = attrs.get('password')
      password2 = attrs.get('password2')
      if password != password2:
         raise serializers.ValidationError("Password and Confirm Password doesn't match")
      return attrs
    

    def create(self, validated_data):
       password = validated_data.pop('password2')
       user = User.objects.create_user(**validated_data)
       user.set_password(password)
       user.save()
       return user

    
class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
      model = User
      fields = ['email','password']



class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model =State
        fields = '__all__'

class Area_CitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model =Area_Cities
        fields = '__all__'

class DestinationSerializer(serializers.ModelSerializer):
    # area_cities =serializers.StringRelatedField(many=True, read_only=True)
    # state =serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
       model = Destination
       fields = ['id', 'name', 'area_cities', 'state', 'ts']

class Pick_UpSerializer(serializers.ModelSerializer):
    class Meta:
       model = Pick_Up
       fields = '__all__'
   
class DropSerializer(serializers.ModelSerializer):
    class Meta:
       model = Drop
       fields = '__all__'

class TransferSerializer(serializers.ModelSerializer):
    class Meta:
       model = Transfer
       fields = '__all__'

class ActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
       model = Activities
       fields = '__all__'

class Trip_DetailSerializer(serializers.ModelSerializer):
   class Meta:
      model = Trip_Detail
      fields = '__all__'