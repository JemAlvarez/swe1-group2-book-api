# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'publisher', views.PublisherViewSet)
router.register(r'genre', views.GenreViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('books/', views.book),
    path('books/<str:isbn>', views.getBookByISBN),
    path('author/', views.author),
    path('author/<str:name>/books', views.getAuthorBooks),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework')),
    path('wishlist/<str:user>', views.getWishlistByUser)
]