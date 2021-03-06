from rest_framework import serializers
from locations.serializers import LocationSerializer, LanguageSerializer
from institutions.serializers import InstitutionSerializer, CareerSerializer
from django.contrib.auth.models import User
from users.models import UserDetail
#from tutorias.serializers import TutorSerializer


class UserDetailSerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    institution = InstitutionSerializer()
    language = LanguageSerializer()
    career = CareerSerializer()

    class Meta:
        model = UserDetail
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    userdetail = UserDetailSerializer(many = False)
    # tutor = TutorSerializer(many = False)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'userdetail',
        )

