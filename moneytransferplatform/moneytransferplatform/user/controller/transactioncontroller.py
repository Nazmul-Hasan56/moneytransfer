from rest_framework import status

from library.apiresponse import ApiResponse
from moneytransferplatform.user.models import UserTransaction
from moneytransferplatform.user.validation import transactionvalidation

def userTransactions(profile):
	transactions = list(UserTransaction.objects.filter(sender=profile))
	transactionList = []
	for transaction in transactions:
		transactionResponse = {
			'transactionId': transaction.transactionId,
			'recieverId': transaction.reciever.profileId,
			'amount': transaction.amount,
			'isSuccessful': transaction.isSuccessful,
			'timestamp': transaction.timestamp
		}
		transactionList.append(transactionResponse)
	return ApiResponse(
		{'transactionHistory': transactionList}, status.HTTP_200_OK
	)

def getUserTransactions(request, userId):
	userValidation = transactionvalidation.canUserGetTransactions(
		request.user, userId
	)
	if not userValidation.isValid:
		return ApiResponse(userValidation.response, userValidation.status)
	return userTransactions(userValidation.response)