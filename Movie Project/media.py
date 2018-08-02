import webbrowser


class Movie():
    """
    This class provides a way to store movie related information. 
    """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        """
        This doctring explains the constructor method inputs and outputs
        :param movie_title: string
        :param movie_storyline : string
        :param poster_image: string
        :param trailer_youtube: string
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        # function that will open the browser and open the movie trailer
        webbrowser.open(self.trailer_youtube_url)

    def show_poster(self):
        # function that will open the browser and open the movie poster.
        webbrowser.open(self.poster_image_url)
