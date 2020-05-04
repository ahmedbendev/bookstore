from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from users.models import Client
LANGUAGES_CHOICES = (
    ('English', 'English'),
    ('Arabic', 'Arabic'),
    ('Frenche', 'Frenche'),
    ('Other', 'Other')
)
TYPEBOOK_CHOICES = (
    ('USED','usedbook'),
    ('NEW','newbook')
)

class Genre(models.Model):
      name_genre = models.CharField(max_length=200)

      def __str__(self):
          return self.name_genre

      def get_absolute_url(self):
          return reverse('genre-detail', kwargs={'pk':self.pk})

class Book(models.Model):
      title_book = models.CharField(max_length=100)
      num_page_book = models.IntegerField()
      author_book = models.CharField(max_length=100)
      isbn_book = models.CharField(max_length=100)
      image_book = models.ImageField(default='default.jpg', upload_to='profile_pics')
      descript_book = models.TextField()
      langague_book = models.CharField(choices=LANGUAGES_CHOICES,max_length=100)
      genre_book = models.ManyToManyField(Genre)
      type=models.CharField(choices=TYPEBOOK_CHOICES,max_length = 100 , default = "usedbook")

      def __str__(self):
          return self.title_book


class Usedbook(models.Model):
      book = models.OneToOneField(Book, on_delete = models.CASCADE )
      user_usedbook = models.ForeignKey(User, on_delete=models.CASCADE)
      etat_book  = models.TextField(default='availabel')
      date_posted = models.DateTimeField(default=timezone.now)
      etat_actu_book = models.IntegerField(default='9')
      def __str__(self):
          return str(self.pk)

      def get_absolute_url(self):
          return reverse('usedbook-detail', kwargs={'pk':self.pk})

class Newbook(models.Model):
      book = models.OneToOneField(Book, on_delete = models.CASCADE )
      date_start_sell = models.DateTimeField(default=timezone.now)
      quantity_book = models.IntegerField()
      price_book = models.IntegerField()
      date_posted = models.DateTimeField(default=timezone.now)
      stars_book = models.IntegerField(default='5')
      def __str__(self):
          return str(self.pk)

      def get_absolute_url(self):
          return reverse('Newbook-detail', kwargs={'pk':self.pk})

class Wishlist(models.Model):
      wishlist_book = models.CharField(max_length=100)   
      wishlist_date = models.DateTimeField(default=timezone.now)
      wishlist_user = models.ForeignKey(User, on_delete=models.CASCADE)
      wishlist_note = models.CharField(max_length=200)
      wishlist_emailme = models.BooleanField(verbose_name="email me whene the book is available") 
      def __str__(self):
          return str(self.pk)
