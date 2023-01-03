"=======================APIView======================="
# APIView - класс, который позволяет вам на классах писать view
# тот метод, который вы переопределите в своем классе, тот и будет обрабатывать ваша view
# (get, post, put, patch, delete)

# вы можете переопределить аттрибут permission_classes и передать список из permissions

"=======================ViewSet======================="
# ViewSet - класс, который позволяет обрабатывать сразу все запросы в одном классе (но его нужно подключать в urls через router (rest_framework.routers.SimpleRouter / rest_framework.routers.DefaultRouter))

# viewset включает в себя сразу все методы (create, retrieve, update, partial_update, destroy, list), которые по желанию можно переопределить (они как и обычные view принимают в себя request и если это не методы (create и list), то они так же принимают pk (например id))

# Например
"""
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(ViewSet):

    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Product.objects.all()
        product = get_object_or_404(queryset, pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
"""

# если же вы хотите добавить свою view во viewset, то можете воспользоваться декоратором action (rest_framework.decorators.action). декоратор принимает в себя ключевые аргументы 
# detail - если True, значит в функцию будет приходить pk (например id)
# methods - список с методами, которые обрабатывает эта функция

# Например
"""
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Product, Like
from .serializers import ProductSerializer

class ProductViewSet(ViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['put'])
    def toggle_like(self, request, pk=None):
        user = request.user
        product = get_object_or_404(Product, id=pk) # product = self.get_object()
        if Like.objects.filter(user=user, product=product).exists():
            Like.objects.filter(user=user, product=product).delete()
        else:
            Like.objects.create(user=user, product=product)
        return Response("Like toggled", 200)
"""


"====================ModelViewSet===================="
# ModelViewSet - более удобная версия ViewSet

# достаточно переопределить аттрибуты
'queryset' # - обьекты, которые будут использоваться
'serializer_class' # - сериализатор, который будет использоваться

# дополнительно можно переопределить
'permission_classes' # - список с permissions
'filter_backends' # - список с классами для фильтрации (например rest_framework.filters.OrderingFilter)
'ordering_fields' # - список с полями по которым будет сортироваться ваш queryset

# так же если вашему сериализатору нужно передать данные со view помимо обьектов для сериализации, то можно переопределить метод get_serializer_context

# Например
"""
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context
"""

# так же если вы хотите поставить permissions не на все ваши функции (views) в этом viewset, то можете переопределить метод get_permissions

# Например
"""
    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        return [IsAuthorOrAdminPermission()]
"""
# self.action - может быть одним из (create, retrieve, update, partial_update, destroy, list), а так же одним из методов, которые задекорированы action

