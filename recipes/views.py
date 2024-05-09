from rest_framework import status, authentication, permissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .permissions import IsCreator
from .serializers import *
from .models import *


class CategoryModelViewset(ModelViewSet):
    queryset = Category.objects.all()
    http_method_names = ["get", "post", "put", "delete"]
    serializer_class = CategorySerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer_class()
        serializer = serializer(queryset, many=True)

        return Response({
            'message': 'List Of Recipe Categories.',
            'status': status.HTTP_200_OK,
            'data': serializer.data
        })

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'message': 'Recipe Category Created Successfully!',
            'status': status.HTTP_201_CREATED,
            'data': serializer.data
        })

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response({
            'message': 'Recipe Category Updated Successfully!',
            'status': status.HTTP_200_OK,
            'data': serializer.data
        })

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            'message': 'Recipe Category Deleted Successfully!',
            'status': status.HTTP_200_OK,
            'data': []
        })


class IngredientsModelViewset(ModelViewSet):
    queryset = Ingredient.objects.all()
    http_method_names = ["get", "post", "put", "delete"]
    serializer_class = IngredientSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer_class()
        serializer = serializer(queryset, many=True)

        return Response({
            'message': 'List Of Ingredients.',
            'status': status.HTTP_200_OK,
            'data': serializer.data
        })

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'message': 'Ingredient Created Successfully!',
            'status': status.HTTP_201_CREATED,
            'data': serializer.data
        })

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response({
            'message': 'Ingredient Updated Successfully!',
            'status': status.HTTP_200_OK,
            'data': serializer.data
        })

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            'message': 'Ingredient Deleted Successfully!',
            'status': status.HTTP_200_OK,
            'data': []
        })


class RecipeModelViewset(ModelViewSet):
    queryset = Recipe.objects.all()
    http_method_names = ["get", "post", "put", "delete"]
    serializer_class = RecipeSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsCreator]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(user=request.user)
        serializer = self.get_serializer_class()
        serializer = serializer(queryset, many=True)

        return Response({
            'message': 'List Of Recipes.',
            'status': status.HTTP_200_OK,
            'data': serializer.data
        })

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data, context={'user': request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'message': 'Recipe Created Successfully!',
            'status': status.HTTP_201_CREATED,
            'data': serializer.data
        })

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        user = request.user
        serializer = self.get_serializer(instance, data=request.data, context={'user': user})
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response({
            'message': 'Recipe Updated Successfully!',
            'status': status.HTTP_200_OK,
            'data': serializer.data
        })

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            'message': 'Recipe Deleted Successfully!',
            'status': status.HTTP_200_OK,
            'data': []
        })



