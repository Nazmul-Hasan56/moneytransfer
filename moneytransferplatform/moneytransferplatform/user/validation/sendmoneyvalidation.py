from dataclasses import dataclass

from library.validationresponse import ValidationResponse
from library.error import errorutil
from moneytransferplatform.user.models import Profile


@dataclass(frozen=True)
class SendMoneyParam:
	userProfile: Profile
	receiverProfile: Profile

def getValidatedUserProfile(user):
	try:
		userProfile = Profile.objects.select_for_update().get(user=user)
		return ValidationResponse(True, userProfile, None)
	except Profile.DoesNotExist as exception:
		return errorutil.get404Error('Profile does not exist', False)

def getUserProfileByProfileId(profileId):
	try:
		userProfile = Profile.objects.select_for_update().get(
			profileId=profileId
		)
		return ValidationResponse(True, userProfile, None)
	except Profile.DoesNotExist as exception:
		return errorutil.get404Error('Receiver profile does not exist', False)

def canUserSendMoney(user, userId, transactionParam):
	userValidation = getValidatedUserProfile(user)
	if not userValidation.isValid:
		return userValidation
	userProfile = userValidation.response
	if userProfile.profileId != userId:
		return errorutil.get403Error('You do not have permission', False)
	recieverId = transactionParam['recieverId']
	receiverValidation = getUserProfileByProfileId(recieverId)
	if not receiverValidation.isValid:
		return receiverValidation
	if userProfile.balance < transactionParam['amount']:
		return errorutil.get400Error('You have exceeded your balance', False)
	response = SendMoneyParam(userProfile, receiverValidation.response)
	return ValidationResponse(True, response, None)