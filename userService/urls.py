from django.urls import path, include
from .views import userViews, authViews

urlpatterns2 = [
    path('', userViews.ConfidentialUserView.as_view(), name='user-detail'),
    path('', include('buyingService.urls'), name="buyingService"),
    path('sign/', authViews.SignUserView.as_view(), name='sign'),
    path('registration/', authViews.CreateUserView.as_view(), name='registration'),
    path('authenticate/', authViews.CheckTokenView.as_view(), name='authenticate'),
    path('update/', authViews.UpdateUserView.as_view(), name='update'),
]

urlpatterns = [
    path('<int:id_user>/', userViews.UserView.as_view()),
    path('<str:user>/planets/', include('planetService.urls')),
    path('me/', include(urlpatterns2), name='user-detail'),
]