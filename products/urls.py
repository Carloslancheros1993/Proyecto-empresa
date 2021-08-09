from django.urls import path

from products.views import ProductGenericView, ProductDetailGenericView

app_name = 'products'
urlpatterns = [
    path('', ProductGenericView.as_view()),
    path('<pk>/', ProductDetailGenericView.as_view())
    ]