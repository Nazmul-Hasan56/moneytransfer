import re

from library.error import errorutil
from library.validationresponse import ValidationResponse
from moneytransferplatform.user.models import Profile

def hasMixCase(password):
	return bool(re.search("([a-z].*[A-Z])|([A-Z].*[a-z])", password))

def hasNumber(password):
	return bool(re.search("[0-9]", password))

def hasSpecialCharacter(password):
	return bool(re.search("[^a-zA-Z0-9\s]", password))

def isStrongPassword(password):
	return (
		hasMixCase(password) and
		hasNumber(password) and
		hasSpecialCharacter(password)
	)

def isUserAlreadyExist(mobileNumber):
	return Profile.objects.filter(mobileNumber=mobileNumber).exists()

def canUserSignup(signupParam):
	password = signupParam['password']
	if not isStrongPassword(password):
		return errorutil.get400Error('Weak password', False)
	if isUserAlreadyExist(signupParam['mobileNumber']):
		return errorutil.get409Error(
			'User already exist with this mobile number', False
		)
	return ValidationResponse(True, None, None)	
