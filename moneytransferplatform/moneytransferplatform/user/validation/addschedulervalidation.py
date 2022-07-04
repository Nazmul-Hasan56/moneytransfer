from dataclasses import dataclass

from library.validationresponse import ValidationResponse
from library.error import errorutil
from moneytransferplatform.user import userutil
from moneytransferplatform.user.models import Profile

@dataclass(frozen=True)
class AddScheduleUserParam:
	userProfile: Profile
	receiverProfile: Profile

def  canUserAddScheduler(user, userId, requestParam):
	userValidation = userutil.getValidatedUserProfile(user)
	if not userValidation.isValid:
		return userValidation
	userProfile = userValidation.response
	if userProfile.profileId != userId:
		return errorutil.get403Error('You do not have permission', False)
	receiverValidation = \
		userutil.getUserProfileByProfileId(requestParam['recieverId'])
	if not receiverValidation.isValid:
		return receiverValidation
	response = AddScheduleUserParam(userProfile, receiverValidation.response)
	return ValidationResponse(True, response, None)
