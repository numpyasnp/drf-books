Books-Comment api / Add fake data (User or Book) / Spesific Permissions

# SuperUser
Username = admin

password = admin123

# Add Fake User and Data
python manage.py shell

from Comment.models import Books, Comment

from scripts.fake_data import add_user, add_book

for _ in range(2):

    add_user()

Output like this

Tracy Heath tracy_heath@evans.com

user created tracy_heath

Christian Burton christian_burton@brown-reynolds.com

user created christian_burton

# Add Books
add_book("love") # add books about "love"

add_book("natural") # add books about "natural"



# books api from openlibrary
http://openlibrary.org/search.json?q=love (Topic = love)



python manage.py runserver
