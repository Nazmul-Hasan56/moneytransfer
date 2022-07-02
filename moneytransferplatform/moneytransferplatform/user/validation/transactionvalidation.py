from library.validationresponse import ValidationResponse
from library.error import errorutil

from moneytransferplatform.user.models import Profile

def getValidatedUser(user):
	try:
		userProfile = Profile.objects.get(user=user)
		return ValidationResponse(True, userProfile, None)
	except Profile.DoesNotExist as exception:
		return errorutil.get404Error('Profile does not exist', False)

def canUserGetTransactions(user, userId):
	userValidation = getValidatedUser(user)
	if not userValidation.isValid:
		return userValidation
	userProfile = userValidation.response
	if userProfile.profileId != userId:
		return errorutil.get403Error('You do not have permission', False)
	return ValidationResponse(True, userProfile, None)