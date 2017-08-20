import webbrowser




class Video():
        def __init__(self,video_title,video_duration):
                self.title=video_title
                self.duration=video_duration

class Movie(Video):
        
        """This class serves as a template for a collection of standard
           descriptive variables for films."""
        
        MPAA_RATINGS = [ "G", "PG", "PG-13", "R"]
        
        RATINGS_GUIDE = {
                             'G'     : 'General audiences.'
                           , 'PG'    : 'Parental guidance suggested.'
                           , 'PG-13' : 'Parents strongly cautioned.'
                           , 'R'     : 'Restricted.'
                        }

        def __init__(self, title, duration, rating, movie_storyline, poster_image, trailer_youtube):
                Video.__init__(self,title,duration)
                self.rating=rating
                self.storyline=movie_storyline
                self.poster_image_url=poster_image
                self.trailer_youtube_url = trailer_youtube

        def show_trailer(self):
                webbrowser.open(self.trailer_youtube_url)
