from django.urls import path

from moneytransferplatform.api import views as userView

urlpatterns = [
	path('users', userView.Users.as_view(), name='signup'),
	path(
		'users/<uuid:userId>/transactions',
		userView.Transactions.as_view(),
		name='userTransactions'
	),
	path(
		'users/<uuid:userId>/schedulers',
		userView.ScheduleUser.as_view(),
		name='addScheduleUser'
	),
]