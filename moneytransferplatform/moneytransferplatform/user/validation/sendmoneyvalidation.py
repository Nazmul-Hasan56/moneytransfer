from dataclasses import dataclass

from library.validationresponse import ValidationResponse
from library.error import errorutil
from moneytransferplatform.user import userutil
from moneytransferplatform.user.models import Profile

@dataclass(frozen=True)
class SendMoneyParam:
	userProfile: Profile
	receiverProfile: Profile

def canUserSendMoney(user, userId, transactionParam):
	userValidation = userutil.getValidatedUserProfile(user)
	if not userValidation.isValid:
		return userValidation
	userProfile = userValidation.response
	if userProfile.profileId != userId:
		return errorutil.get403Error('You do not have permission', False)
	recieverId = transactionParam['recieverId']
	receiverValidation = userutil.getUserProfileByProfileId(recieverId)
	if not receiverValidation.isValid:
		return receiverValidation
	if userProfile.balance < transactionParam['amount']:
		return errorutil.get400Error('You have exceeded your balance', False)
	response = SendMoneyParam(userProfile, receiverValidation.response)
	return ValidationResponse(True, response, None)