from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from core import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView 
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


router = routers.DefaultRouter()
router.register(r'categorias', views.CategoriaModelViewSet)
router.register(r'editora', views.EditoraViewSet)
router.register(r'autor', views.AutorViewSet)
router.register(r'livros', views.LivroViewSet)
router.register(r'compras', views.CompraViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('teste/', views.teste),
    path('teste2/', views.second_teste),
    path('categorias-class/', views.CategoriasView.as_view()),
    path('categorias-class/<int:id>/,', views.CategoriasView.as_view()),
    path('categorias-apiview/', views.CategoriasList.as_view()),
    path('categorias-apiview/<int:id>/', views.CategoriaDetail.as_view()),
    path('categorias-generics/', views.CategoriaListGeneric.as_view()),
    path('categorias-generics/<int:id>/', views.CategoriaGenericDetail.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # YOUR PATTERNS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api/', include(router.urls)), 
]
