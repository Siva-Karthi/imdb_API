# from rest_framework import serializers
# from rest_framework.serializers import ModelSerializer
# 
# from api.models import Movie
# 
# class GenreSerializer(ModelSerializer):
# #     class Meta:
# #         model = Track
# #         fields = ('order', 'title', 'duration')
#       genre = serializers.SlugRelatedField(
#         many=True,
#         read_only=True,
#         slug_field='genre'
#      )
# 
# class MovieSerializer(ModelSerializer):
#     class Meta:
#         model = Movie
#         fields = ('id', 'name', 'director','popularity','genre','imdb_score')
#         extra_kwargs = {
#             'id': {'read_only': True}
#         }

from rest_framework import exceptions
from rest_framework import serializers
from .models import MovieModel, GenreModel
from rest_framework.validators import UniqueValidator


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = GenreModel
        fields = ('genre_name', )


class MovieSerializer(serializers.ModelSerializer):

    # genre = serializers.StringRelatedField(many=True)
    # name = serializers.CharField(required=True, validators=[UniqueValidator(queryset=MovieModel.objects.all(), message = "Given movie already exists. Try update if any changes need.")])

    class Meta:
        model = MovieModel
        fields = ('popularity_99', 'director', 'genre', 'imdb_score', 'name')

    def to_representation(self, instance):
        ret = super(MovieSerializer, self).to_representation(instance)
        ret['99popularity'] = ret['popularity_99']
        del ret['popularity_99']
        return ret

    # def validate(self,data):
    #     movie = data["name"]
    #     movie_qs = MovieModel.objects.filter(name = movie)
    #     if movie_qs.exists():
    #         raise serializers.ValidationError("Movie already exists")
    #     return data

    def to_internal_value(self, data):
        name = data.get('name')
        # validation for director
        if not name:
            raise exceptions.ValidationError({
                                'name': 'This field is required.'
                                })
        popularity_99 = data.get('99popularity')
        popularity_99_from_admin = data.get('popularity_99')

        #Providing both in while POST 
        if popularity_99 and popularity_99_from_admin:
             raise exceptions.ValidationError({
                                '99popularity or popularity_99': 'Providing any one is sufficient'
                                })
         
        if popularity_99_from_admin :
            popularity_99 = popularity_99_from_admin

        # validation for popularity_99
        if not popularity_99:
            raise exceptions.ValidationError({
                                '99popularity': 'This field is required.'
                                })
        else:
            if float(popularity_99) > 100.0 or float(popularity_99) < 0:
                raise exceptions.ValidationError({
                                '99popularity':
                                'This field value should be between 0 to 100.'
                                })

        director = data.get('director')
        # validation for director
        if not director:
            raise exceptions.ValidationError({
                                'director': 'This field is required.'
                                })

        genre = data.get('genre',["default"])

        imdb_score = data.get('imdb_score')
        # validation for imdb_score
        if not imdb_score:
            raise exceptions.ValidationError({
                                'imdb_score': 'This field is required.'
                                })
        else:
            if float(imdb_score) > 10.0 or float(imdb_score) < 0:
                raise exceptions.ValidationError({
                                'imdb_score':
                                'This field value should be between 0 to 10.'
                                })


        return {
                'popularity_99': float(popularity_99),
                'director': director,
                'genre': genre,
                'imdb_score': float(imdb_score),
                'name': name
              }

    def create(self, validated_data):
        print "here5e in create  "
        new_movie = MovieModel(name=validated_data['name'],
                               director=validated_data['director'],
                               popularity_99=validated_data['popularity_99'],
                               imdb_score=validated_data['imdb_score']
                               )
        new_movie.save()
        # add genre
        for genre in validated_data['genre']:
            obj, created = GenreModel.objects.get_or_create(genre_name=genre)
            new_movie.genre.add(obj)
        return new_movie

    def update(self, instance, validated_data):
        print "here5e   "
        instance.name = validated_data.get('name', instance.name)
        instance.popularity_99 = validated_data.get('popularity_99',
                                                    instance.popularity_99)
        instance.imdb_score = validated_data.get('imdb_score',
                                                 instance.imdb_score)
        instance.director = validated_data.get('director', instance.director)
        # update genre
        instance.genre = []
        # for genre in validated_data['genre']:
        #         obj, created = GenreModel.objects.get_or_create(genre_name=genre.strip())
        #         instance.genre.add(obj)
        if type(validated_data['genre']) == list:
            for genre in validated_data['genre']:
                obj, created = GenreModel.objects.get_or_create(genre_name=genre.strip())
                instance.genre.add(obj)
        else:
            obj, created = GenreModel.objects.get_or_create(genre_name=validated_data['genre'].strip())
            instance.genre.add(obj)
        instance.save()
        return instance


