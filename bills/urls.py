from django.urls import path

from bills.views import BillGenericView, BillDetailGenericView

app_name = 'bills'
urlpatterns = [
    path('', BillGenericView.as_view()),
    path('<pk>/', BillDetailGenericView.as_view())
]
