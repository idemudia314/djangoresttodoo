from django.shortcuts import render
from todos.serializers import TodoSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from todos.models import Todo

from rest_framework.permissions import IsAuthenticated
# Create your views here.
from rest_framework import permissions, filters
from todos.pagination import CustomPageNumberPagination


from django_filters.rest_framework import DjangoFilterBackend





class TodosAPIView(ListCreateAPIView):
    serializer_class = TodoSerializer
    pagination_class = CustomPageNumberPagination
    permission_classes = (IsAuthenticated,)
    filter_backends =[DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['id', 'title', 'is_complete', 'desc']
    search_fields = ['id', 'title', 'is_complete', 'desc']
    ordering_fields = ['id', 'title', 'is_complete', 'desc']


    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    
    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)



class TodoDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"


    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)










#class CreateTodoAPIView(CreateAPIView):
    #serializer_class = TodoSerializer
    #permission_classes = (IsAuthenticated,)

    #def perform_create(self, serializer):
        #return serializer.save(owner=self.request.user)


#class TodoListAPIView(ListAPIView):
    #serializer_class = TodoSerializer
   # permission_classes = (IsAuthenticated,)
    
   # def get_queryset(self):
   #     return Todo.objects.filter(owner=self.request.user)

