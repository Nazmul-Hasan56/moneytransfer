from django.db import transaction
from rest_framework import status

from library.apiresponse import ApiResponse
from moneytransferplatform.user.models import ScheduledUser, UserTransaction

def createTransaction(sender, reciever, amount):
	with transaction.atomic():
		userTransaction = UserTransaction(
			sender=sender, reciever=reciever, amount=amount, isSuccessful=True
		)
		userTransaction.save()
		sender.balance = sender.balance - amount
		sender.save()
		reciever.balance = reciever.balance + amount
		reciever.save()
		return userTransaction

def scheduleTransaction():
	scheduleTransactionUsers = list(ScheduledUser.objects.all())
	scheduleTransactionList = []
	for scheduleTransactionUser in scheduleTransactionUsers:
		sender = scheduleTransactionUser.sender
		reciever = scheduleTransactionUser.reciever
		amount = scheduleTransactionUser.amount
		userTransaction = createTransaction(sender, reciever, amount)
		userTransactionResponse = {
			'transactionId': userTransaction.transactionId,
			'recieverId': userTransaction.reciever.profileId,
			'amount': userTransaction.amount,
			'isSuccessful': userTransaction.isSuccessful,
			'timestamp': userTransaction.timestamp
		}
		scheduleTransactionList.append(userTransactionResponse)
	response = {'scheduleTransactionList': scheduleTransactionList}
	return ApiResponse(response, status.HTTP_201_CREATED)
