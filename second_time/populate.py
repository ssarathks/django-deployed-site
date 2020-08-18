import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','second_time.settings')

import django
django.setup()

from second_app.models import User
from faker import Faker

faker = Faker()

def fake_data_gen(N=5):
    for entry in range(N):
        fake_name = faker.name().split()
        first_name = fake_name[0]
        last_name = fake_name[1]
        email = faker.email()

        user = User.objects.get_or_create(first_name = first_name,
                                    last_name =last_name,
                                    email = email)[0]
        user.save()

if __name__ == "__main__":
    print('Populating')
    fake_data_gen(20)
    print('population completed')