from django.contrib.auth.models import User, Group
from dispense.models import License
from rest_framework import viewsets
from dispense.serializers import UserSerializer, GroupSerializer, LicenseSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class LicenseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows licenses to be viewed or edited.
    """
    queryset = License.objects.all().order_by('-created_date')
    serializer_class = LicenseSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
