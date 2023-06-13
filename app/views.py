from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from email import message
from pyexpat.errors import messages
from django.contrib import messages
from django.core.paginator import Paginator
from app.models import Inventory,Customer,Staff,Product,POS, delivery
from  django.contrib.auth import authenticate,login,logout
from  django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login as authlogin
import csv
import pandas as pd
from numpy import genfromtxt
from django.http import JsonResponse
# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST.get('username','')
        password =request.POST.get('password','')

        userr = authenticate(request, username=username, password=password)

        if userr is not None:
            authlogin(request, userr)
            messages.success(request, 'Username OR password is validated.')
            return redirect('Dashboard')
        else:
            messages.info(request, 'Username OR password is incorrect.')
    return render(request,'login.html')
    
def signup(request):
     if request.method=="POST":
      username=request.POST.get('username')
      passw=request.POST.get('password')
      confirmpassword=request.POST.get('cpassword')
      myuser=User.objects.create(username=username, password = make_password(passw))
    #   save=myuser.save()
      if myuser:
       messages.success(request,"You are SignUp")
      else:
       messages.error(request,"Invalid Creditial")
     return render(request,'signup.html')
def signout(request):
    logout(request)
    messages.success(request,"Successfully Logged Out")
    return redirect('login')

def inventory(request):
    if request.method == "POST":
        inventoryname=request.POST.get('invname','')
        category=request.POST.get('cat','')
        subcategory=request.POST.get('subcat','')
        desc=request.POST.get('desc','')
        sellingprice=request.POST.get('sp','')
        costprice=request.POST.get('cp','')
        quantity=request.POST.get('quantity','')
        inventoryy=Inventory(inventoryname=inventoryname,category=category,subcategory=subcategory,desc=desc,sellingprice=sellingprice,costprice=costprice,quantity=quantity)
        save=inventoryy.save()
        if inventoryy.save()==save:
            messages.success(request,"Your inventory Data are Enter in the Database")
        else:
          messages.error(request,"Your inventory Data Does Not Enter in the Database ") 

    return render(request,'Inventory.html')   

def InventoryData(request):
    data=Inventory.objects.all()
    paginator=Paginator(data,4)
    page_number =request.GET.get('page')
    page_obj =paginator.get_page(page_number)
    context={ 
        "view":data,
        "page_obj":page_obj
        
        }
    return render(request, 'inventorydata.html',context)


def updateinventory(request,id):
     inc=Inventory.objects.get(pk=id)
     data=Inventory.objects.all()


     context={
        'inc':inc,
        'view':data
     }
     return render(request,'updateinventory.html',context)  

def edit_inventory(request,id):
    inc=Inventory.objects.get(pk=id)
    inc.inventoryname=request.POST['invname']
    inc.category=request.POST['cat']
    inc.subcategory=request.POST['subcat']
    inc.quantity=request.POST['quantity']
    inc.desc=request.POST['desc']
    inc.costprice=request.POST['cp']
    inc.sellingprice=request.POST['sp']
    
    
    inc.save()
    return redirect(InventoryData)    

def inventoryComponent(request):

    return render(request,'inventoryComponent.html')            
def Report(request):

    return render(request,'Report.html')

def drive(request):
   
    return render(request,'drive.html')

def dashboard(request):
    pos=POS.objects.values('product', 'sellingprice','id','customername')
    inven=Inventory.objects.values('id')
    deliver=delivery.objects.values('id','staffname')
    data =[item['id'] for item in pos]
    idata =[item['id'] for item in inven]
    deliverydata =[item['id'] for item in deliver]
    # Prepare the data for the chart
    labels = [item['customername'] for item in pos]
    chart_data = [item['sellingprice'] for item in pos]
    context={ 
         "data" :data,
         "idata" :idata,
         "deliverydata" :deliverydata,
         'chart_labels': labels,
         'chart_data': chart_data,
        }
       
    return render(request,'Dashboard.html' ,context)   
def data(request):

    return render(request,'data.html')  

def deliveryProduct(request):
    if request.method == "POST":
        staffname=request.POST.get('staffname','')
        product=request.POST.get('product','')
        desc=request.POST.get('desc','')
        quantity=request.POST.get('quantity','')
        price=request.POST.get('price','')
        address=request.POST.get('address','')
        phone=request.POST.get('phone','')
        Delivery=delivery(staffname=staffname,product=product,address=address,desc=desc,price=price,phone=phone,quantity=quantity)
        save=Delivery.save()
        if Delivery.save()==save:
            messages.success(request,"Your inventory Data are Enter in the Database")
        else:
          messages.error(request,"Your inventory Data Does Not Enter in the Database ") 
    return render(request,'deliveryProduct.html')  
