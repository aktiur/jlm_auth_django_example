from rest_framework.serializers import ModelSerializer

from accounts.models import User


class UserSerializer(ModelSerializer):
    """Standard user serializer
    """
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'city', 'country_code')
        read_only_fields = ('id', 'email')
