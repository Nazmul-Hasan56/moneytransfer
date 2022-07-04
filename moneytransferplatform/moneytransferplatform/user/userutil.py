from library.validationresponse import ValidationResponse
from library.error import errorutil
from moneytransferplatform.user.models import Profile

def getValidatedUserProfile(user):
	try:
		userProfile = Profile.objects.get(user=user)
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
