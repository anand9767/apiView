
from django.contrib import admin
from django.db import router
from django.urls import path
from django.urls.conf import include
from api import views
from rest_framework.routers import DefaultRouter
# from django.conf.urls import url,include

router = DefaultRouter()

router.register('studentapi',views.StudentModelViewSet,basename = 'student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    # path('studentapi/',views.StudentModelViewSet.as_view()),
    # path('studentapi/',views.StudentCreate.as_view()),
    # path('studentapi/<int:pk>/',views.StudentRetrieveUpdate.as_view())

]