class MovieListSerializer(serializers.ModelSerializer):

    genre = serializers.StringRelatedField(many=True)

    class Meta:
        model = MovieModel
        fields = ('popularity_99', 'director', 'genre', 'imdb_score', 'name')


class MovieCreateSerializer(serializers.ModelSerializer):

    # genre = serializers.StringRelatedField(many=True)
    # genre = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='genre_name'
    #  )
    name = serializers.CharField(required=True, validators=[UniqueValidator(queryset=MovieModel.objects.all(), message = "Given movie already exists. Try update if any changes need.")])

    # Create a custom method field
    # current_user = serializers.SerializerMethodField('_user')

    # Use this method for the custom field
    # def _user(self, obj):
    #    user = self.context['request'].user
    #    return user

    class Meta:
        model = MovieModel
        fields = ('popularity_99', 'director', 'genre', 'imdb_score', 'name')

    def to_representation(self, instance):
        ret = super(MovieCreateSerializer, self).to_representation(instance)
        ret['99popularity'] = ret['popularity_99']
        del ret['popularity_99']
        return ret

    def validate(self,data):
        movie = data["name"]
        movie_qs = MovieModel.objects.filter(name = movie)
        if movie_qs.exists():
            raise serializers.ValidationError("Movie already exists")
        return data

    def to_internal_value(self, data):
        name = data.get('name')
        # validation for director
        if not name:
            raise exceptions.ValidationError({
                                'name': 'This field is required.'
                                })
        popularity_99 = data.get('99popularity')
        popularity_99_from_admin = data.get('popularity_99')

        #Providing both in while POST 
        if popularity_99 and popularity_99_from_admin:
             raise exceptions.ValidationError({
                                '99popularity or popularity_99': 'Providing any one is sufficient'
                                })
         
        if popularity_99_from_admin :
            popularity_99 = popularity_99_from_admin

        if not popularity_99:
            raise exceptions.ValidationError({
                                '99popularity': 'This field is required.'
                                })
        else:
            if float(popularity_99) > 100.0 or float(popularity_99) < 0:
                raise exceptions.ValidationError({
                                '99popularity':
                                'This field value should be between 0 to 100.'
                                })

        director = data.get('director')
        # validation for director
        if not director:
            raise exceptions.ValidationError({
                                'director': 'This field is required.'
                                })

        genre = data.get('genre',["default"])
        print  "genre her", genre

        imdb_score = data.get('imdb_score')
        # validation for imdb_score
        if not imdb_score:
            raise exceptions.ValidationError({
                                'imdb_score': 'This field is required.'
                                })
        else:
            if float(imdb_score) > 10.0 or float(imdb_score) < 0:
                raise exceptions.ValidationError({
                                'imdb_score':
                                'This field value should be between 0 to 10.'
                                })


        return {
                'popularity_99': float(popularity_99),
                'director': director,
                'genre': genre,
                'imdb_score': float(imdb_score),
                'name': name
              }

    def create(self, validated_data):
        new_movie = MovieModel(name=validated_data['name'],
                               director=validated_data['director'],
                               popularity_99=validated_data['popularity_99'],
                               imdb_score=validated_data['imdb_score']
                               )
        new_movie.save()
        if type(validated_data['genre']) == list:
            # add genre
            for genre in validated_data['genre']:
                obj, created = GenreModel.objects.get_or_create(genre_name=genre.strip())
                new_movie.genre.add(obj)
        else:
            obj, created = GenreModel.objects.get_or_create(genre_name=validated_data['genre'].strip())
            new_movie.genre.add(obj)
        return new_movie

