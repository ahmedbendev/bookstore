from django.shortcuts import render, get_object_or_404, redirect
from .models import  Book,Usedbook,Newbook,Genre,Wishlist
from users.models import  Client,Region,Profile
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin , LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from .forms import AdvancedserchForm,CreateusedbookForm,BookUpdateForm,UsedbookUpdateForm,WishlistForm,ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
# start Latestbookshome #
class LatestbookshomeListView(ListView):
      model = Book
      context_object_name = "books"
      paginate_by = 8
      template_name = 'store/home.html'
      def get_queryset(self):
          books = Book.objects.all()
          return books
# end Latestbookshome #

# start Allnewbooks #
class NewbookshomeListView(ListView):
      model = Newbook
      context_object_name = "newbooks"
      paginate_by = 8
      template_name = 'store/newbooks.html'
      def get_queryset(self):
          newbooks = Newbook.objects.all()
          return newbooks
# end Allnewbooks #

# start Allusedbooks #
class UsedbookshomeListView(ListView):
      model = Usedbook
      context_object_name = "usedbooks"
      paginate_by = 8
      template_name = 'store/usedbooks.html'
      def get_queryset(self):
          usedbooks = Usedbook.objects.all()
          return usedbooks
# end Allusedbooks #

# start categoriesbookshome #
def choose_categories_home(request):
    genres = Genre.objects.all()
    return render(request ,'store/choosecategories.html',{"genres":genres})

def categories_books(request,pk):
    books = Book.objects.filter(genre_book = pk)
    genre = Genre.objects.filter(pk = pk).first()
    return render(request ,'store/genre_detail.html',{"books":books ,"genre":genre})

# end categoriesbookshome #

# start Langaguesbookshome #
class LangaguesengbookhomeListView(ListView):
    model = Book
    context_object_name = "books"
    paginate_by = 8
    template_name = 'store/languageshome/langaguesengbooks.html'
    def get_queryset(self):
        books = Book.objects.filter(langague_book='English')
        return books
class LangaguesarbbookhomeListView(ListView):
    model = Book
    context_object_name = "books"
    paginate_by = 8
    template_name = 'store/languageshome/langaguesarbbooks.html'
    def get_queryset(self):
        books = Book.objects.filter(langague_book='Arabic')
        return books
class LangaguesfrebookhomeListView(ListView):
    model = Book
    context_object_name = "books"
    paginate_by = 8
    template_name = 'store/languageshome/langaguesfrebooks.html'
    def get_queryset(self):
        books = Book.objects.filter(langague_book='Frenche')
        return books
class LangaguesothbookhomeListView(ListView):
    model = Book
    context_object_name = "books"
    paginate_by = 8
    template_name = 'store/languageshome/langaguesothbooks.html'
    def get_queryset(self):
        books = Book.objects.filter(langague_book='Other')
        return books
# end Langaguesbookshome #

# start regionusedbookshome #

def choose_region_home(request):
    regions = Region.objects.all()
    return render(request ,'store/chooseregion.html',{"regions":regions})

def region_books(request,pk):

    region = Region.objects.filter(pk = pk).first()
    client = Client.objects.filter(region_cl__name_region = region)
    profile = Profile.objects.filter(client__in = client )
    user = User.objects.filter(profile__in=profile)
    usedbooks = Usedbook.objects.filter(user_usedbook__in=user)

    return render(request ,'store/region_detail.html',{"usedbooks":usedbooks ,"region":region})

# end Regionusedbookshome #

# start serchhome #
def search_book(request):
    query = request.GET.get('search')
    books = Book.objects.filter(
        Q(title_book__icontains=query) | Q(author_book__icontains=query)
    )
    return render(request ,'store/search_book.html',{"books":books})
# end serchhome #

# start advancedserchhome #
def Advancedsearch_book(request):
    form = AdvancedserchForm()
    return render(request, 'store/advancedsearch_book.html',{'form':form})


