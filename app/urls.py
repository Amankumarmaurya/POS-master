from django.contrib import admin
from django.urls import path,include

# from app.models import income
from . import views
urlpatterns = [
    path('inventory/',views.inventory, name="inventory" ),
    path('inventoryData/',views.InventoryData, name="inventoryData" ),
    path('updateinventory/<int:id>',views.updateinventory, name="updateinventory" ), 
    path('edit_inventory/<int:id>',views.edit_inventory, name="edit_inventory" ),
    path('',views.login, name="login" ),
    path('Report/',views.Report, name="Report" ),
    path('drive/',views.drive, name="drive" ),
    path('signup/',views.signup, name="signup" ),
    path('signout/',views.signout, name="signout" ),
    path('product/',views.product, name="product" ),
    path('productdata/',views.productdata, name="productdata" ),
    path('updateproduct/<int:id>',views.updateproduct, name="updateproduct" ), 
    path('edit_product/<int:id>',views.edit_product, name="edit_product" ),
    path('staff/',views.staff, name="staff" ),
    path('staffdata/',views.staffdata, name="staffdata" ),
    path('updatestaff/<int:id>',views.updatestaff, name="updatestaff" ), 
    path('edit_staff/<int:id>',views.edit_staff, name="edit_staff" ),
    path('Dashboard/',views.dashboard, name="Dashboard" ),
    path('customer/',views.customer, name="customer" ),
    path('customerdata/',views.customerdata, name="customerdata" ),
    path('updatecustomer/<int:id>',views.updatecustomer, name="updatecustomer" ), 
    path('edit_customer/<int:id>',views.edit_customer, name="edit_customer" ),
    path('inventoryComponent/',views.inventoryComponent, name="inventoryComponent" ),
    path('pos/',views.pos, name="pos" ),
    path('posdata/',views.posdata, name="posdata" ),
    path('updatepos/<int:id>',views.updatepos, name="updatepos" ), 
    path('edit_pos/<int:id>',views.edit_pos, name="edit_pos" ),
    path('data/',views.data, name="data" ),
    path('deliveryProduct/',views.deliveryProduct, name="deliveryProduct" ),
    path('deliveryProductdata/',views.deliveryProductdata, name="deliveryProductdata" ),
     path('datacsv',views.data_csv, name="datacsv" ),
     path('searchdata/', views.search_view, name='searchdata'),
]