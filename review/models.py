import datetime

from model_utils import Choices
from django.db import models
from django_countries.fields import CountryField
from languages.fields import LanguageField

from user.models import Member


class Staff(models.Model):
    first_name = models.CharField(max_length=255, blank=True, null=False)
    last_name = models.CharField(max_length=255, blank=True, null=False)
    profile_picture_url = models.ImageField(default='default_cast.png', upload_to='gallery')
    ROLE_CHOICES = Choices('Director', 'Writer', 'Actor')
    role = models.CharField(choices=ROLE_CHOICES, max_length=255)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class MovieReview(models.Model):
    title = models.CharField(max_length=255, blank=True, null=False)
    cover = models.ImageField(default='default_cast.png', upload_to="gallery")
    YEAR_CHOICES = []
    for r in range(1900, (datetime.datetime.now().year + 1)):
        YEAR_CHOICES.append((r, r))
    year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    GENRE_CHOICES = Choices('Action', 'Comedy', 'Drama', 'Family', 'Romance', 'Sci-Fi')
    genre = models.CharField(choices=GENRE_CHOICES, max_length=255, null=False)
    time = models.IntegerField(blank=True, null=False, default=0)
    release_date = models.DateField(default=datetime.date.today)
    description = models.TextField(max_length=255, blank=True, null=False)
    country = CountryField(default='US', null=False)
    movie_language = LanguageField(default='En', null=False)
    IMDB_rating = models.FloatField(max_length=255, blank=True, null=True)
    MPAA_rating = models.IntegerField(blank=True, null=True)
    date_created = models.DateField(default=datetime.date.today)
    alcohol = models.ValueRange(start=0, end=5)
    nudity = models.ValueRange(start=0, end=5)
    LGBTQ = models.ValueRange(start=0, end=5)
    sex = models.ValueRange(start=0, end=5)
    language = models.ValueRange(start=0, end=5)
    violence = models.ValueRange(start=0, end=5)

    def __str__(self):
        return self.title


class Comment(models.Model):
    title = models.CharField(max_length=255, blank=True, null=False)
    content = models.TextField(blank=True, null=False)
    date_added = models.DateField(default=datetime.date.today)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    alcohol = models.ValueRange(start=0, end=5)
    nudity = models.ValueRange(start=0, end=5)
    sex = models.ValueRange(start=0, end=5)
    LGBTQ = models.ValueRange(start=0, end=5)
    language = models.ValueRange(start=0, end=5)
    violence = models.ValueRange(start=0, end=5)
    memberID = models.ForeignKey(Member, on_delete=models.CASCADE, null=True)
    reviewID = models.ForeignKey(MovieReview, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class Suggestion(models.Model):
    title = models.CharField(max_length=255, blank=True, null=False)
    up_votes = models.IntegerField(default=1)
    memberID = models.ForeignKey(Member, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class MovieCast(models.Model):
    castID = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True)
    movieID = models.ForeignKey(MovieReview, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.movieID.title + ' ' + self.castID.role


class UpVote(models.Model):
    memberID = models.ForeignKey(Member, on_delete=models.CASCADE, null=True)
    suggestionID = models.ForeignKey(Suggestion, on_delete=models.CASCADE, null=True)


class ReportComment(models.Model):
    memberID = models.ForeignKey(Member, on_delete=models.CASCADE, null=True)
    commentID = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True)
    content = models.CharField(max_length=255)
    date_added = models.DateField(default=datetime.date.today)


class ReactComment(models.Model):
    memberID = models.ForeignKey(Member, on_delete=models.CASCADE, null=True)
    commentID = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True)
    type = models.BinaryField


class ReportReview(models.Model):
    memberID = models.ForeignKey(Member, on_delete=models.CASCADE, null=True)
    reviewID = models.ForeignKey(MovieReview, on_delete=models.CASCADE, null=True)
    content = models.CharField(max_length=255)
    date_added = models.DateField(default=datetime.date.today)


class ReportMember(models.Model):
    reporterID = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='%(class)s_reporter', null=True)
    reportedID = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='%(class)s_reported', null=True)
    content = models.CharField(max_length=255)
    date_added = models.DateField(default=datetime.date.today)