from django.urls import path

from clients.views import ClientGenericView, ClientDetailGenericView

app_name = 'clients'
urlpatterns = [
    path('', ClientGenericView.as_view()),
    path('<pk>/', ClientDetailGenericView.as_view())
]
