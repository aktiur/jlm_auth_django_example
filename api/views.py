from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework import permissions

from .serializers import UserSerializer


class UserView(RetrieveUpdateAPIView):
    """API view to retrieve and update the user profile
    """
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
