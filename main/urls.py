from rest_framework import routers
from django.urls import include, path
from .views import CategoryLIstViewSet, CategoryDetailViewSet, UserListView, UserDetailView, ClothesListViewSet,\
    ClothesColorListViewSet, ClothesSizeListViewSet, ClothesInStockListViewSet

app_name = 'main'

router = routers.DefaultRouter()

router.register(r'category-list', CategoryLIstViewSet, basename='category-list')
router.register(r'category-detail', CategoryDetailViewSet, basename='category-detail')
router.register(r'clothes-list', ClothesListViewSet, basename='clothes-list')
router.register(r'clothescolor-list', ClothesColorListViewSet, basename='clothescolor-list')
router.register(r'clothessize-list', ClothesSizeListViewSet, basename='clothessize-list')
router.register(r'clothesinstock-list', ClothesInStockListViewSet, basename='clothesinstock-list')


urlpatterns = [
    path('', include(router.urls)),
    path('user/', UserListView.as_view(), name='user-list'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]

