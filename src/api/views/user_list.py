from rest_framework.viewsets import ModelViewSet
from apps.users.models import User
from rest_framework.permissions import AllowAny
from api.serializer.user_app import UserListSeralizers
from api.paginations import MyCustomPaginator


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserListSeralizers
    permission_classes = [AllowAny]
    pagination_class = MyCustomPaginator
