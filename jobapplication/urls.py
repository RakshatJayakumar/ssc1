from django.urls import path
from .views import ApplicationList,ApplicationDetail,ApplicationCreate, ApplicationUpdate, ApplicationDelete, CustomLoginView,RegisterPage, random_fact_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/',RegisterPage.as_view(), name='register'),
    path('', ApplicationList.as_view(), name='applications'),
    path('application/<int:pk>/',ApplicationDetail.as_view(), name='application'),
    path('application-create', ApplicationCreate.as_view(), name='application-create'),
    path('application-update/<int:pk>/', ApplicationUpdate.as_view(), name='application-update'),
    path('application-delete/<int:pk>/', ApplicationDelete.as_view(), name='application-delete'),
    path('random-fact/', random_fact_view, name='random_fact'),
]
