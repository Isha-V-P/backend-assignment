from rest_framework import serializers
from api.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        #fields=['id','first_name','last_name','company_name','city','state','zip','email','web','age']
        fields='__all__'
        #read_only_fields=['id','company_name','city','state','zip','email','web','age']