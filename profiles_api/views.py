from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import filters, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.authentication import TokenAuthentication
from .serializers import HelloSerializer, UserProfileSerializer, CustomAuthTokenSerializer
from .models import UserProfile
from .permissions import UpdateOwnProfile


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


class HelloApiViewset(viewsets.ViewSet):
    """Testing API viewsets"""

    serializer_class = HelloSerializer

    a_viewset = [
        'This is sentence 1',
        'This is sentence 2',
        'This is sentence 3',
    ]

    def list(self, request):
        """Handles the get requests"""
        return Response({'message': 'Abay Saaalay!', 'a_viewset': self.a_viewset})

    def create(self, request):
        """Creates(POST HTTP request) a new object and show from serializer"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

    def retrieve(self, request, pk=None):
        """Handles the retrieve (GET) request"""
        return Response({'method': 'Retrieve(GET)'})

    def update(self, request, pk=None):
        """Handles the Update(put) request"""
        return Response({'method': 'UPDATE (put)'})

    def partial_update(self, request, pk=None):
        """Handles the partial update (patch)"""
        return Response({'method': 'Partial_update (PATCH)'})

    def destroy(self, request, pk=None):
        """Handles the delete request"""
        return Response({'method': 'Destroy (DELETE)'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating and updating user profiles"""

    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, UpdateOwnProfile)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """Handle the user authentication in our system"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    serializer_class = CustomAuthTokenSerializer
