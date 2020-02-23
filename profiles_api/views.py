from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import HelloSerializer


class HelloApiView(APIView):
    """
    Testing a simple API view
    """
    api_view = [
        'This is the sentence 1',
        'This is the sentence 2',
        'This is the sentence 3',
        'This is the sentence 4',
    ]
    serializer_class = HelloSerializer

    def get(self, request, format=None):
        """Responses the get request"""
        return Response({'message': 'Abay Saalay', 'api_view': self.api_view})

    def post(self, request):
        """Responses the post request of API"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle the update requests of API"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'changed to {name}'
            return Response({'method': 'PUT', 'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

    def patch(self, request, pk=None):
        """Handle partial updates requests of the API"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Handle the delete requests of the API"""
        return Response({'method': 'DELETE'})
