from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from book.views import BookView
from person.views import PersonView
from myapp import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'person', PersonView)
router.register(r'book', BookView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('person/', include('rest_framework.urls', namespace='person')),
    path('book/', include('rest_framework.urls', namespace='book')),
]
