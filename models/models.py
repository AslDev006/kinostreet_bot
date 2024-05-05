import uuid
from datetime import datetime
from django.db import models
films = 'filmlar'
series = "seriallar"
animes = 'animelar'
primieras = 'primyeralar'

class PartModels(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    photo = models.CharField(max_length=255)
    caption = models.TextField()
    title = models.CharField(max_length=255)
    movie = models.ForeignKey('MovieModels', on_delete=models.CASCADE, related_name='part')
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.movie.title} {self.title}"
class SeasonModels(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    photo = models.CharField(max_length=255)
    caption = models.TextField()
    title = models.CharField(max_length=255)
    season = models.ForeignKey(PartModels, on_delete=models.CASCADE, related_name='season')
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class MovieModels(models.Model):
    Categories = (
        (films, films),
        (series, series),
        (animes, animes),
        (primieras, primieras),
    )
    file_id = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    # season = models.ForeignKey(SeasonModels, on_delete=models.CASCADE, related_name='season')
    # part = models.ForeignKey(PartModels, on_delete=models.CASCADE, related_name='part')
    caption = models.TextField()
    photo = models.CharField(max_length=255, null=True, blank=True)
    category = models.CharField(max_length=25, choices=Categories, default=primieras)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    key = models.CharField(max_length=255, unique=True, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.key} {self.title}"