from django.db import models
from django.utils import timezone

# Model Team
class Team(models.Model):
    image = models.TextField()
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    # Đã sửa: Xóa unique=True (vì mô tả không cần thiết phải duy nhất)
    description = models.TextField() 

    def __str__(self):
        return self.name

# Model cho Bài Viết (Post)
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    # TRƯỜNG IMAGE: Cần thiết để lưu URL ảnh
    image = models.TextField(null=True, blank=True) 
    published_date = models.DateTimeField(default=timezone.now) 
    author = models.CharField(max_length=100, default='Admin')

    def __str__(self):
        return self.title

# Model Comment
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    image = models.TextField(blank=True, null=True) 

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comment by {self.author} on {self.post.title}'