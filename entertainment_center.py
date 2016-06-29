import fresh_tomatoes
import media

#instantiate a movie instance
warcraft = media.Movie("Warcraft", "150min",
                       "The film portrays the origin story of the initial encounters"
                       " between the humans and the orcs, with an emphasis upon both the Alliance's"
                       " and Horde's sides of their conflict. Featuring characters such as Durotan and Lothar,"
                       " the film will take place in a variety of locations established in the video game series.",
                       "https://upload.wikimedia.org/wikipedia/en/5/56/Warcraft_Teaser_Poster.jpg",
                       "https://www.youtube.com/watch?v=RhFMIRuHAL4")

dory = media.Movie("Finding Dory", "97min",
                   "The friendly-but-forgetful blue tang fish begins a search for her long-lost parents,"
                   " and everyone learns a few things about the real meaning of family along the way.",
                   "http://ia.media-imdb.com/images/M/MV5BNzg4MjM2NDQ4MV5BMl5BanBnXkFtZTgwMzk3MTgyODE@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                   "https://www.youtube.com/watch?v=dLIy1K8kJPo")

#construct a list of movies
movies = [warcraft, warcraft, warcraft, dory, dory, dory]

#construct the page with data above
fresh_tomatoes.open_movies_page(movies)