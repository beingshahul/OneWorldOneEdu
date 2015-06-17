from django.db import models
from django.template.defaultfilters import slugify

from ratings.handlers import ratings
from ratings.forms import SliderVoteForm
# Create your models here.

class Category(models.Model):
    category=models.CharField(max_length = 100, unique= 'true')

    def __unicode__(self):
        return (self.category)


class Tags(models.Model):
    tag=models.CharField(max_length = 100, unique= 'true')

    def __unicode__(self):
        return (self.tag)

        
class OpenCourse(models.Model):
    link=models.URLField(max_length = 200)
    provider=models.CharField(max_length=120)
    language=models.CharField(max_length=50)
    rating=models.DecimalField(max_digits=2, decimal_places=1, default=0)
    panel_rating=models.IntegerField(default=0)
    category=models.ForeignKey(Category, default=1)
    tags=models.ManyToManyField(Tags)
    # author=models.
    title=models.CharField(max_length=200)
    description=models.TextField()
    pubDate = models.DateField()
    slug = models.SlugField()

    # class Meta:
    #     ordering = ["-rating","-panel_rating","title"]

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.title)

        super(OpenCourse, self).save(*args, **kwargs)
    
    def __unicode__(self):
        return (self.title)

# ratings.register(OpenCourse, weight=2, form_class=SliderVoteForm)
ratings.register(OpenCourse)
