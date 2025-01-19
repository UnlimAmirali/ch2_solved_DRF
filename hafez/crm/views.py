from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import PersonalInfo, InsuranceInfo
from .serializers import PersonalInfoSerializer, InsuranceInfoSerializer

class PersonalInfoViewSet(ModelViewSet):
    queryset = PersonalInfo.objects.all()
    serializer_class = PersonalInfoSerializer
    permission_classes = [IsAuthenticated]

class InsuranceInfoViewSet(ModelViewSet):
    queryset = InsuranceInfo.objects.all()
    serializer_class = InsuranceInfoSerializer
    permission_classes = [IsAuthenticated]