def Advancedsearch_bookresult(request):
    if request.method == 'GET':
       form = AdvancedserchForm(request.GET)
       if form.is_valid():
          serch_keyone = form.cleaned_data['serch_keyone']
          serch_keytwo = form.cleaned_data['serch_keytwo']
          serch_keythree = form.cleaned_data['serch_keythree']
          serch_keyfour = form.cleaned_data['serch_keyfour']
          bookchoice = form.cleaned_data['bookchoice']
          booklanguechoice = form.cleaned_data['bookgenrechoice']
          bookgenrechoice = form.cleaned_data['bookgenrechoice']
          title_book = form.cleaned_data['title_book']
          isbn_book = form.cleaned_data['isbn_book']
          user_usedbook = form.cleaned_data['user_usedbook']
          etat_book = form.cleaned_data['etat_book']
          etat_actu_book = form.cleaned_data['etat_actu_book']
          date_postedubookstart = form.cleaned_data['date_postedubookstart']
          date_postedubookend = form.cleaned_data['date_postedubookend']
          etat_actu_book = form.cleaned_data['etat_actu_book']
          date_postednbookstart = form.cleaned_data['date_postednbookstart']
          date_postednbookend = form.cleaned_data['date_postednbookend']
          price_book = form.cleaned_data['price_book']
          stars_book = form.cleaned_data['stars_book']
          books = Book.objects.filter(
                  Q(title_book__icontains=serch_keyone) | Q(author_book__icontains=serch_keytwo)|
                  Q(author_book__icontains=serch_keythree)| Q(author_book__icontains=serch_keyfour)
                   )
          context = {
          "books":books,"serch_keyone":serch_keyone,"serch_keytwo":serch_keytwo,"serch_keythree":serch_keythree,
          "serch_keyfour":serch_keyfour,"bookchoice":bookchoice,"booklanguechoice":booklanguechoice,
          "bookgenrechoice":bookgenrechoice,"title_book":title_book,"isbn_book":isbn_book,"user_usedbook":user_usedbook,
          "etat_book":etat_book,"etat_actu_book":etat_actu_book,"date_postedubookstart":date_postedubookstart,"date_postedubookend":date_postedubookend,
          "etat_actu_book":etat_actu_book,"date_postednbookstart":date_postednbookstart,"date_postednbookend":date_postednbookend,"price_book":price_book,"stars_book":stars_book
          }
          print(books)
          print(context)
          return render(request ,'store/advancedsearch_bookresult.html',context)
    else:
        form = AdvancedserchForm()
    return render(request, 'store/advancedsearch_book.html',{'form':form})
# end advancedserchhome #

# start createusedbook #
@login_required
def createusedbook(request):
    form = CreateusedbookForm()
    if request.method == 'POST':
       form = CreateusedbookForm(request.POST, request.FILES,request.user)
       if form.is_valid():
           title_book = form.cleaned_data['title_book']
           num_page_book = form.cleaned_data['num_page_book']
           author_book = form.cleaned_data['author_book']
           isbn_book = form.cleaned_data['isbn_book']
           image_book = form.cleaned_data['image_book']
           descript_book = form.cleaned_data['descript_book']
           langague_book = form.cleaned_data['langague_book']
           genre_book = form.cleaned_data.get('genre_book')
           etat_actu_book = form.cleaned_data['etat_actu_book']
           book=Book.objects.create(
                                 title_book = title_book,
                                 num_page_book = num_page_book,
                                 author_book = author_book,
                                 isbn_book = isbn_book,
                                 image_book = image_book,
                                 descript_book = descript_book,
                                 langague_book = langague_book,
                                 )
           book.save()
           for x in genre_book:
               genre=Genre.objects.get(name_genre=x)
               book.genre_book.add(genre)

           current_user = request.user
           usedbook=Usedbook.objects.create(
                                 book = book,
                                 user_usedbook = current_user,
                                 etat_actu_book = etat_actu_book,
                                 )

           context = {
           "title_book":title_book,"num_page_book":num_page_book,"author_book":author_book,
           "isbn_book":isbn_book,"image_book":image_book,"descript_book":descript_book,
           "langague_book":langague_book,"genre_book":genre_book,"etat_actu_book":etat_actu_book
           }
           print(usedbook.pk)
           print (current_user.id)
           print (current_user.username)
           print(context)
           print(book)
           print(usedbook)
           print(genre_book)
           print(genre)
           return redirect(usedbook)
    else:
        form = CreateusedbookForm()
    return render(request, 'store/createusedbook.html',{'form':form})
