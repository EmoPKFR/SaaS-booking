from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Service
from .serializers import ServiceSerializer
from .permissions import IsBusinessOwnerOfService
from businesses.models import Business


class ServiceViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticatedOrReadOnly(), IsBusinessOwnerOfService()]
        return [IsAuthenticatedOrReadOnly()]
    
    def perform_create(self, serializer):
        business_id = self.request.data.get('business_id')

        business = Business.objects.get(id=business_id)

        # Ensure the logged-in user owns this business
        if business.owner != self.request.user:
            raise PermissionError('You cannot add services to a business you don\'t own.')
        
        serializer.save(business=business)
