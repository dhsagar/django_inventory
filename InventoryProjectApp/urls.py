from django.urls import path
from . import views
urlpatterns = [
    path('registration/', views.RegistrationView, name = 'Registration-Page' ),
    path('', views.HomePage, name = 'Home-Page' ),
    path('logout/', views.LogoutView, name = 'Logout-Page' ),
    path('main/', views.MainView, name = 'Main-Page' ),
    #path('homepage/', views.HomePage, name = 'Home-Page' ),
    path('mainpage/', views.MainPage, name = 'Main-Page-New' ),
    path('product_form/', views.productForm, name = 'ProductForm-Page'),
    path('additem/', views.AddItemForm, name = 'AddItemForm'),
    path('edititem/<str:pk>', views.EditItemForm, name = 'EditItemForm'),

]