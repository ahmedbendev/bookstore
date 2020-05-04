from django import forms
import datetime
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import Profile,Client,Publisher
from .models import Book,Genre,Usedbook,Newbook,Wishlist

CHOICES_BOOK = [('ALL','Allbooks'),('NEW','Newbooks'),('USED','Usedbooks')]
CHOICES_BOOK_LANGUE = [('English','English'),('Arabic','Arabic'),('Frenche','Frenche'),('Other','Other')]
CHOICES_BOOK_GENRE = [
('Action and Adventure','Action and Adventure'),('Anthology','Anthology'),('Classic','Classic'),('Comic and Graphic Novel','Comic and Graphic Novel'),
('Crime and Detective','Crime and Detective'),('Drama','Drama'),('Fable','Fable'),('Fairy Tale','Fairy Tale'),('Fan-Fiction','Fan-Fiction'),
('Fantasy','Fantasy'),('Historical Fiction','Historical Fiction'),('Horror','Horror'),('Humor','Humor'),('Legend','Legend'),('Magical Realism','Magical Realism'),
('Mystery','Mystery'),('Mythology','Mythology'),('Realistic Fiction','Realistic Fiction'),('Romance','Romance'),('Satire','Satire'),('Science Fiction (Sci-Fi)','Science Fiction (Sci-Fi)'),
('Short Story','Short Story'),('Suspense/Thriller','Suspense/Thriller'),('Biography','Biography'),('Essay','Essay'),('Memoir','Memoir'),('Narrative Nonfiction','Narrative Nonfiction'),
('Periodicals','Periodicals'),('Reference Books','Reference Books'),('Self-help Book','Self-help Book'),('Speech','Speech'),('Textbook','Textbook'),
('Poetry','Poetry'),('Speech','Speech'),('Food & Cookbooks','Food & Cookbooks'),('other','other')
]
class AdvancedserchForm(forms.Form):
    serch_keyone = forms.CharField(widget=forms.TextInput(attrs={'class' : 'serch_keyone'}),label='serch keyone ', max_length=100 ,required=False)
    serch_keytwo = forms.CharField(label='serch keytwo', max_length=100,required=False)
    serch_keythree = forms.CharField(label='serch keythree', max_length=100,required=False)
    serch_keyfour = forms.CharField(label='serch keyfour', max_length=100,required=False)
    bookchoice=forms.CharField(label='bookchoice', widget=forms.RadioSelect(choices=CHOICES_BOOK),required=False,initial='ALL')
    booklanguechoice=forms.MultipleChoiceField(label='booklanguechoice', widget=forms.CheckboxSelectMultiple,choices=CHOICES_BOOK_LANGUE,required=False)
    bookgenrechoice=forms.MultipleChoiceField(label='bookgenrechoice', widget=forms.CheckboxSelectMultiple,choices=CHOICES_BOOK_GENRE,required=False)
    title_book= forms.CharField(label='title book', max_length=100 ,required=False, help_text='100 characters max.')
    isbn_book= forms.IntegerField(label='isbn book',required=False)
    user_usedbook= forms.CharField(label='user ubook', max_length=100 ,required=False)
    etat_book= forms.IntegerField(label='etat ubook',required=False)
    date_postedubookstart= forms.DateField(label='start date_posted ubook',initial='2020-01-01',required=False)
    date_postedubookend= forms.DateField(label='end date_posted ubook',initial=datetime.date.today,required=False)
    etat_actu_book= forms.IntegerField(label='etatact ubook',required=False)
    date_postednbookstart= forms.DateField(label='start date_posted nbook',initial='2020-01-01',required=False)
    date_postednbookend= forms.DateField(label='end date_posted nbook',initial=datetime.date.today,required=False)
    price_book= forms.IntegerField(label='price nbook',required=False)
    stars_book= forms.IntegerField(label='stars nbook',required=False)


class CreateusedbookForm(forms.Form):
    title_book = forms.CharField(label='title_book', max_length=100)
    num_page_book = forms.IntegerField(label='num_page_book')
    author_book = forms.CharField(label='author_book',max_length=100)
    isbn_book = forms.CharField(label='isbn_book',max_length=100)
    image_book = forms.ImageField(label='image_book',initial='default.jpg')
    descript_book = forms.CharField(label='descript_book',widget=forms.Textarea)
    langague_book = forms.CharField(label='langague_book',widget=forms.RadioSelect(choices=CHOICES_BOOK_LANGUE))
    genre_book = forms.MultipleChoiceField(label='genre_book',widget=forms.CheckboxSelectMultiple,choices=CHOICES_BOOK_GENRE)
    etat_actu_book = forms.IntegerField(label='etat_actu_book')


class BookUpdateForm(forms.ModelForm):
      class Meta:
        model = Book
        fields = ['title_book','num_page_book','author_book','isbn_book','image_book','descript_book','langague_book','genre_book']

        widgets = {
        "descript_book" : forms.Textarea,
        "langague_book" : forms.RadioSelect(choices=CHOICES_BOOK_LANGUE),
        "genre_book" : forms.CheckboxSelectMultiple(choices=CHOICES_BOOK_GENRE),
        }
class UsedbookUpdateForm(forms.ModelForm):
      class Meta:
        model = Usedbook
        fields = ['etat_actu_book']

class WishlistForm(forms.ModelForm):
      class Meta:
        model = Wishlist
        fields = ['wishlist_book','wishlist_note','wishlist_emailme']        

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)