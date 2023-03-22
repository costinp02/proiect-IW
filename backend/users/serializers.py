from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="user-detail", lookup_field='pk')
    class Meta:
        model = User
        fields = [
            'url',
            'id',
            'username',
            'role',
            'cnp',
            'password'
        ]

    def validate(self, attrs):
        if str(attrs['role']).lower() == "client":
            validated_cnp = str(attrs['cnp'])
            qs = User.objects.filter(cnp__exact=validated_cnp)
            if qs.exists() or len(validated_cnp) != 13 or not validated_cnp.isnumeric():
                raise serializers.ValidationError(f"Invalid data")
        return super().validate(attrs)
