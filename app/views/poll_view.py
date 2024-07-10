from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from app.serializers.user_serializer import UserSerializer
from app.serializers.poll_serializers import PollSerializer
from app.services.poll_service import PollService


class PollViewSet(viewsets.ViewSet):

    _service = PollService()

    # GET
    def list(self, request):
        polls = self._service.get_all_polls()
        if polls['success']:
            return Response(polls['data'], status=status.HTTP_200_OK)
        return Response({'error': polls['error']}, status=status.HTTP_404_NOT_FOUND)

    # GEt
    def retrieve(self, request, pk=None):
        pass

    # POST
    def create(self, request):
        serializer = PollSerializer(data=request.data)
        print("Entrou 1")
        if serializer.is_valid():
            print("Entrou 2")
            poll = self._service.create_poll(serializer.validated_data)
            if poll['success']:
                print("Entrou 3")
                return Response(PollSerializer(poll['data']).data, status=status.HTTP_201_CREATED)
            return Response({'error': poll['error']}, status=status.HTTP_400_BAD_REQUEST)
        print("Erros de validação: ", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PUT
    def update(self, request, pk=None):
        pass

    # PATCH
    def partial_update(self, request, pk=None):
        return Response({'error': 'Not Implemented'})

    # DELETE
    def destroy(self, request, pk=None):
        pass