def deliveryProductdata(request):
    data=delivery.objects.all()
    paginator=Paginator(data,4)
    page_number =request.GET.get('page')
    page_obj =paginator.get_page(page_number)
    context={ 
        "view":data,
        "page_obj":page_obj
        
        }
    return render(request, 'deliveryProductdata.html',context)  

def product(request):
    if request.method == "POST":
        productname=request.POST.get('pname')
        category=request.POST.get('cat','')
        subcategory=request.POST.get('subcat','')
        desc=request.POST.get('desc','')
        productcode=request.POST.get('pcode','')
        product=Product(productname=productname,category=category,subcategory=subcategory,desc=desc,productcode=productcode)
        save=product.save()
        if product.save()==save:
            messages.success(request,"Your product Data are Enter in the Database")
        else:
          messages.error(request,"Your product Data Does Not Enter in the Database ") 
    return render(request,'Product.html')     

def productdata(request):
    data=Product.objects.all()
    paginator=Paginator(data,4)
    page_number =request.GET.get('page')
    page_obj =paginator.get_page(page_number)
    context={ 
        "view":data,
        "page_obj":page_obj
        
        }
    return render(request, 'productdata.html',context)    


def updateproduct(request,id):
     inc=Product.objects.get(pk=id)
     data=Product.objects.all()


     context={
        'inc':inc,
        'view':data
     }
     return render(request,'updateproduct.html',context)  

def edit_product(request,id):
    inc=Product.objects.get(pk=id)
    inc.productname=request.POST['pname']
    inc.category=request.POST['cat']
    inc.subcategory=request.POST['subcat']
    inc.productcode=request.POST['pcode']
    inc.desc=request.POST['desc']
    
    
    inc.save()
    return redirect(productdata)




def staff(request):
 if request.method == "POST":
    staffname=request.POST.get('staffname','')
    phone=request.POST.get('phone','')
    address=request.POST.get('add','')
    salary=request.POST.get('salary','')
    time=request.POST.get('time','')
    staff=Staff(staffname=staffname,phone=phone,address=address,salary=salary,time=time)
    save=staff.save()
    if staff.save()==save:
            messages.success(request,"Your staff Data are Enter in the Database")
    else:
          messages.error(request,"Your staff Data Does Not Enter in the Database ") 

 return render(request,'Staff.html') 

def staffdata(request):
    data=Staff.objects.all()
    paginator=Paginator(data,4)
    page_number =request.GET.get('page')
    page_obj =paginator.get_page(page_number)
    context={ 
        "view":data,
        "page_obj":page_obj
        
        }
    return render(request, 'staffdata.html',context)   
def updatestaff(request,id):
     inc=Staff.objects.get(pk=id)
     data=Staff.objects.all()


     context={
        'inc':inc,
        'view':data
     }
     return render(request,'updatestaff.html',context)  

def edit_staff(request,id):
    inc=Staff.objects.get(pk=id)
    inc.staffname=request.POST['staffname']
    inc.address=request.POST['add']
    inc.time=request.POST['time']
    inc.phone=request.POST['phone']
    inc.salary=request.POST['salary']
    
    
    inc.save()
    return redirect(staffdata)


def customer(request):
   if request.method == "POST":
     customername=request.POST.get('customername','')
     address=request.POST.get('add','')
     product=request.POST.get('product','')
     phone=request.POST.get('phone','')
     desc=request.POST.get('desc','')
     customers=Customer(customername=customername,address=address,product=product,phone=phone,desc=desc)
     save=customers.save()
     if customers.save()==save:
            messages.success(request,"Your customer Data are Enter in the Database")
     else:
          messages.error(request,"Your customer Data Does Not Enter in the Database ") 
   return render(request,'Customers.html')  

def customerdata(request):
    data=Customer.objects.all()
    customer=Customer.objects.all()
    paginator=Paginator(data,4)
    page_number =request.GET.get('page')
    page_obj =paginator.get_page(page_number)
    context={ 
        "view":data,
        "page_obj":page_obj
        
        }
    return render(request, 'customerdata.html',context)  

