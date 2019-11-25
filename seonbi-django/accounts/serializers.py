from django.contrib.auth import get_user_model
from rest_framework import serializers

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'password')
        
    def save(self):
        print(self.validated_data)
        user = get_user_model().objects.create_user(**self.validated_data)
        return user