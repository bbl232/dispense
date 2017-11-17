from django.contrib.auth.models import User, Group
from dispense.models import License
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class LicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = License
        fields = ('url', 'body', 'expiry', 'type', 'tags', 'consumed_by', 'created_date', 'updated_date')

