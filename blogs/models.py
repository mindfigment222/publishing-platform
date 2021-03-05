from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


class IsActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


def get_blog_image_dir_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / ...
    return 'blogs/{}-{}-{}/images/{}'.format(instance.title,
                                             instance.author.first_name,
                                             instance.author.last_name,
                                             filename)


def get_post_image_dir_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / ...
    return 'blogs/{}-{}-{}/images/posts/{}'.format(instance.blog.title,
                                                   instance.blog.author.first_name,
                                                   instance.blog.author.last_name,
                                                   filename)


class Blog(models.Model):
    title = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blogs')
    is_active = models.BooleanField(default=True)
    about = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=get_blog_image_dir_path,
                              blank=True)

    objects = models.Manager()
    active = IsActiveManager()

    class Meta:
        ordering = ('created',)

    def get_absolute_url(self):
        return reverse('blogs:blog_detail',
                       args=[self.slug])


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique_for_date='publish')
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(upload_to=get_post_image_dir_path,
                              blank=True)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='draft')

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogs:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day, self.slug])