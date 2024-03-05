from django.db import models



# Create your models here.
class home_hero(models.Model):
    slider_img = models.ImageField(upload_to='home/', blank=True, null=True)
    slider_title = models.CharField(max_length=50, blank=True, null=True)
    slider_text = models.TextField(blank=True, null=True)
    poster_img = models.ImageField(upload_to='home/', blank=True, null=True)
    poster_name = models.CharField(max_length=50, blank=True, null=True)
    slider_date = models.DateField(auto_now_add=True) 

    def __str__(self):
        return self.slider_title 

class BlogCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    category_img = models.ImageField(upload_to='category_images/', blank=True, null=True)
    category_title = models.CharField(max_length=150, blank=True, null=True)
    category_date = models.DateField(auto_now_add=True, blank=True, null=True)
   
    
    def __str__(self):
        return self.name

class Blog(models.Model):
    blog_img = models.ImageField(upload_to='home/', blank=True, null=True)
    blog_title = models.CharField(max_length=150, blank=True, null=True)
    blog_date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, null=True, default=0)

    def __str__(self):
        return self.blog_title

class PoliticsBlog(Blog):
    # Add specific fields for politics blog if needed
    pass

class TechnologyBlog(Blog):
    # Add specific fields for technology blog if needed
    pass

class BusinessBlog(Blog):
    # Add specific fields for business blog if needed
    pass

class SportsBlog(Blog):
    # Add specific fields for sports blog if needed
    pass

class ScienceBlog(Blog):
    # Add specific fields for science blog if needed
    pass

class featureVideoCategory(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class featureVideo(models.Model):
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='videos/')
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(featureVideoCategory, on_delete=models.CASCADE, null=True, default=0)
  
    def __str__(self):
        return self.title

class aboutUs(models.Model):
    title = models.CharField(max_length=10)
    story = models.TextField()
    about_img = models.ImageField(upload_to='about/', blank=True, null=True)
    ourStory = models.FileField(upload_to='videos/')
    
    def __str__(self):
        return self.title