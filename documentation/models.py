from django.db import models

class Language(models.Model):
    name = models.CharField(verbose_name='نام فارسی' ,max_length=50)
    about = models.CharField(verbose_name='درباره' ,max_length=500)
    slug = models.SlugField(verbose_name='نام انگلیسی' ,max_length=50, unique=True, primary_key=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'زبان'
        verbose_name_plural = 'زبان ها'


class Document(models.Model):
    language = models.ForeignKey(Language, models.SET_NULL, verbose_name='زبان', null=True)
    name = models.CharField(verbose_name='نام' ,max_length=50)
    about = models.CharField(verbose_name='درباره' ,max_length=500)
    body = models.TextField(verbose_name='توضیحات مستند')
    LIBRARY = 'li'
    FRAMEWORK = 'fr'
    TYPE = [
        (LIBRARY, 'کتابخانه'),
        (FRAMEWORK, 'فریمورک')
    ]
    type = models.CharField(verbose_name='نوع', max_length=10, choices=TYPE, default=LIBRARY)
    slug = models.SlugField(verbose_name='لینک' ,max_length=50, unique=True, primary_key=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'مستند'
        verbose_name_plural = 'مستند ها'


class Page(models.Model):
    document = models.ForeignKey(Document, models.SET_NULL, verbose_name='داکیومنت', null=True)
    title = models.CharField(verbose_name='عنوان' ,max_length=100,)
    body = models.TextField(verbose_name='متن')
    date_create = models.DateField(verbose_name='زمان انتشار', auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'صفحه'
        verbose_name_plural = 'صفحه ها'
    
