from django.shortcuts import render, get_object_or_404, redirect
from .models import  Offre
from store.models import  Book,Usedbook,Newbook,Genre
from users.models import  Client,Region,Profile
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin , LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User

# start Createoffer  #
@login_required
def Createoffer(request,pk):
    usedbook = Usedbook.objects.filter(id = pk).first()
    book= usedbook.book
    username= request.user
    user = User.objects.filter(username=username).first()
    userusedbooks = Usedbook.objects.filter(user_usedbook=user)

    if request.method == 'POST':
        userdemandeur = user
        useroffreur = usedbook.user_usedbook
        usedbookoffer = usedbook
        usedbookdemand = request.POST.get('usedbookdemandeur')
        bookk= Book.objects.filter(title_book=usedbookdemand).first()
        usedbookdemandeur= Usedbook.objects.filter(book=bookk).first()
        content = request.POST.get('message')
        offre=Offre.objects.create(
                              userdemandeur = userdemandeur,
                              useroffreur = useroffreur,
                              usedbookoffer = usedbookoffer,
                              usedbookdemandeur = usedbookdemandeur,
                              content = content
                              )
        offre.save()
        print(userdemandeur)
        print(useroffreur)
        print(usedbookoffer)
        print(usedbookdemandeur)
        print(content)
        print(offre)
        return redirect(offre)

    return render(request, 'create_offer.html',{"usedbook":usedbook,"userusedbooks":userusedbooks})
# end Createoffer  #

# start Offredetail  #
def Offredetail(request,pk):
    offre = Offre.objects.filter(id = pk).first()
    return render(request ,'offre_detail.html',{"offre":offre})
# end Offredetail  #

# start Useroffers  #
def Useroffers(request,username):
    user = User.objects.filter(username=username).first()
    userdemandeuroffers = Offre.objects.filter(userdemandeur=user)
    useroffreuroffers = Offre.objects.filter(useroffreur=user)
    context ={
          'user' : user,
          'userdemandeuroffers' : userdemandeuroffers,
          'useroffreuroffers' : useroffreuroffers
        }
    print(user)
    print(userdemandeuroffers)
    print(useroffreuroffers)
    return render(request ,'useroffers.html',context)
# end Useroffers  #

# start Deleteusedbook  #
@login_required
def Deleteoffre(request,pk):
    offre = Offre.objects.filter(id = pk).first()
    useroff= request.user.username
    print(useroff)
    print(offre)
    if request.method=='POST':
        offre.delete()
        return redirect(Useroffers,username=useroff)
    return render(request, 'offre_delete.html',{"offre":offre,"useroff":useroff})
# end Deleteusedbook  #

@login_required
def Aproveoffer(request,id):
    offre = Offre.objects.filter(id = id).first()
    useroff = request.user.username
    if request.method == 'POST' :
        offre.aprove()
        return redirect(Useroffers,username=useroff)
    return render(request, 'offre_aproved.html',{"offre":offre,"useroff":useroff})

@login_required
def Refuseoffer(request,id):
    offre = Offre.objects.filter(id = id).first()
    useroff = request.user.username
    if request.method == 'POST' :
        offre.refuse()
        return redirect(Useroffers,username=useroff)
    return render(request, 'offre_refuse.html',{"offre":offre,"useroff":useroff})

@login_required
def Contactoffer(request,id):
    offre = Offre.objects.filter(id = id).first()
    useroff = request.user.username
    userdemandeur=offre.userdemandeur
    useroffreur=offre.useroffreur
    print(offre)
    print(useroff)
    print(userdemandeur)
    print(useroffreur)
    if request.user.username == offre.userdemandeur.username:
        userinfo=offre.useroffreur
        print(userinfo)
    elif request.user.username == offre.useroffreur.username:
         userinfo=offre.userdemandeur
         print(userinfo)
    else:
        print("123")
    context={
        "offre":offre,
        "useroff":useroff,
        "userinfo":userinfo,
    }
    return render(request, 'offre_contact.html',context)

@login_required
def Doneoffer(request,id):
    offre = Offre.objects.filter(id = id).first()
    useroff = request.user.username
    if request.method == 'POST' :
        offre.usedbookoffer.etat_book = "not available"
        offre.usedbookdemandeur.etat_book = "not available"
        offre.usedbookoffer.save()
        offre.usedbookdemandeur.save()
        offre.done()
        return redirect(Useroffers,username=useroff)
    return render(request, 'offre_done.html',{"offre":offre,"useroff":useroff})
