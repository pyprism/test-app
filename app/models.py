from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    notify = models.DateField()

    def __str__(self):
        return "%s %s %s" % (self.title, self.content, self.notify)


class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return '%s %s' % (self.title, self.content)