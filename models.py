from django.db import models
from django.db.models import permalink
from django.utils.text import slugify

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, editable=False, unique=True)
    body = models.TextField()
    posted = models.DateTimeField(db_index=True, auto_now_add=True)
    category = models.ForeignKey('blog.Category', on_delete=models.CASCADE,)

    def __str__(self):
        return '%s' % self.title

    def save(self, *args, **kwargs):
        # if not self.slug:
        self.slug = slugify(self.title + ' ' + self.category.title)

        return super(Blog, self).save(*args, **kwargs)

    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, { 'slug': self.slug })

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True, editable=False, db_index=True)

    def __str__(self):
        return '%s' % self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)

        return super(Category, self).save(*args, **kwargs)

    @permalink
    def get_absolute_url(self):
        return ('view_blog_category', None, { 'slug': self.slug })
