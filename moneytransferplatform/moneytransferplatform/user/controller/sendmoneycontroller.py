from django.db import transaction
from rest_framework import status

from library.error import errorutil
from library.apiresponse import ApiResponse
from moneytransferplatform.user.serializer.transaction import \
	TransactionSerializerIn
from moneytransferplatform.user.validation import sendmoneyvalidation
from moneytransferplatform.user.models import UserTransaction

def saveTransaction(transactionResponse, transactionParam):
	userProfile = transactionResponse.userProfile
	receiverProfile = transactionResponse.receiverProfile
	amount = transactionParam['amount']
	with transaction.atomic():
		userTransaction = UserTransaction(
			sender=userProfile,
			reciever=receiverProfile,
			amount=amount,
			isSuccessful=True
		)
		userTransaction.save()
		userProfile.balance = userProfile.balance - amount
		receiverProfile.balance = receiverProfile.balance + amount
		userProfile.save()
		receiverProfile.save()
		return userTransaction

def sendMoney(request, userId):
	serializerIn = TransactionSerializerIn(data=request.data, many=True)
	if not serializerIn.is_valid():
		return errorutil.getSerilizerError(serializerIn.errors)
	finalResponseList = []
	for transactionParam in serializerIn.validated_data:
		transactionValidation = sendmoneyvalidation.canUserSendMoney(
			request.user, userId, transactionParam
		)
		print(transactionValidation)
		if not transactionValidation.isValid:
			finalResponse = {
				'isSuccessful': False,
				'errorResponse': transactionValidation.response
			}
			finalResponseList.append(finalResponse)
		else:
			transaction = saveTransaction(
				transactionValidation.response, transactionParam
			)
			finalResponse = {
				'transactionId': transaction.transactionId,
				'senderId': transaction.sender.profileId,
				'recieverId': transaction.reciever.profileId,
				'amount': transaction.amount,
				'isSuccessful': transaction.isSuccessful
			}
			finalResponseList.append(finalResponse)
	return ApiResponse(
		{"trandactionResponse": finalResponseList}, status.HTTP_200_OK
	)