from django.db import models

def make_equal_length(a):
	return '0'*(4-len(str(a))) + str(a)

class BaseModel(models.Model):
	attr_ID = models.IntegerField()
	target = models.IntegerField()

	# for x in range(1, 1934 + 1):
	# 	locals().update({'VAR_' + make_equal_length(x): models.TextField(null=True)})
