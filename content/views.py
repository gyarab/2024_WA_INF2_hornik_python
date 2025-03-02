from rest_framework import generics
from django.http import JsonResponse
from .models import Band, Album


def homepage(request):
    return JsonResponse({
        "message": "Welcome to the Music API. You can view bands and albums by visiting /bands/ and /albums/."
    })


class BandListCreate(generics.ListCreateAPIView):
    queryset = Band.objects.all()
    serializer_class = None

    def get_serializer(self, *args, **kwargs):
        from rest_framework import serializers
        class BandSerializer(serializers.ModelSerializer):
            class Meta:
                model = Band
                fields = '__all__'
        self.serializer_class = BandSerializer
        return super().get_serializer(*args, **kwargs)


class BandDetail(generics.RetrieveAPIView):
    queryset = Band.objects.all()
    serializer_class = None

    def get_serializer(self, *args, **kwargs):
        from rest_framework import serializers
        class BandSerializer(serializers.ModelSerializer):
            class Meta:
                model = Band
                fields = '__all__'
        self.serializer_class = BandSerializer
        return super().get_serializer(*args, **kwargs)


class AlbumListCreate(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = None

    def get_serializer(self, *args, **kwargs):
        from rest_framework import serializers
        class AlbumSerializer(serializers.ModelSerializer):
            class Meta:
                model = Album
                fields = '__all__'
        self.serializer_class = AlbumSerializer
        return super().get_serializer(*args, **kwargs)


class AlbumDetail(generics.RetrieveAPIView):
    queryset = Album.objects.all()
    serializer_class = None

    def get_serializer(self, *args, **kwargs):
        from rest_framework import serializers
        class AlbumSerializer(serializers.ModelSerializer):
            class Meta:
                model = Album
                fields = '__all__'
        self.serializer_class = AlbumSerializer
        return super().get_serializer(*args, **kwargs)
