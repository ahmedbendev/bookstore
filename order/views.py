from django.shortcuts import render, get_object_or_404, redirect
from .models import  Bookorder,Order,Orderdetail
from offre.models import  Offre
from store.models import  Book,Usedbook,Newbook,Genre
from users.models import  Client,Region,Profile
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin , LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from .forms import OrdercheckoutForm

@login_required
def Addtocart(request,pk):
    newbook = Newbook.objects.filter(id = pk).first()
    useroff= request.user
    order=Order.objects.filter(userorder = useroff).exclude(ordered = True).first()
    print(order)
    print(newbook)
    print(useroff)
    if order == None :
        orderbook=Bookorder.objects.create(
                                   userorderbook = useroff,
                                   newbook = newbook,
                                   )
        orderbook.save()
        order=Order.objects.create(
                                    userorder = useroff,
                                  )
        order.save()
        order.bookorders.add(orderbook)
        order.save()
        print(order)
    else:
        orderbookava = order.bookorders.filter(newbook=newbook).first()
        print(orderbookava)
        if orderbookava == None :
            orderbook=Bookorder.objects.create(
                                       userorderbook = useroff,
                                       newbook = newbook,
                                       )
            orderbook.save()
            print("ranifilif")
            order.bookorders.add(orderbook)
            order.save()
            print(order)
        else :
            print("ranifilelse")
            bookqua = orderbookava.newbook.quantity_book
            qua = orderbookava.quantity
            if bookqua > qua :
                quant = orderbookava.quantity + 1
                print(quant)
                orderbookava.quantity = quant
                orderbookava.save()
    return redirect('/newbooks')
# Create your views here.


# start Useroffers  #
@login_required
def Mycarte(request,username):
    useroff = User.objects.filter(username=username).first()
    currentorder = Order.objects.filter(userorder = useroff).exclude(ordered = True).first()
    print(currentorder)
    if currentorder :
        empty = '0'
        context ={
          'empty' : empty,
          'useroff' : useroff,
          'currentorder' : currentorder
                 }
        print(useroff)
        print(currentorder)
        return render(request ,'mycarte.html',context)
    else:
        empty = '1'
        context ={
          'empty' : empty,
          'useroff' : useroff,
                 }
        print(useroff)
        return render(request ,'mycarte.html',context)
# end Useroffers  #

# start Useroffers  #
@login_required
def Myorders(request,username):
    useroff = User.objects.filter(username=username).first()
    endorders = Order.objects.filter(userorder = useroff).exclude(ordered = False)
    context ={
          'useroff' : useroff,
          'endorders' : endorders
        }
    print(useroff)
    print(endorders)
    return render(request ,'myorders.html',context)
# end Useroffers  #


@login_required
def Addquantity(request,pk):
    useroff= request.user.username
    print(useroff)
    bookorder = Bookorder.objects.filter(pk = pk).first()
    print(bookorder)
    bookqua = bookorder.newbook.quantity_book
    qua = bookorder.quantity
    if bookqua > qua :
        quant = bookorder.quantity + 1
        print(quant)
        bookorder.quantity = quant
        bookorder.save()
    return redirect(Mycarte,username=useroff)

@login_required
def Removequantity(request,pk):
    useroff= request.user.username
    print(useroff)
    bookorder = Bookorder.objects.filter(pk = pk).first()
    print(bookorder)
    qua = bookorder.quantity
    if qua > 1 :
        quant = bookorder.quantity - 1
        print(quant)
        bookorder.quantity = quant
        bookorder.save()
    return redirect(Mycarte,username=useroff)

@login_required
def Removebookorder(request,pk):
    useroff= request.user.username
    print(useroff)
    bookorder = Bookorder.objects.filter(pk = pk).first()
    bookorder.delete()
    return redirect(Mycarte,username=useroff)

@login_required
def Checkout(request,pk):
    useroff= request.user.username
    print(useroff)
    order = Order.objects.filter(pk = pk).first()
    form= OrdercheckoutForm()
    if request.method=='POST':
        form= OrdercheckoutForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            region_adress = form.cleaned_data.get('region_adress')
            town_adress = form.cleaned_data.get('town_adress')
            city_adress = form.cleaned_data.get('city_adress')
            street_adress = form.cleaned_data.get('street_adress')
            postal_code = form.cleaned_data.get('postal_code')
            phone_num = form.cleaned_data.get('phone_num')
            email = form.cleaned_data.get('email')
            shipping_type = form.cleaned_data.get('shipping_type')
            paying_type = form.cleaned_data.get('paying_type')
            orderdetail=Orderdetail.objects.create(
                                  first_name = first_name,
                                  last_name = last_name,
                                  region_adress = region_adress,
                                  town_adress = town_adress,
                                  city_adress = city_adress,
                                  street_adress = street_adress,
                                  postal_code = postal_code,
                                  phone_num = phone_num,
                                  email = email,
                                  shipping_type = shipping_type,
                                  paying_type = paying_type,
                                  order = order,
                                  )
            orderdetail.save()
            order.ordered = True
            order.save()
            return redirect(Myorders,username=useroff)
    else:
        form = OrdercheckoutForm()
    return render(request, 'checkout.html',{"form":form,"order":order})
