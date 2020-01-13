from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField(blank=True)
    image = models.ImageField(upload_to="images/")
    image1 = models.ImageField(upload_to="images/", blank=True)
    image2 = models.ImageField(upload_to="images/", blank=True)
    image3 = models.ImageField(upload_to="images/", blank=True)
    image4 = models.ImageField(upload_to="images/", blank=True)
    image5 = models.ImageField(upload_to="images/", blank=True)
    image6 = models.ImageField(upload_to="images/", blank=True)
    image7 = models.ImageField(upload_to="images/", blank=True)
    image8 = models.ImageField(upload_to="images/", blank=True)
    image9 = models.ImageField(upload_to="images/", blank=True)
    image10 = models.ImageField(upload_to="images/", blank=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100] + '...'

    def pub_date_pretty(self):
        return self.pub_date.strftime('%e %b %Y')
