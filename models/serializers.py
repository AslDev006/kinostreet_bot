from rest_framework import serializers
from .models import *

class SeasonSerializers(serializers.ModelSerializer):
    class Meta:
        model = SeasonModels
        fields = "__all__"

class MainPartSerializers(serializers.ModelSerializer):
    class Meta:
        model = PartModels
        fields = "__all__"


class PartSerializers(serializers.ModelSerializer):
    season = SeasonSerializers(read_only=True, many=True)

    class Meta:
        model = PartModels
        fields = "__all__"




class MovieSerializers(serializers.ModelSerializer):
    part = MainPartSerializers(read_only=True, many=True)
    class Meta:
        model = MovieModels
        fields = "__all__"
