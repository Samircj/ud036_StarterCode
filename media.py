import webbrowser

class Video():
    def __init__(self, video_title, video_storyline, video_duration, poster_image, trailer_youtube):
        self.title = video_title
        self.duration = video_duration
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.storyline = video_storyline

class Movie(Video):
    """ This class provides a way to store movie related information"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_yotube, movie_duration):
        Video.__init__(self, movie_title, movie_storyline, movie_duration, poster_image, trailer_yotube) # Call parent class constructor
                

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

class TvShow(Video):
    def __init__(self, show_title, show_storyline, show_season, show_episode, tv_station, show_duration, 
                 poster_image, trailer_youtube):
        Video.__init__(self, show_title, show_storyline, show_duration, 
                       poster_image, trailer_youtube) # Call parent class constructor
        self.season = show_season
        self.episode = show_episode
        self.tv_station = tv_station
    
    # Prints show information
    def get_local_listing(self):
        print("Title: " + self.show_title)
        print("Season: " + self.season)
        print("Episode: " + self.episode)
        print("Station:" + self.tv_station)
        print("Duration: " + str(self.duration))


