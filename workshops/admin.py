from django.contrib import admin
from .models import Workshop, Enrollment, Feedback

admin.site.register(Workshop)
admin.site.register(Enrollment)
admin.site.register(Feedback)