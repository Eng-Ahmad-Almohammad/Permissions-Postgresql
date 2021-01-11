from django.urls import path , include

from .views import DataView, DetailsView

urlpatterns = [
    path('', DataView.as_view(), name = 'data'),
    path('<int:pk>/',DetailsView.as_view(), name = 'details')
]