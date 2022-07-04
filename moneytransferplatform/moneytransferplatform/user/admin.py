from django.contrib import admin

from moneytransferplatform.user.models import Profile, UserTransaction, \
	ScheduledUser

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

class ScheduledUserAdmin(admin.ModelAdmin):
	list_display = [
		'id', 'sender', 'reciever', 'amount', 'transferSchedule'
	]

admin.site.register(Profile, ProfileAdmin)
admin.site.register(UserTransaction, UserTransactionAdmin)
admin.site.register(ScheduledUser, ScheduledUserAdmin)