from django.urls import path
from . import views

app_name = 'analysis'
urlpatterns = [
    path('', views.AnalysisPageView.as_view(), name='analysis'),
]
