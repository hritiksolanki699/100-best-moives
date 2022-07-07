import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")

movie_name = soup.find_all(name="h3", class_="title", limit=100)
# print(movie_name.getText())

movie_titles = [movie.getText() for movie in movie_name]

movies = movie_titles[::-1]

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")
