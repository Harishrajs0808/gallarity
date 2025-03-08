from django.db import models # type: ignore

class User(models.Model):
    username = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    def __str__(self):
        return self.username

class Wallpaper(models.Model):
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='wallpapers/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
