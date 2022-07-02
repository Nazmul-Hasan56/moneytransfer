from rest_framework import status

from library.error import errorutil
from library.apiresponse import ApiResponse
from moneytransferplatform.user.serializer.transaction import \
	TransactionSerializerIn
from moneytransferplatform.user.validation import sendmoneyvalidation

def sendMoney(request, userId):
	serializerIn = TransactionSerializerIn(data=request.data, many=True)
	if not serializerIn.is_valid():
		return errorutil.getSerilizerError(serializerIn.errors)
	for transactionParam in serializerIn.validated_data:
		transactionValidation = sendmoneyvalidation.canUserSendMoney(
			request.user, userId, transactionParam
		)
	return ApiResponse({"isValid": True}, status.HTTP_200_OK)