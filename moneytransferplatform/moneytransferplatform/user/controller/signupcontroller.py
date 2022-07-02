from django.contrib.auth.models import User
from django.db import transaction
from rest_framework import status
from rest_framework.authtoken.models import Token

from library.apiresponse import ApiResponse
from library.error import errorutil
from moneytransferplatform.user.models import Profile
from moneytransferplatform.user.validation import signupvalidation
from moneytransferplatform.user.serializer.signup import SignupSerializerIn

def signup(signupParam):
	with transaction.atomic():
		userName = signupParam['name'].lower()
		password = signupParam['password']
		user = User.objects.create_user(userName, password)
		token, isCreated = Token.objects.get_or_create(user=user)
		profile = Profile(
			name=userName,
			mobileNumber=signupParam['mobileNumber'],
			user=user,
			balance=signupParam['balance']
		)
		profile.save()
	return ApiResponse({'isCreated': True}, status.HTTP_201_CREATED)

def userSignup(request):
	serializerIn = SignupSerializerIn(data=request.data)
	if not serializerIn.is_valid():
		return errorutil.getSerilizerError(serializerIn.errors)
	signupValidation = \
		signupvalidation.canUserSignup(serializerIn.validated_data)
	if not signupValidation.isValid:
		return ApiResponse(signupValidation.response, signupValidation.status)
	return signup(serializerIn.validated_data)