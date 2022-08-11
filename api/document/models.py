from django.db import models

class Language(models.Model):
    name = models.CharField(verbose_name='نام' ,max_length=50)
    slug = models.SlugField(verbose_name='لینک' ,max_length=50, unique=True, primary_key=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'زبان'
        verbose_name_plural = 'زبان ها'


class Document(models.Model):
    language = models.ForeignKey(Language, models.SET_NULL, verbose_name='زبان', null=True)
    slug = models.CharField(verbose_name='نام' ,max_length=50, unique=True, primary_key=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'داکیومنت'
        verbose_name_plural = 'داکیومنت ها'


class Page(models.Model):
    document = models.ForeignKey(Document, models.SET_NULL, verbose_name='داکیومنت', null=True)
    title = models.CharField(verbose_name='عنوان' ,max_length=100,)
    slug = models.SlugField(verbose_name='لینک' ,max_length=50, unique=True, primary_key=True)
    body = models.TextField(verbose_name='متن')
    date_create = models.DateField(verbose_name='زمان انتشار', auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'صفحه'
        verbose_name_plural = 'صفحه ها'
    