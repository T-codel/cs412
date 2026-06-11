


from django.urls import path

from dadjokes.views import JokeDetailAPIView, JokesListAPIView, PictureDetailAPIView, PicturesListAPIView, RandomJokeView, RandomPictureAPIView, RandomTemplateAPIView, ShowJokeView, ShowJokesView, ShowPictureView, ShowPicturesView


urlpatterns = [ 

    # show one Joke and one Picture selected at random
    path('', RandomJokeView.as_view(), name='main3'), 

    # another page taht show one Joke and one Picture selected at random
    path('random', RandomJokeView.as_view(), name='random'), 

    # show a page with all Jokes (no images) 
    path('jokes', ShowJokesView.as_view(), name="jokes"),

    # show a page with all pictures
    path('pictures', ShowPicturesView.as_view(), name='pictures'),

    # show one Joke by its primary key
    path('joke/<int:pk>', ShowJokeView.as_view(), name='show_joke'),

    # show one Picture by its primary key
    path('picture/<int:pk>', ShowPictureView.as_view(), name='show_picture'),

    # returns a Json representation of one Joke selected at random
    path(r'api/', RandomTemplateAPIView.as_view()),
    
    # returns a Json representation of one Joke selected at random
    path(r'api/random', RandomTemplateAPIView.as_view()),

    # returns a Json representation of all Jokes
    path(r'api/jokes', JokesListAPIView.as_view()),

    # returns a Json representation of one Joke by its primary key
    path(r'api/joke/<int:pk>', JokeDetailAPIView.as_view()),

    # returns a Json representation of all Pictures
    path(r'api/pictures', PicturesListAPIView.as_view()),

    # returns a Json representation of one Picture by its primary key
    path(r'api/picture/<int:pk>', PictureDetailAPIView.as_view()),

    # returns a Json representation of one Picture selected at random
    path(r'api/random_picture', RandomPictureAPIView.as_view()),
]