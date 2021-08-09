from django.urls import path

from billsProducts.views import BillProductGenericView, BillProductDetailGenericView

app_name = 'billsProducts'
urlpatterns = [
    path('', BillProductGenericView.as_view()),
    path('<pk>/', BillProductDetailGenericView.as_view())
]
