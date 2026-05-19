from django.db import models

class Workshop(models.Model):

    title = models.CharField(max_length=200)

    speaker = models.CharField(max_length=100)

    date = models.DateField()

    time = models.TimeField()

    description = models.TextField()

    image = models.ImageField(
    upload_to='workshop_images/',
    blank=True,
    null=True
)

    seats = models.IntegerField()

    def seats_left(self):

        enrolled_count = self.enrollment_set.count()

        return self.seats - enrolled_count

    def __str__(self):
        return self.title
    
from django.contrib.auth.models import User

class Enrollment(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE)

    enrolled_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.workshop.title}"


class Feedback(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    workshop = models.ForeignKey(
        Workshop,
        on_delete=models.CASCADE
    )

    rating = models.IntegerField()

    comment = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return f"{self.user.username} - {self.workshop.title}"