from django.db import models

class Posts(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    image = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.title
 
class Comments(models.Model):
    author = models.CharField(max_length=30)
    text = models.TextField()
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, verbose_name='id')

    def __str__(self):
        return self.text