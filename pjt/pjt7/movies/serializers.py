from rest_framework import serializers
from movies.models import Movie,Review,Actor


class MovieTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title',)

class ActorNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('name',)

class ReviewSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('title','content',)

class ActorSerializer(serializers.ModelSerializer):
    movies = MovieTitleSerializer(many = True,read_only = True)
    class Meta:
        model = Actor
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieTitleSerializer(Movie ,read_only = True)
    class Meta:
        model = Review
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    actors = ActorNameSerializer(many =True, read_only = True)
    review_set = ReviewSetSerializer(many =True, read_only = True)
    class Meta:
        model = Movie
        fields = '__all__'


class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('id','name')


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title','overview',)

class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('title','content')