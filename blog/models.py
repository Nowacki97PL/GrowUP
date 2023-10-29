from django.db import models

from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Image(BaseModel):
    avatar = models.ImageField(upload_to="media/post-images", blank=True, null=True)


class Post(BaseModel):
    avatar = models.ImageField(upload_to="media/", blank=True, null=True)
    avatar_thumbnail = ImageSpecField(
        source="avatar",
        processors=[ResizeToFill(200, 200)],
        format="JPEG",
        options={"quality": 100},
    )
    title = models.CharField(max_length=32)
    content = models.TextField()
    image = models.ManyToManyField(Image, blank=True)

    def __str__(self):
        return f"{self.title}"
