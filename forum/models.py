from django.db import models
from django.contrib.auth.models import User

# Variable for approved posts
STATUS = ((0, "Not Approved"), (1, "Approved"))

class Post(models.Model):
    """
    Model for posts
    """
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts"
        )
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    # returns only two first lines of comment text
    def get_content_preview(self):
        words = self.content.split()  
        first_20_words = words[:20]  
        return ' '.join(first_20_words)
