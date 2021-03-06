from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import ParseError
from rest_framework import status

from library.error import errorutil
from moneytransferplatform.user.controller import signupcontroller, \
	transactioncontroller, sendmoneycontroller, scheduleusercontroller

class Users(APIView):
	permission_classes = (AllowAny,)

	def post(self, request, format=None):
		apiResponse = None
		try:
			apiResponse = signupcontroller.userSignup(request)
		except ParseError as exception:
			apiResponse = errorutil.getJSONParseError(exception)
		except Exception as exception:
			apiResponse = errorutil.get500Error(exception)
		return JsonResponse(apiResponse.response, status=apiResponse.status)

class Transactions(APIView):
	def get(self, request, userId, format=None):
		apiResponse = None
		try:
			apiResponse = transactioncontroller.getUserTransactions(
				request, userId
			)
		except Exception as exception:
			apiResponse = errorutil.get500Error(exception)
		return JsonResponse(apiResponse.response, status=apiResponse.status)

	def post(self, request, userId, format=None):
		apiResponse = None
		try:
			apiResponse = sendmoneycontroller.sendMoney(request, userId)
		except ParseError as exception:
			apiResponse = errorutil.getJSONParseError(exception)
		except Exception as exception:
			apiResponse = errorutil.get500Error(exception)
		return JsonResponse(apiResponse.response, status=apiResponse.status)

class ScheduleUser(APIView):
	def post(self, request, userId, format=None):
		apiResponse = None
		try:
			apiResponse = scheduleusercontroller.addScheduledUser(request, userId)
		except ParseError as exception:
			apiResponse = errorutil.getJSONParseError(exception)
		except Exception as exception:
			apiResponse = errorutil.get500Error(exception)
		return JsonResponse(apiResponse.response, status=apiResponse.status)