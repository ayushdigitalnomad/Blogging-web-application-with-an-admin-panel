from django.db import models
from django.utils.html import format_html
# Create your models here.
class Category(models.Model):
    cat_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=1000)
    url=models.CharField(max_length=150)
    image=models.ImageField(upload_to="category/")
    add_date=models.DateTimeField(auto_now_add=True,null=True)

    def image_tag(self):
        return format_html('<img src="/media/{}" style="width:40px;height:40px"  />'.format(self.image))

    def __str__(self):
        return self.title
class Post(models.Model):
    post_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    content=models.TextField()
    url=models.CharField(max_length=150)
    image=models.ImageField(upload_to="post/")
    cat=models.ForeignKey(Category,on_delete=models.CASCADE)
    add_date=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.title
