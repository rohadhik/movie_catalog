import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life","https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://www.youtube.com/watch?v=SgoiKLFBA3Q")


#print(toy_story.storyline)

avatar = media.Movie("Avatar", "A marine on an alien planet", "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY")

#print(avatar.storyline)
#avatar.show_trailer()


bajiraomastani = media.Movie("Baji Roa Mastani","A story of Baji Roa and his lover mastani", "C:\Python27\MyUdacityscripts\Movies\IMG_0018.jpg","C:\Python27\MyUdacityscripts\Movies\Video_0658.MOV")

#bajiraomastani.show_trailer()

Movies = [toy_story, avatar, bajiraomastani]
print (media.Movie.VALID_RATINGS)
#fresh_tomatoes.open_movies_page(Movies)
print (media.Movie.__doc__)
print (media.Movie.__name__)
print (media.Movie.__module__)
