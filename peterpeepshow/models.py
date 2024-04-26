from django.db import models

    
class signup(models.Model):
    username = models.CharField(primary_key=True,max_length=30)
    email=models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    class meta:
        db_table="signup"
    def __str__(self):
        return self.username

class movies(models.Model):
    m_name = models.CharField(primary_key=True,max_length=50)
    m_year = models.CharField(max_length=50)
    m_hour = models.CharField(max_length=50)
    m_img = models.ImageField(max_length=50)
    m_link = models.URLField(max_length=200)
    genre = models.CharField(max_length=30, default="action")
    disc = models.CharField(max_length=500)
    director = models.CharField(max_length=30)
    #cast
    class Meta:
        db_table="movies"
    def __str__(self):
        return self.m_name


class gonor(models.Model):
    movie_name=models.CharField(max_length=60)
    go_name=models.CharField(max_length=30)
    class Meta:
        db_table="gonor"
    def __str__(self):
        return self.movie_name

