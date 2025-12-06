from django.contrib import admin
from django.urls import include, path

from django.http import JsonResponse

def home(request):
    return JsonResponse({
        "message": "Django Stocks Products API is running!",
        "endpoints": {
            "admin": "/admin/",
            "api": "/api/v1/",
            "products": "/api/v1/products/",
            "stocks": "/api/v1/stocks/"
        }
    })

urlpatterns = [
    path('', lambda r: JsonResponse({"message": "API is working!"})),
    path('admin/', admin.site.urls),
    path('api/v1/', include('logistic.urls')),
]
