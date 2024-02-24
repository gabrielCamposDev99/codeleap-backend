from django.db import models

class PostModel(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=100)
    created_datetime = models.DateTimeField()
    title = models.CharField(max_length=255)
    content = models.TextField()
    author_ip = models.CharField(max_length=15)

    class Meta:
        db_table = "posts"

    def __str__(self):
        return self.title