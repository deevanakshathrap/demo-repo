from django.urls import path
from .import views

urlpatterns = [
    path("home",views.home,name="home"),
    path("product_register",views.productreg,name="product_register"),
    path("product_process",views.product_process,name="product_process"),
    path("productdetails",views.product_all,name="productdetails"),
    path("catreg",views.category_reg,name="catreg"),
    path("catprocess",views.catprocess,name="catprocess"),
    path("catdetails",views.category_all,name="catdetails"),
    path("custreg",views.customer_reg,name="custreg"),
    path("custprocess",views.customer_process,name="custprocess"),
    path("custall",views.customer_all,name="custall"),
    path("details",views.details,name="details"),
    path("onerecord",views.one_record,name="onerecord"),
    path("oneprocess", views.one_process, name="oneprocess"),
    path("selectproduct", views.select_product, name="selectproduct"),
    path("totalproduct", views.select_all, name="totalproduct"),
    path("venreg",views.vendor_reg,name="venreg"),
    path("venprocess",views.vendor_process,name="venprocess"),
    path("login",views.login,name="login"),
    path("customerhome",views.customer_home,name="customerhome"),

     

     

 

]
