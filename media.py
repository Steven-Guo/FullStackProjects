class Movie():
    """Class for Movie. Note: this is a simple demonstration class, the necessary parameters
    are title, poster_image_url, trailer_youtube_url. More information may be added for customization.
    :param title: Movie title
    :param duration: Movie length
    :param storyline: Movie description
    :param poster_image_url: Movie poster URL
    :param trailer_youtube_url: Movie trailer url from Youtube
    """
    def __init__(self, title, duration, storyline, poster_image_url, trailer_youtube_url):
        self.title = title
        self.duration = duration
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url