from django.urls import path
from catalog import views
from catalog.apps import CatalogConfig
from catalog.views import ProductDetailView, CategoryCreateView, ProductCreateView, \
    CatalogTemplateView, ProductUpdateView, ProductListView, ProductDeleteView, toggle_active

# from catalog.views import CatalogView, ContactsView, ProductView, CategoryCreateView, ProductCreateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('create_product/', ProductCreateView.as_view(), name='create_product'),
    path('view/<int:pk>', ProductDetailView.as_view(), name='view_product'),
    path('update/<int:pk>', ProductUpdateView.as_view(), name='update_product'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete_product'),
    path('activity/<int:pk>', toggle_active, name='toggle_active'),
]

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('contacts/', views.contacts, name='contacts'),
#     path('product/<int:pk>', views.product, name='product'),
#     path('create_category/', views.create_category, name='create_category'),
#     path('create_product/', views.create_product, name='create_product'),
# ]