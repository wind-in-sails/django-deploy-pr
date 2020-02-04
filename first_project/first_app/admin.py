from django.contrib import admin
from first_app import models 

# superuser: sergey, test@test.com, qwedcxzas
admin.site.register(models.AppUser)
admin.site.register(models.IssueDescription)
admin.site.register(models.UserProfileInfo)
