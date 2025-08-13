from django.shortcuts import render,redirect, get_object_or_404
from django.http import*
from .models import *
from decimal import Decimal
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request,("home.html"))

def productreg(request):
    cat=Category.objects.all()
    return render(request,"productreg.html",{"category":cat})

def product_process(request):
    if request.method =="POST":
        pname = request.POST.get("pname")
        pdes = request.POST.get("pdes")
        pprice = request.POST.get("pprice")
        category_id = request.POST.get("category")
        productimage = request.FILES.get("productimage")
    
        print(pname,"",pdes,"",pprice,"",category_id,productimage,"")

        #ORM
        category = Category.objects.get(category_id=category_id)
        print(category)

        Product.objects.create(product_name=pname,product_description=pdes,product_price=pprice,category_id_id=category_id,image=productimage)
        context={"pname":pname,"pdes":pdes,"pprice":pprice,"category_id":category_id,"productimage":productimage}
        return render(request,"productprocess.html",context)

def product_all(request):
        product=Product.objects.all()
        print(product)
        return render(request,"productall.html",{"product":product})

def category_reg(request):
     return render(request,"categoryreg.html")

def catprocess(request):
     category_id=request.POST.get("category_id")
     category_name=request.POST.get("category_name")
     print(category_id,"",category_name,"")


     #ORM
     Category.objects.create(category_id=category_id,category_name=category_name)
     context={"category_name":category_name}
     return render(request,"catprocees.html",context)



def category_all(request):
     category=Category.objects.all()
     return render(request,"categoryall.html",{"category":category})

@login_required
def customer_reg(request):
     return render(request,"customerreg.html")

@login_required
def customer_process(request):
     customer_id=request.POST.get("cusid")
     customer_name=request.POST.get("cusname")
     username=request.POST.get("uname")
     customer_city=request.POST.get("cuscity")
     customer_email=request.POST.get("cusemail")
     customer_password=request.POST.get("cuspwd")
     customer_address=request.POST.get("cusaddress")
     user1=User.objects.create_user(username=username,email=customer_email,password=customer_password)
     print(customer_name,"",customer_city,"",customer_email,"",customer_password,"",customer_address,"")

     #ORM
     Customer.objects.create(user=user1,customer_id=customer_id,customer_name=customer_name,username=username,customer_city=customer_city,customer_email=customer_email,customer_password=customer_password,customer_address=customer_address)
     group = Group.objects.get(name="Customers")
     user1.groups.add(group)

     context={"customer_name":customer_name,"username":username,"customer_city":customer_city,"customer_email":customer_email,"customer_password":customer_password,"customer_address":customer_address}
     return render(request,"customerprocess.html",context)

@login_required
def customer_all(request):
     customer=Customer.objects.all()
     return render(request,"customerall.html",{"customer":customer})

def details(request):
     if request.method=="GET":
          category=Category.objects.all()
          return render(request,"detail.html",{"category":category})
     
     elif request.method=="POST":
          category=request.POST.get("category")
          cat=Category.objects.get(category_id=category)
          prod=Product.objects.filter(category_id=cat)
          category=Category.objects.all()
          return render(request,"detail.html",{"prod":prod,"category":category,"cat":cat})
          
def one_record(request):
     product_id=request.GET.get("product_id")
     product=get_object_or_404(Product,product_id=product_id)
     return render(request,"onerecord.html",{"Product":product})

def one_process(request):
     if request.method == "POST":
          category_id=request.POST.get("category_id")
          product_id=request.POST.get("product_id")
          pname = request.POST.get("pname")
          pprice = float(request.POST.get('pprice',))
          quantity = int(request.POST.get('quantity',))
          total_price = quantity * pprice
          request.session['category_id']=category_id
          item={"product_name": pname,"category_id": category_id,"product_price": pprice,"quantity": quantity,"total_price": total_price,}
          cart = request.session.get('cart',[])
          cart += [item]
          request.session['cart'] =cart
          print(pname,quantity,pprice,total_price)

          product = get_object_or_404(Product,product_id=product_id)
        

          context = {"product": product,"product_name": pname,"category_id": category_id,"product_price": pprice,"quantity": quantity,"total_price": total_price,}
          return render(request,"oneprocess.html",context)

def select_product(request):
     if request.method == 'POST':
          cname=request.session.get('category_id')
          cart=request.session.get('cart')
          print("cart",cart)
          return render(request,'detail.html',{"cname":cname,"cart":cart})
     else:
          cname=request.session.get('category_id')
          return render(request,'oneprocess.html',{"cname":cname})
     
def select_all(request):
     if request.method =="POST":
          request.session.clear()
          return render(request,"detail.html")
     else:
          cname=request.session.get('category_id')
          cart=request.session.get('cart',[])
          return render(request,'productshow.html',{"cname":cname,"cart":cart})

def vendor_reg(request):
      return render(request,"vendoreg.html")

def vendor_process(request):
     vendor_id=request.POST.get("venid")
     vendor_name=request.POST.get("venname")
     username=request.POST.get("uname")
     vendor_email=request.POST.get("venemail")
     vendor_city=request.POST.get("vencity")
     vendor_password=request.POST.get("venpwd")
     vendor_address=request.POST.get("venaddress")
     user1=User.objects.create_user(username=username,email=vendor_email,password=vendor_password)
     print(vendor_name,"",vendor_city,"",vendor_email,"",vendor_password,"",vendor_address,"")
    
     #ORM
     Vendor.objects.create(user=user1,vendor_id=vendor_id,vendor_name=vendor_name,username=username,vendor_city=vendor_city,vendor_email=vendor_email,vendor_password=vendor_password,vendor_address=vendor_address)
     group = Group.objects.get(name="Vendors")
     user1.groups.add(group)

     context={"vendor_name":vendor_name,"username":username,"vendor_city":vendor_city,"vendor_email":vendor_email,"vendor_password":vendor_password,"vendor_address":vendor_address}
     return render(request,"vendorprocess.html",context)

def login(request):
    if request.method == "POST":
        username = request.POST.get('uname')
        password = request.POST.get('password')
        print("Username ###############", username, "Password", password)
 
        user = authenticate(request,username=username,password=password)
        print("Authenticated user:", user)
        
        if user:
            print(" Hello ! ", user)
           

        if user is not None:
            auth_login(request, user)
            print(" User ", user)
            if user.groups.filter(name='Customers').exists():
              role='Customers'
            elif user.groups.filter(name='Vendors').exists():
              role='Vendors'
            else:
               role='unknown'
            print("Username ", user , " Role : " , role )

            request.session["role"] = role
            request.session["user"] = user.username

            if role == "Customers":
                return redirect("customerhome")
            elif role == "Vendors":
                return redirect("vendorhome")

        else:
         context = {"error": "Invalid username or password"}
         return render(request, "login.html", context)      
    return render(request, "login.html",)

@login_required
def customer_home(request):
    username = request.session.get("user")
    customer=Customer.objects.get(user__username=username)

    show = False
    if request.method == "POST":
        action = request.POST.get("action")
       
        if action == "Me":
            show = True
        
    context = {"customer": customer,"show": show } 
    return render(request, "customerdashboard.html", context)