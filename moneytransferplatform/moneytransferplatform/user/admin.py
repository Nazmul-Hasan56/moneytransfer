from django.contrib import admin

from moneytransferplatform.user.models import Profile, UserTransaction

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

admin.site.register(Profile, ProfileAdmin)
admin.site.register(UserTransaction, UserTransactionAdmin)