"==============================Swagger=============================="
# установите drf-yasg

# в INSTALLED_APPS добавьте 'drf_yasg'

# если используете jwt, то добавьте в settings.py
"""
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    }
}
"""

# в главных urls проекта создайте view для swagger
"""
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Python 21 API",
        description="makers bootcamp",
        default_version="v1",
    ),
    public=True
)
"""

# подключите view в urlpatterns

"""
urlpatterns = [
    ...
    path('docs/', schema_view.with_ui("swagger")),
    ...
]
"""


# если вам нужно дополнить документацию для ваших view можете декорировать их

# Например не отображается параметр для поиска
"""
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class ProductViewSet(ModelViewSet):

    @swagger_auto_schema(manual_parameters=[openapi.Parameter("title", openapi.IN_QUERY, "search products by title", type=openapi.TYPE_STRING)])
    @action(methods=["GET"], detail=False)
    def search(self, request):
        title = request.query_params.get("title")
        queryset = self.get_queryset()
        if title:
            queryset = queryset.filter(title__icontains=title)
        
        serializer = ProductSerializer(queryset, many=True, context={"request":request})
        return Response(serializer.data, 200)
"""

# Например если не отображаются поля при POST запросе (используйте сериализатор)
"""
from drf_yasg.utils import swagger_auto_schema

class RegistrationView(APIView):

    @swagger_auto_schema(request_body=RegistrationSerializer())
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response("Вы успешно зарегистрировались!")
"""
