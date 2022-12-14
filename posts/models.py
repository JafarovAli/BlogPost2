from django.db import models
from django.contrib.auth import get_user_model



User = get_user_model()

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username

class Category(models.Model):
    title = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=20)
    slug = models.SlugField()
    thumbnail = models.ImageField()
    def __str__(self):
        return self.title

class contact(models.Model):
    Universitet= models.CharField(max_length=20)
    Fakulte= models.CharField(max_length=20)
    Ixtisas= models.CharField(max_length=20)
    AD= models.CharField(max_length=20)
    Soyad= models.CharField(max_length=20)
    Number = models.CharField(max_length=10)

    
    def __str__(self):
        return self.AD


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()


    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post,verbose_name='Post',related_name='comment',on_delete=models.CASCADE)
    isim_soyisim = models.CharField(verbose_name='Ad,Soyad',max_length=20)
    icerik = models.TextField(verbose_name='icerik', max_length=1000)
    tarix = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'Yorumlar'
        verbose_name_plural = 'Yorumlar'

    def __str__(self):
        return "%s - %s"%(self.post,self.isim_soyisim)