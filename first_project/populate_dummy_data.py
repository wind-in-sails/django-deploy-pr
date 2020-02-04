import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')
from faker import Faker

import django
django.setup()

from first_app.models import AppUser



def populate(n=5):
    fakegen = Faker()
    for iteration in range(n):
        first_name = fakegen.first_name()
        last_name = fakegen.last_name()
        t = AppUser.objects.get_or_create(first_name=first_name, last_name=last_name)[0]
        t.save()

if __name__ == "__main__":
    print('populating')
    populate(20)
    print("DONE")
else:
    print("Something went wrong")