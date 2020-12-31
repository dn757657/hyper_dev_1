from django.db import models
from hyper.users.models import User

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)
    # associated project
    # associated tasks

    def __str__(self):
        return self.name


class Project(models.Model):
    # primary key is added automatically!
    title = models.CharField(max_length=256)
    desc = models.TextField()

    # define status choices for creating and editing (future)
    NOT_STARTED = 'NS'
    ON_HOLD = 'OH'
    ON_TRACK = 'OT'
    CANCELLED = 'CA'
    BEHIND = 'BE'
    STATUS_CHOICES = [
        (NOT_STARTED, 'Not Started'),
        (ON_HOLD, 'On Hold'),
        (ON_TRACK, 'On Track'),
        (CANCELLED, 'Cancelled'),
        (BEHIND, 'Behind')
        ]
    status  = models.CharField(max_length=10, choices=STATUS_CHOICES, default=NOT_STARTED)

    start_date  = models.DateField()
    end_date  = models.DateField()
    budget = models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
    # TODO: add files parameter and file handling capability, aka folder management
    # TODO: based on project names etc.

    project_tags = models.ManyToManyField(Tag, blank=True)
    # assiged_users = models.ManyToManyField(User)


    # calculate progress from another model and use it as a property!
    # @property
    # def progress_status(self):
    #     ''' returns the progress percentage of the project '''
    #     progress = 0
    #     return progress


    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=10)
    desc = models.TextField()
    status = models.CharField(max_length=10)  # complete/active/hold/cancelled
    priority = models.PositiveIntegerField()  # rating can be converted into one of three or four tags?
    project = models.ForeignKey(Project, on_delete=models.CASCADE)  # a project can have many tasks, a task can only be part of one project
    assigned_users = models.ManyToManyField(User)  # a task can have many assigned users, a user can have many tasks
    # task_tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class Comment(models.Model):
    # only prototype, how are comments typicall stored with relations?
    content = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)  # a project can have many comments, a comment can have only one project
    # project can be inferred from task
    tasks = models.ForeignKey(Task, on_delete=models.CASCADE)  # a task can have many comments
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # a user can have many comments, a comment is made by a single user

    def __str__(self):
        return self.content


class Link(models.Model):
    link = models.URLField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    # a project can have many links, links can be duplicated in different projects (although unliekly)

    def __str__(self):
        return self.link
