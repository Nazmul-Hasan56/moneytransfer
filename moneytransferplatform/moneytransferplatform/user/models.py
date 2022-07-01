import uuid
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
	id =  models.BigAutoField(primary_key=True)
	profileId = \
		models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
	user = models.OneToOneField(User, on_delete=models.PROTECT)
	name = models.CharField(max_length=50)
	mobileNumber = models.CharField(max_length=14)
	balance = models.DecimalField(max_digits=12, decimal_places=2)

	def __str__(self):
		return str(self.profileId) + " - " + str(self.name)

class UserTransaction(models.Model):
	id = models.BigAutoField(primary_key=True)
	transactionId = \
		models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
	userProfile = models.ForeignKey(Profile, on_delete=models.PROTECT)
	amount = models.DecimalField(max_digits=12, decimal_places=2)
	isSuccessful = models.BooleanField(default=False)