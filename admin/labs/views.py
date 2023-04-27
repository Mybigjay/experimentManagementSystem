from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Labs, User
#from .producer import publish
from .serializers import LabsSerializer
import random


class LabsViewSet(viewsets.ViewSet):
    def list(self, request):
        labs = Labs.objects.all()
        serializer = LabsSerializer(labs, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = LabsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
       # publish('lab_created', serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        lab = Labs.objects.get(id=pk)
        serializer = LabsSerializer(lab)
        return Response(serializer.data)

    def update(self, request, pk=None):
        lab = Labs.objects.get(id=pk)
        serializer = LabsSerializer(instance=lab, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('lab_updated', serializer.data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        lab = Labs.objects.get(id=pk)
        lab.delete()
        publish('lab_deleted', pk)
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserAPIView(APIView):
    def get(self, _):
        users = User.objects.all()
        user = random.choice(users)
        return Response({
            'id': user.id
        })
