from django.urls import path, include
from django.http import JsonResponse
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'teams', views.TeamViewSet)
router.register(r'activities', views.ActivityViewSet)
router.register(r'workouts', views.WorkoutViewSet)
router.register(r'leaderboard', views.LeaderboardViewSet)

def api_url_list(request):
    base = '/api/'
    return JsonResponse({
        'users': base + 'users/',
        'teams': base + 'teams/',
        'activities': base + 'activities/',
        'workouts': base + 'workouts/',
        'leaderboard': base + 'leaderboard/',
    })

urlpatterns = [
    path('', views.api_root, name='api-root'),
    path('get', api_url_list, name='api-url-list'),
    path('api/', include(router.urls)),
]
