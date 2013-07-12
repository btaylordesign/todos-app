from django.contrib.auth.models import User
from django.db import models


class CompletedTodoManager(models.Manager):
    def get_query_set(self):
        return super(CompletedTodoManager, self).get_query_set().filter(
            completed_on__isnull=False)


class UncompletedTodoManager(models.Manager):
    def get_query_set(self):
        return super(UncompletedTodoManager, self).get_query_set().filter(
            completed_on__isnull=True)


class Todo(models.Model):
    user = models.ForeignKey(User, editable=False)
    title = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    completed_on = models.DateTimeField(blank=True, null=True)

    objects = models.Manager()
    complete = CompletedTodoManager()
    uncomplete = UncompletedTodoManager()

    def __unicode__(self):
        return self.title
