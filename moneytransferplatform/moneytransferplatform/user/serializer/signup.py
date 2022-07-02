from rest_framework import serializers

class SignupSerializerIn(serializers.Serializer):
	name = serializers.CharField(max_length=50)
	password = serializers.CharField(min_length=8)
	mobileNumber = serializers.CharField(min_length=11, max_length=14)
	balance = serializers.DecimalField(max_digits=12, decimal_places=2)