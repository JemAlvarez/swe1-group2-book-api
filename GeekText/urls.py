# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views
from .views import RatingViewSets
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r'publisher', views.PublisherViewSet)
router.register(r'genre', views.GenreViewSet)
router.register('rating', RatingViewSets)
router.register(r'user', views.UsersViewSet)
router.register(r'wishlist', views.WishlistViewSet)

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
    path('wishlist/<str:user>', views.getWishlistByUser),
    path('api/', include(router.urls)), 
    path('wishlist/<str:user>', views.getAllWishLists),
    path('wishlist/<str:user>/<str:wishlist_name>', views.wishlist),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
