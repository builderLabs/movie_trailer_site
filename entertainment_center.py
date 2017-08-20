import media
import fresh_tomatoes




#---movie information:----------------------------------------------------------


eddieTheEagle = media.Movie(  "Eddie The Eagle"
                            , "1h 46m"
                            , "PG-13"
                            , "British athlete Michael Edwards is determined "
                              "to represent his country in ski jumping."
                            , "https://upload.wikimedia.org/wikipedia/en/4/4f/"
                              "Eddie_the_Eagle_poster.png"
                            , "https://www.youtube.com/watch?v=hyzQjVUmIxk"
                            )


bridgeOfSpies = media.Movie(  "Bridge of Spies"
                            , "2h 22m"
                            , "PG-13"
                            , "New York lawyer James Donovan is pilot Gary "
                              "Power's only hope of getting out of East Germany."
                            , "https://upload.wikimedia.org/wikipedia/en/f/fa/"
                              "Bridge_of_Spies_poster.jpg"
                            , "https://www.youtube.com/watch?v=A44obMQ8B7o"
                            )


bfg = media.Movie(   "The BFG"
                   , "1h 57m"
                   , "PG"
                   , "Ten-year-old Sophie is in for the adventure of a lifetime "
                     "when she meets the Big Friendly Giant."
                   , "https://upload.wikimedia.org/wikipedia/en/a/af/"
                     "The_BFG_poster.jpg"
                   , "https://www.youtube.com/watch?v=y1fZg0hhBX8"
                   )


theMartian = media.Movie(     "The Martian"
                            , "2h 31m"
                            , "PG-13"
                            , "When astronauts blast off from the planet Mars, "
                              "they leave behind Mark Watney."
                            , "https://upload.wikimedia.org/wikipedia/en/c/cd/"
                              "The_Martian_film_poster.jpg"
                            , "https://www.youtube.com/watch?v=MVs1I6thz7o"
                        )


jurassicWorld = media.Movie(   "Jurassic World"
                             , "2h 5m"
                             , "PG-13"
                             , "Located off the coast of Costa Rica, the "
                               "Jurassic World luxury resort provides a habitat "
                               "for an array of genetically engineered dinosaurs."
                             , "http://vignette2.wikia.nocookie.net/jurassicpark/"
                               "images/f/f5/Jurassic_World_Teaser_Poster.jpg/"
                               "revision/latest/scale-to-width-down/2000?cb=20141015011159"
                             , "https://www.youtube.com/watch?v=jhtt4dd8Rbc"
                        )


theRevenant = media.Movie(    "The Revenant"
                            , "2h 36m"
                            , "R"
                            , "While exploring the uncharted wilderness in 1823, "
                              "frontiersman Hugh Glass sustains life-threatening"
                              "injuries from a brutal bear attack."
                            , "https://upload.wikimedia.org/wikipedia/en/b/b6/"
                              "The_Revenant_2015_film_poster.jpg"
                            , "https://www.youtube.com/watch?v=ox-4hm92XnI"
                        )


#------------------------------------------------------------------------------




#---movie list (modify order here to affect display line-up in web page)
movies =  [
               eddieTheEagle
             , bridgeOfSpies
             , bfg
             , theMartian
             , jurassicWorld
             , theRevenant
          ]

#---create the page
fresh_tomatoes.open_movies_page(movies)
                                                                                                                                                                                           
