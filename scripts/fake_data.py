import os
import random
from pprint import pprint

import requests

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Books.settings")

import django

django.setup()

from django.contrib.auth.models import User
from faker import Faker


def set_user():
    fake = Faker(["en_US"])
    f_name = fake.first_name()
    l_name = fake.last_name()
    email = fake.email()
    u_name = f"{f_name.lower()}_{l_name.lower()}"
    email = f"{u_name}@{fake.domain_name()}"
    print(f"{f_name} {l_name} {email}")

    user_check = User.objects.filter(username=u_name)
    while user_check.exists():
        u_name = u_name + str(random.randint(1, 99))

    user = User(
        username=u_name,
        first_name=f_name,
        last_name=l_name,
        email=email,
        is_staff=fake.boolean(chance_of_getting_true=50),
    )
    user.set_password("testing123..")
    user.save()
    print("user created", u_name)


def search_book(topic):
    fake = Faker(["en_US"])
    url = "http://openlibrary.org/search.json"
    payload = {"q": topic}
    response = requests.get(url, params=payload)
    if response.status_code != 200:
        print("Error:", response.status_code)
        return
    jsn = response.json()
    books = jsn.get("docs")
    for book in books:
        # print(book.get("text"))
        data = dict(
            name=book.get("title"),
            author=book.get("author_name")[0],  # return list of authors
            explanation="-".join(book.get("publish_place")),
            publish_at=fake.date_time_between(start_date="-10y", end_date="now"),
        )
        pprint(data)

    # print(response.url)
    # print(response.history)
    # print(response.elapsed.total_seconds())
