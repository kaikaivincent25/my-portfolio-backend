from django.db import models

class Profile(models.Model):
    full_name = models.CharField(max_length=120)
    title = models.CharField(max_length=120, blank=True)
    bio = models.TextField(blank=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    website = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.full_name

class Project(models.Model):
    STATUS_CHOICES = [('done', 'Done'), ('in_progress', 'In Progress'), ('idea', 'Idea')]
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    description = models.TextField()
    short_description = models.CharField(max_length=300, blank=True)
    cover = models.ImageField(upload_to='projects/', blank=True, null=True)
    demo_url = models.URLField(blank=True)
    repo_url = models.URLField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_progress')
    tech_stack = models.CharField(max_length=300, blank=True)  # comma separated
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['-featured', '-created_at']

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} - {self.email}'