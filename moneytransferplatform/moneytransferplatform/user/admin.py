from django.contrib import admin

class ProfileAdmin(admin.ModelAdmin):
	list_display = [
		'id', 'profileId', 'user', 'name', 'mobileNumber', 'balance'
	]

class UserTransactionAdmin(admin.ModelAdmin):
	list_display = [
		'id',
		'transactionId',
		'sender',
		'reciever',
		'amount',
		'isSuccessful',
		'timestamp'
	]