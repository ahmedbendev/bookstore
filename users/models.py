from django.db import models
from django.contrib.auth.models import User
from PIL import Image

REGION_CHOICES = (
    ('1', 'Adrar'),
    ('2', 'Chlef'),
    ('3', 'Laghouat'),
    ('4', 'Oum El Bouaghi'),
    ('5', 'Batna'),
    ('6', 'Béjaïa'),
    ('7', 'Biskra'),
    ('8', 'Béchar'),
    ('9', 'Blida'),
    ('10', 'Bouira'),
    ('11', 'Tamanrasset'),
    ('12', 'Tébessa'),
    ('13', 'Tlemcen'),
    ('14', 'Tiaret'),
    ('15', 'Tizi Ouzou'),
    ('16', 'Alger'),
    ('17', 'Djelfa'),
    ('18', 'Jijel'),
    ('19', 'Sétif'),
    ('20', 'Saïda'),
    ('21', 'Skikda'),
    ('22', 'Sidi Bel Abbès'),
    ('23', 'Annaba'),
    ('24', 'Guelma'),
    ('25', 'Constantine'),
    ('26', 'Médéa'),
    ('27', 'Mostaganem'),
    ('28', 'MSila'),
    ('29', 'Mascara'),
    ('30', 'Ouargla'),
    ('31', 'Oran'),
    ('32', 'El Bayadh'),
    ('33', 'Illizi'),
    ('34', 'Bordj Bou Arreridj'),
    ('35', 'Boumerdès'),
    ('36', 'El Tarf'),
    ('37', 'Tindouf'),
    ('38', 'Tissemsilt'),
    ('39', 'El Oued'),
    ('40', 'Khenchela'),
    ('41', 'Souk Ahras'),
    ('42', 'Tipaza'),
    ('43', 'Mila'),
    ('44', 'Aïn Defla'),
    ('45', 'Naâma'),
    ('46', 'Aïn Témouchent'),
    ('47', 'Ghardaïa'),
    ('48', 'Relizane'),
    ('49', 'El MGhair'),
    ('50', 'El Meniaa'),
    ('51', 'Ouled Djellal'),
    ('52', 'Bordj Baji Mokhtar'),
    ('53', 'Béni Abbès'),
    ('54', 'Timimoun'),
    ('55', 'Touggourt'),
    ('56', 'Djanet'),
    ('57', 'In Salah'),
    ('58', 'In Guezzam')
)

# profile models .
class Profile(models.Model):
      user = models.OneToOneField(User, on_delete=models.CASCADE)
      image = models.ImageField(default='default.jpg', upload_to='profile_pics')
      type = models.CharField(max_length = 100 , default = "client")

      def __str__(self):
          return str(self.user.username)

      def save(self, *args, **kwargs):
          super(Profile,self).save(*args, **kwargs)

          img = Image.open(self.image.path)

          if img.height > 300 or img.width > 300:
              output_size = (300, 300)
              img.thumbnail(output_size)
              img.save(self.image.path)

# region_cl models.
class Region(models.Model):
      name_region = models.CharField(max_length=200)
      number_region = models.IntegerField()

      def __str__(self):
          return str(self.name_region)

# client models .
class Client(models.Model):
      profile = models.OneToOneField(Profile , on_delete = models.CASCADE )
      first_name_cl = models.CharField(max_length = 256,null = True)
      last_name_cl = models.CharField(max_length = 256,null = True)
      region_cl = models.ForeignKey(Region ,on_delete=models.SET_NULL,blank=True, null=True)
      adress_cl = models.CharField(max_length = 256,null = True)
      phone_num_cl = models.IntegerField(null = True)
      facebook_cl = models.CharField(max_length = 256,null = True)

      def __str__(self):
           return str(self.first_name_cl)

      def save(self, *args, **kwargs):
          super(Client,self).save(*args, **kwargs)

      def get_absolute_url(self):
         return reverse('client-detail', kwargs={'pk':self.pk})



# publisher models .
class Publisher(models.Model):
      profile = models.OneToOneField(Profile , on_delete = models.CASCADE )
      psudo_pub = models.CharField(max_length = 256)

      def __str__(self):
         return str(self.psudo_pub)
