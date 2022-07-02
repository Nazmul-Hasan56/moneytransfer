import logging
from rest_framework import status
from library.apiresponse import ApiResponse
from library.validationresponse import ValidationResponse
from library import constants as const
from library.error.errortype import ErrorType
from library.error.exceptionlogger import logException

logger = logging.getLogger(__name__)

def getFieldErrors(errors):
	fieldErrors = dict(errors)
	fieldErrorDict = {}
	for error in fieldErrors:
		fieldErrorDict[error] = fieldErrors[error][0]
	return fieldErrorDict

def getErrorResponse(errorMesseageType, errorDetail):
	errorResponse = {
		const.IS_VALID_PROPERTY : False,
		const.ERROR_PROPERTY: {
			const.ERROR_TYPE_PROPERTY: errorMesseageType,
		}
	}
	errorProperty = errorResponse[const.ERROR_PROPERTY]
	if errorMesseageType == ErrorType.FIELD:
		errorProperty[const.FIELD_PROPERTY] = errorDetail
	else:
		errorProperty[const.ERROR_MESSAGE_PROPERTY] = errorDetail
	return errorResponse

def getError(errorType, errorMessage, isApiResponse, statusCode):
	errorResponse = {const.ERROR_TYPE_PROPERTY: errorType}
	if errorType == ErrorType.SINGLE:
		errorResponse[const.ERROR_MESSAGE_PROPERTY] = errorMessage
	else:
		errorResponse[const.FIELD_PROPERTY] = errorMessage
	if isApiResponse:
		return ApiResponse(errorResponse, statusCode)
	else:
		return ValidationResponse(False, errorResponse, statusCode)

def getSerilizerError(errors):
	return getError(
		ErrorType.FIELD, errors, True, status.HTTP_400_BAD_REQUEST
	)

def getSingleErrorResponse(errorMsg, isApiResponse, statusCode):
	return getError(ErrorType.SINGLE, errorMsg, isApiResponse, statusCode)

def get400Error(errorMsg, isApiResponse):
	return getSingleErrorResponse(
		errorMsg, isApiResponse, status.HTTP_400_BAD_REQUEST
	)

def get401Error(errorMsg, isApiResponse):
	return getSingleErrorResponse(
		errorMsg, isApiResponse, status.HTTP_401_UNAUTHORIZED
	)

def get404Error(errorMsg, isApiResponse):
	return getSingleErrorResponse(
		errorMsg, isApiResponse, status.HTTP_404_NOT_FOUND
	)

def get403Error(errorMsg, isApiResponse):
	return getSingleErrorResponse(
		errorMsg, isApiResponse, status.HTTP_403_FORBIDDEN
	)

def get409Error(errorMsg, isApiResponse):
	return getSingleErrorResponse(
		errorMsg, isApiResponse, status.HTTP_409_CONFLICT
	)

def getJSONParseError(exception):
	logException(logger, exception, 'Invalid json format')
	return getSingleErrorResponse(
		'Invalid json format',
		True,
		status.HTTP_400_BAD_REQUEST
	)

def get500Error(exception=None, errorMsg=None, isApiResponse=True):
	errMsg = 'Internal server error'
	if errorMsg:
		errMsg = errorMsg
	if exception:
		logException(logger, exception, errMsg)
	return getSingleErrorResponse(
		'Internal server error',
		isApiResponse,
		status.HTTP_500_INTERNAL_SERVER_ERROR
	)
