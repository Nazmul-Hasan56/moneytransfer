from rest_framework import status

from library.apiresponse import ApiResponse
from library.error import errorutil
from moneytransferplatform.user.serializer.transaction import \
	TransactionSerializerIn
from moneytransferplatform.user.validation import addschedulervalidation
from moneytransferplatform.user.models import ScheduledUser

def addUser(addScheduledUserResponse, requestParam):
	scheduleUser = ScheduledUser(
		sender=addScheduledUserResponse.userProfile,
		reciever=addScheduledUserResponse.receiverProfile,
		amount=requestParam['amount']
	) 
	scheduleUser.save()
	return ApiResponse({'isAdded': True}, status.HTTP_201_CREATED)

def addScheduledUser(request, userId):
	serializerIn = TransactionSerializerIn(data=request.data)
	if not serializerIn.is_valid():
		return errorutil.getSerilizerError(serializerIn.errors)
	addSchedulerValidation = addschedulervalidation.canUserAddScheduler(
		request.user, userId, serializerIn.validated_data
	)
	if not addSchedulerValidation.isValid:
		return addSchedulerValidation
	return addUser(addSchedulerValidation.response, serializerIn.validated_data)