from dataclasses import dataclass

@dataclass(frozen=True)
class ErrorType:
	SINGLE = 'SingleError'
	FIELD = 'FieldError'