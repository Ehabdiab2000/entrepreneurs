from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
# Create your models here.
PROJECT_TYPE =(('IT','IT'), ('Technology','Technology'), ('Coffe Shops','Coffe Shops'),('Manufacturing','Manufacturing'), ('Media','Media'))

def image_upload(instance,filename):
    imagename,extension = filename.split('.')
    return 'projects/%s.%s'%(instance.id,extension)



class Project(models.Model):  # creates table in database
    owner = models.ForeignKey(User, related_name='project_owner', on_delete=models.CASCADE)
    title= models.CharField(max_length=100)    # creates  column in the table
    description = models.TextField(max_length=1000)
    project_type = models.CharField(max_length=20, choices=PROJECT_TYPE)
    published_at =models.DateTimeField(auto_now=True)
    budget =models.IntegerField(default=0)   # expected Budjet
    image = models.ImageField(upload_to=image_upload)
    location = models.CharField(max_length=100)
    slug = models.SlugField(null=True,blank=True)



    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super(Project,self).save(*args, **kwargs)

    def __str__(self):    # to make object name the title name
        return self.title


class Join(models.Model):
    project = models.ForeignKey(Project, related_name='apply_project', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    webiste = models.URLField()
    cv = models.FileField(upload_to='apply/')
    message = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name