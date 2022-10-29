from collections import namedtuple

Book = namedtuple("Book", "author title genre")
books = [
    Book("Pratchett", "Nightwatch", "fantasy"),
    Book("Pratchett", "Thief Of Time", "fantasy"),
    Book("Le Guin", "The Dispossessed", "scifi"),
    Book("Le Guin", "A Wizard Of Earthsea", "fantasy"),
    Book("Turner", "The Thief", "fantasy"),
    Book("Phillips", "Preston Diamond", "western"),
    Book("Phillips", "Twice Upon A Time", "scifi"),
]

# fantasy_titles = {b.title: b for b in books if b.genre == "fantasy"}
# print(fantasy_titles)

scifi_format = {(f"Title: {scifi.title} - Author: {scifi.author}\n") if scifi.genre == "scifi" else "" for scifi in books}
print("".join(scifi_format))