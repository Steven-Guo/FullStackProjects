import fresh_tomatoes
import media

#instantiate a movie instance
warcraft = media.Movie("Warcraft", "2h 30m",
                       "The film portrays the origin story of the initial encounters"
                       " between the humans and the orcs, with an emphasis upon both the Alliance's"
                       " and Horde's sides of their conflict. Featuring characters such as Durotan and Lothar,"
                       " the film will take place in a variety of locations established in the video game series.",
                       "https://upload.wikimedia.org/wikipedia/en/5/56/Warcraft_Teaser_Poster.jpg",
                       "https://www.youtube.com/watch?v=RhFMIRuHAL4")

#construct a list of movies
movies = [warcraft, warcraft, warcraft, warcraft, warcraft, warcraft]

#construct the page with data above
fresh_tomatoes.open_movies_page(movies)