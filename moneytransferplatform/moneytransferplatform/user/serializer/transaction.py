from rest_framework import serializers

class TransactionSerializerIn(serializers.Serializer):
	recieverId = serializers.UUIDField()
	amount = serializers.DecimalField(max_digits=12, decimal_places=2)