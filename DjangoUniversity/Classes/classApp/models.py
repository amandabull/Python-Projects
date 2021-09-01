from django.db import models

class djangoClasses(models.Model):
    title = models.CharField(max_length=60, default="")
    course_number = models.IntegerField()
    instructor_name = models.CharField(max_length=60, default="", blank=True, null=False)
    duration = models.DecimalField(default=0.0, max_digits=10000, decimal_places=1)

    objects = models.Manager()

    def __str__(self):
        return self.title