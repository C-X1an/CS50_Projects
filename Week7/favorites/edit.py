from cs50 import SQL

name = [
    'Adventure Time',
    'Arrow',
    'Avatar: The Last Airbender',
    'Brooklyn Nine-Nine',
    'Community',
    'Family Guy',
    'Friends',
    'Game of Thrones',
    'Gilmore Girls',
    'Grey’s Anatomy',
    'How I Met Your Mother',
    'It’s Always Sunny in Philadelphia',
    'Parks and Recreation',
    'Sherlock',
    'Squid Game',
    'The Bachelorette',
    'The Crown',
    'The Office',
    'The Queen’s Gambit',
    'The Untamed'
]
db = SQL("sqlite:///favorites.db")

for show in name:
    db.execute("UPDATE shows SET title = ? WHERE title LIKE ?", show,show)

