# generic api view and model mixin
from django.db.models import query
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, CreateAPIView,ListCreateAPIView,RetrieveUpdateAPIView
# from rest_framework.generics import GenericAPIView
# from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# class StudentList(ListAPIView):   #vid 15
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class StudentCreate(CreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class StudentRetrieveUpdate(RetrieveUpdateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer




#model mixin
# class StudentList(GenericAPIView, ListModelMixin):  #vid 14
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def get(self, request, *args, **kwargs ):
#         return self.list(request, *args,**kwargs)

# class StudentCreate(GenericAPIView, CreateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def post(self, request, *args, **kwargs ):
#         return self.create(request, *args,**kwargs)

# class StudentRetrive(GenericAPIView,RetrieveModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def get(self,request,*args,**kwargs):
#         return self.retrieve(request,*args,**kwargsi)