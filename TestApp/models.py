from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


# Create your models here.
class ThoughtPostModel(models.Model):
    user = models.ForeignKey(User,
                             default=1,
                             null=True,
                             on_delete=models.SET_NULL
                             )
    thought_post_text = models.TextField(max_length=1000)

    def __str__(self):
        if self.user is None:
            return "Error in username"
        return str(self.user)
