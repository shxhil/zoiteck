from rest_framework import serializers
from api.models import Profile
from django.contrib.auth.models import User

class SignUpSerializer(serializers.ModelSerializer):
    class Meta():
        model=User
        fields=["id","username","email","password"]
        read_only_fields=["id"]
    
        
    def create(self,validated_data):
        return User.objects.create_user(**validated_data)
    
class ProfileSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField()
    class Meta:
        model=Profile
        fields=["user","about","dob","profile_pic","gender"]
        read_only_fields=["id","user"]