def updatecustomer(request,id):
     inc=Customer.objects.get(pk=id)
     data=Customer.objects.all()


     context={
        'inc':inc,
        'view':data
     }
     return render(request,'updatecustomer.html',context)  

def edit_customer(request,id):
    inc=Customer.objects.get(pk=id)
    inc.customername=request.POST['customername']
    inc.address=request.POST['add']
    inc.phone=request.POST['phone']
    inc.product=request.POST['product']
    inc.desc=request.POST['desc']
    
    
    inc.save()
    return redirect(customerdata)



def pos(request):
    if request.method == "POST":
     customername=request.POST.get('cname','')
     address=request.POST.get('add','')
     product=request.POST.get('product','')
     phone=request.POST.get('phone','')
     desc=request.POST.get('desc','')
     sellingprice=request.POST.get('sp','')
     date=request.POST.get('date','')
     time=request.POST.get('time','')
     quantity=request.POST.get('qt','')
     pos=POS(customername=customername,address=address,product=product,phone=phone,desc=desc,sellingprice=sellingprice,date=date,
     time=time,quantity=quantity)
     save=pos.save()
     if pos.save()==save:
            messages.success(request,"Your pos Data are Enter in the Database")
     else:
          messages.error(request,"Your pos Data Does Not Enter in the Database ") 
    return render(request,'postofsale.html') 

def posdata(request):
    data=POS.objects.all()
    paginator=Paginator(data,4)
    page_number =request.GET.get('page')
    page_obj =paginator.get_page(page_number)
    context={ 
        "view":data,
        "page_obj":page_obj
        
        }
    return render(request, 'posdata.html',context)      
def updatepos(request,id):
     inc=POS.objects.get(pk=id)
     data=POS.objects.all()


     context={
        'inc':inc,
        'view':data
     }
     return render(request,'updatepos.html',context)  

def edit_pos(request,id):
    inc=POS.objects.get(pk=id)
    inc.customername=request.POST['cname']
    inc.address=request.POST['add']
    inc.product=request.POST['product']
    inc.quantity=request.POST['qt']
    inc.date=request.POST['date']
    inc.time=request.POST['time']
    inc.phone=request.POST['phone']
    inc.sellingprice=request.POST['sp']
    inc.desc=request.POST['desc']
    
    inc.save()
    return redirect(posdata)    

# inventories CSV file
def data_csv(request):
    inc = Inventory.objects.all()
    
    # Convert the queryset to a list of dictionaries
    
    data = [{'InventoryName': item.InventoryName, 'Category': item.Category, 'SubCategory': item.SubCategory,'Quantity': item.Quantity, 'Description': item.Description, 'CostPrice': item.CostPrice,'SellingPrice': item.SellingPrice} for item in inc]

    # Create a DataFrame from the data
    df = pd.DataFrame(data)

    # Define the filename and content type
    filename = 'inventory.csv'
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    # Write the DataFrame to the response as a CSV file
    df.to_csv(response, index=False)

    return response   


# inventories CSV file
def data_csv_product(request):
    inc = Inventory.objects.all()
    context={
     'data':inc
      }
    # Convert the queryset to a list of dictionaries
    

    # Create a DataFrame from the data
    df = pd.DataFrame(context)

    # Define the filename and content type
    filename = 'inventory.csv'
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    # Write the DataFrame to the response as a CSV file
    df.to_csv(response, index=False)

    return response   


def search_view(request):
    search = request.GET.get('query', '')
    inc = Product.objects.none()
    sup = POS.objects.none()
    expen = delivery.objects.none()
    staf = Staff.objects.none()
    inv = Inventory.objects.none()
    customer = Customer.objects.none()

    if search:
        if len(search) > 10:
            messages.warning(request, "No Search Result are Found.")
        else:
            inc = Product.objects.filter(productname__icontains=search)
            sup = POS.objects.filter(customername__icontains=search)  
            expen = delivery.objects.filter(product__icontains=search)  
            staf = Staff.objects.filter(staffname__icontains=search)  
            inv = Inventory.objects.filter(inventoryname__icontains=search)  
            customer = Customer.objects.filter(customername__icontains=search)  
            messages.info(request, "Search Result are Found.") 
    else:
        messages.warning(request, "No Search Result are Found.") 

    params = {
        'data': inc,
        'search': search,
        'expen': expen,
        'staf': staf,
        'inv': inv,
        'sup': sup,
        'customer': customer
    }

    return render(request, 'searchdata.html', params)