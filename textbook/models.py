from django.db import models



class Textbook(models.Model):
    title = models.CharField(max_length=50)
    cover_image = models.ImageField(upload_to='textbooks', blank=True)
  
    def __str__(self):
        return self.title



class Chapter(models.Model):
    textbook = models.ForeignKey(Textbook, on_delete=models.CASCADE)
    number = models.IntegerField()
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=500, blank=True, default="")
    intro = models.TextField(blank=True, default="")

    def __str__(self):

        return self.textbook.title +": "+str(self.number) +" "+ self.title
    

class Section(models.Model):
    chapter = models.ForeignKey(Textbook, on_delete=models.CASCADE)
    number = models.FloatField()
    title = models.CharField(max_length=50)
    text = models.TextField(blank=True, default="")
