from rest_framework import viewsets, mixins, generics, permissions
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Clothes, Category, Brand
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadyOnly, IsClothesOwnerOrReadOnly
from .serializers import CategorySerializer, CategoryDetailSerializer, UserSerializer, ClothesListSerializer,\
    ClothesColorSerializer, ClothesInStockSerializer, ClothesSizeSerializer


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CategoryLIstViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAdminUser,)


class CategoryDetailViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    permission_classes = (permissions.IsAdminUser,)


class ClothesListViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Clothes.objects.all()
    serializer_class = ClothesListSerializer
    permission_classes = (IsOwnerOrReadyOnly,)

    def perform_create(self, serializer):
        serializer.save(onwer=self.request.user)
        return super().perform_create(serializer)


class ClothesColorListViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Clothes.objects.all()
    serializer_class = ClothesColorSerializer


class ClothesSizeListViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Clothes.objects.all()
    serializer_class = ClothesSizeSerializer
    permission_classes = (IsAdminOrReadOnly,)


class ClothesInStockListViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Clothes.objects.all()
    serializer_class = ClothesInStockSerializer
    permission_classes = (IsClothesOwnerOrReadOnly,)



# Create your views here.
