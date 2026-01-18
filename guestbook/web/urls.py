from django.urls import path
from . import views

app_name='web'

urlpatterns = [
    path('', views.MessageList.as_view(), name='message_list'),
    path('create/', views.MessageCreate.as_view()),  
    path('<int:pk>', views.MessageDetail.as_view()),
    path('<int:pk>/delete/', views.MessageDelete.as_view()),   
]