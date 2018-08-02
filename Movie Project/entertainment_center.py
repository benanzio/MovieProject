import fresh_tomatoes #imports code from fresh_tomatoes file
import media #imports code from media file

"""movie_name = media.Movie(
        name of movie,
        A small description of the movie,
        url for the movie poster,
        url for the movie trailer)
"""
coco = media.Movie(
    "Coco",
    "A boy is accidentally transported to the land of dead",
    "https://upload.wikimedia.org/wikipedia/en/9/98/Coco_%282017_film%29_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=xlnPHQ3TLX8")

greatest_showman = media.Movie(
    "The Greatest Showman",
    "Ispired by the story of PT Barnums circus creation",
    "https://upload.wikimedia.org/wikipedia/en/1/10/The_Greatest_Showman_poster.png",  # NOQA
    "https://www.youtube.com/watch?v=AXCTMGYUg9A")

oceans_eleven = media.Movie(
    "Ocean's Eleven",
    "A guy and eleven of his friends plan a casino heist",
    "https://upload.wikimedia.org/wikipedia/en/6/68/Ocean%27s_Eleven_2001_Poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=imm6OR605UI")

harry_potter = media.Movie(
    "Harry Potter",
    "The final episode on the boy who lived.",
    "https://upload.wikimedia.org/wikipedia/en/d/df/Harry_Potter_and_the_Deathly_Hallows_%E2%80%93_Part_2.jpg",  # NOQA
    "https://www.youtube.com/watch?v=mObK5XD8udk")

big_sick = media.Movie(
    "The Big Sick",
    "Real life romance of an interracial couple.",
    "https://upload.wikimedia.org/wikipedia/en/6/69/The_Big_Sick.jpg",
    "https://www.youtube.com/watch?v=PJmpSMRQhhs")

la_la_land = media.Movie(
    "La La Land",
    "A couple following their dreams in Los Angeles",
    "https://upload.wikimedia.org/wikipedia/en/a/ab/La_La_Land_%28film%29.png",  # NOQA
    "https://www.youtube.com/watch?v=0pdqf4P9MB8")

taken = media.Movie(
    "Taken",
    "A father tracks down his daughter after being kidnapped.",
    "https://upload.wikimedia.org/wikipedia/en/e/ed/Taken_film_poster.jpg",
    "https://www.youtube.com/watch?v=uPJVJBm9TPA")

without_a_paddle = media.Movie(
    "Without A Paddle",
    "Three reunited friends take a trip up in a remote river.",
    "https://upload.wikimedia.org/wikipedia/en/b/b3/Without_a_Paddle_movie.jpg",  # NOQA
    "https://www.youtube.com/watch?v=CutKiSmYBIg")

green_street_hooligans = media.Movie(
    "Green Street Hooligans",
    "A hardvard student gets in a hooligan firm from West Ham United",
    "https://upload.wikimedia.org/wikipedia/en/f/fe/Greenstreet.jpg",
    "https://www.youtube.com/watch?v=EAe-1Lv1KYU")

movies = [coco, greatest_showman, oceans_eleven, harry_potter,
          big_sick, la_la_land, taken,
          without_a_paddle, green_street_hooligans]

fresh_tomatoes.open_movies_page(movies)  # Opens movie page on web browser

