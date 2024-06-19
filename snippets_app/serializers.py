from rest_framework import serializers

from .models import Snippet
from .models import LANGUAGE_CHOICES, STYLE_CHOICES


# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default="python")
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

#     def create(self, validated_data):
#         return Snippet.objects.create(**validated_data)

#     def update(self, snippet, validated_data):
#         snippet.title = validated_data.get('title', snippet.title)
#         snippet.code = validated_data.get('code', snippet.code)
#         snippet.linenos = validated_data.get('code', snippet.linenos)
#         snippet.language = validated_data.get('code', snippet.language)
#         snippet.style = validated_data.get('code', snippet.style)
#         snippet.save()

#         return snippet


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ["id", "title", "code", "linenos", "language", "style"]
