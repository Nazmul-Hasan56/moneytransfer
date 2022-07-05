from dataclasses import dataclass

from library.validationresponse import ValidationResponse
from library.error import errorutil
from moneytransferplatform.user import userutil
from moneytransferplatform.user.models import Profile, ScheduledUser

@dataclass(frozen=True)
class AddScheduleUserParam:
	userProfile: Profile
	receiverProfile: Profile

def isScheduleUserExist(userProfile, receiverProfile):
	return ScheduledUser.objects.filter(
		sender=userProfile, reciever=receiverProfile
	).exists()

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
	if isScheduleUserExist(userProfile, receiverValidation.response):
		return errorutil.get400Error('Scheduled user already exist', False)
	response = AddScheduleUserParam(userProfile, receiverValidation.response)
	return ValidationResponse(True, response, None)