# end createusedbook #
# start  newbook detail #
def Newbookdetail(request,pk):
    newbook = Newbook.objects.filter(id = pk).first()
    book= newbook.book
    genres = book.genre_book.values()
    return render(request ,'store/newbook_detail.html',{"newbook":newbook,"genres":genres})
# end  newbook detail #
# start  usedbook detail #
def Usedbookdetail(request,pk):
    usedbook = Usedbook.objects.filter(id = pk).first()
    book= usedbook.book
    genres = book.genre_book.values()
    return render(request ,'store/usedbook_detail.html',{"usedbook":usedbook,"genres":genres})
# end  usedbook detail #

# start  userusedbooks #
def userusedbooks(request,username):
    user = User.objects.filter(username=username).first()
    usedbooks = Usedbook.objects.filter(user_usedbook=user)
    print(user)
    print(usedbooks)
    return render(request ,'store/userusedbooks.html',{"user":user,"usedbooks":usedbooks})
# end userusedbooks #
# start Updateusedbook  #
@login_required
def Updateusedbook(request,pk):
    usedbook = Usedbook.objects.filter(id = pk).first()
    book= usedbook.book
    print(usedbook)
    print(book)
    b_form= BookUpdateForm(request.POST,request.FILES,instance=book)
    ub_form= UsedbookUpdateForm(request.POST,request.FILES,instance=usedbook)

    if request.method=='POST':
        b_form= BookUpdateForm(request.POST,request.FILES,instance=book)
        ub_form= UsedbookUpdateForm(request.POST,request.FILES,instance=usedbook)
        if b_form.is_valid() and ub_form.is_valid():
            b_form.save()
            ub_form.save()
        return redirect(usedbook)
    else:
        b_form= BookUpdateForm(instance=book)
        ub_form= UsedbookUpdateForm(instance=usedbook)
    context ={
      'b_form' : b_form,
      'ub_form' : ub_form
    }
    return render(request, 'store/usedbook_update.html',context)
# end Updateusedbook #
# start Deleteusedbook  #
@login_required
def Deleteusedbook(request,pk):
    usedbook = Usedbook.objects.filter(id = pk).first()
    book= usedbook.book
    user= request.user.username
    print(user)
    print(usedbook)
    print(book)
    if request.method=='POST':
        book.delete()
        usedbook.delete()
        return redirect(userusedbooks,username=user)
    return render(request, 'store/usedbook_delete.html',{"usedbook":usedbook})
# end Deleteusedbook  #

@login_required
def Wishlistuser(request,username):
    print(username)
    useroff = User.objects.filter(username=username).first()
    wishlists = Wishlist.objects.filter(wishlist_user=useroff)
    print(wishlists)
    return render(request, "store/wishlist.html",{"wishlists":wishlists})

@login_required
def Wishlistremove(request,pk):
    wishlist = Wishlist.objects.filter(id = pk).first()
    user= request.user.username
    if request.method=='POST':
        wishlist.delete()
        return redirect(Wishlistuser,username=user)
    return render(request, 'store/wishlist_delete.html',{"wishlist":wishlist})

@login_required
def Wishlistadd(request):
    username= request.user.username
    useroff= request.user
    form= WishlistForm()
    if request.method=='POST':
        form= WishlistForm(request.POST)
        if form.is_valid():
            wishlist_book = form.cleaned_data.get('wishlist_book')
            wishlist_note = form.cleaned_data.get('wishlist_note')
            wishlist_emailme = form.cleaned_data.get('wishlist_emailme')
            wishlist=Wishlist.objects.create(
                                  wishlist_book = wishlist_book,
                                  wishlist_note = wishlist_note,
                                  wishlist_emailme = wishlist_emailme,
                                  wishlist_user = useroff,
                                  )
            wishlist.save()           
        return redirect(Wishlistuser,username=username)    
    else:
        form= WishlistForm()
    context ={
      'form' : form,
    }
    return render(request, 'store/wishlist_create.html',context)

def about(request):
    return render(request, "store/about.html")

def contactusView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "store/contactus.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')    