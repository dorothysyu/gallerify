from django.db import models

# Create your models here.
# class Gallery(models.Model):
#     num_albums = models.IntegerField(null=False, default=10)
def main(request):
    return HttpResponse("hello")