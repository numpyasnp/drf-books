import os
import random
from pprint import pprint
from tkinter import E

import requests

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Books.settings")

import django

django.setup()

from Comment.api.serializer import BooksSerializer, CommentSerializer
from django.contrib.auth.models import User
from faker import Faker


def add_user():
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

    try:
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
    except Exception as e:
        print("set_user err", e)


def add_book(topic):
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
        book_name = book.get("title")
        data = dict(
            name=book_name,
            author=book.get("author_name")[0],  # return list of authors
            explanation="".join(str(book.get("subject_facet"))),
            publish_at=fake.date_time_between(
                start_date="-10y", end_date="now", tzinfo=None
            ),
        )
        serializer = BooksSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print("book created", book_name)
        else:
            continue

    # print(response.url)
    # print(response.history)
    # print(response.elapsed.total_seconds())
