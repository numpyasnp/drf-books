Books-Comment api / Add fake data (User or Book) / Spesific Permissions

# SuperUser
Username = admin < br >
password = admin123 < br >


# Add Fake User and Data
python manage.py shell< br >
from Comment.models import Books, Comment< br >
from scripts.fake_data import add_user, add_book< br >

# Add Fake User
for _ in range(2):< br >
    add_user()< br >

# Output like this
Tracy Heath tracy_heath@evans.com< br >
user created tracy_heath< br >
Christian Burton christian_burton@brown-reynolds.com< br >
user created christian_burton< br >

# Add Books
add_book("love") # add books about "love"
add_book("natural") # add books about "natural"


# books api from openlibrary
http://openlibrary.org/search.json?q=love (Topic = love)



python manage.py runserver
