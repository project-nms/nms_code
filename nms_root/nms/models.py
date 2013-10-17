from django.db import models

#Valdiaiton needs to be implemented

class Vendor(models.Model):
	vendor_id = models.AutoField(primary_key=True)
	vendor_name = models.CharField(max_length=255)
	
	def __str__(self):
		return self.vendor_name

class OS_type(models.Model):
	os_type_id = models.AutoField(primary_key=True)
	type = models.CharField(max_length=255)
	
	def __str__(self):
		return self.type

class OS(models.Model):
	os_id = models.AutoField(primary_key=True)
	vendor_id = models.ForeignKey(Vendor)
	os_type_id = models.ForeignKey(OS_type)
	build = models.CharField(max_length=255)
	short_info = models.CharField(max_length=255)
	name = models.CharField(max_length=255)
	
	def __str__(self):
		return str(self.os_type_id) + ' - ' + str(self.name) + ' ' + str(self.build)

class Dev_model(models.Model):
	model_id = models.AutoField(primary_key=True)
	model_name = models.CharField(max_length=255)
	version = models.CharField(max_length=255)
	
	def __str__(self):
		return str(self.model_name) + ' ' + str(self.version)

class Dev_type(models.Model):
	dev_type_id = models.AutoField(primary_key=True)
	dev_type_name = models.CharField(max_length=255)
	
	def __str__(self):
		return self.dev_type_name

class Gen_dev(models.Model):
	gen_dev_id = models.AutoField(primary_key=True)
	vendor_id = models.ForeignKey(Vendor)
	model_id = models.ForeignKey(Dev_model)
	dev_type_id = models.ForeignKey(Dev_type)

	def __str__(self):
		return str(self.dev_type_id) + ' ' + str(self.vendor_id) + ' ' + str(self.model_id) #Making use of the defined __str__ methods of these classes
	
class OS_dev(models.Model):
	os_dev_id = models.AutoField(primary_key=True)
	os_id = models.ForeignKey(OS)
	gen_dev_id = models.ForeignKey(Gen_dev)

	def __str__(self):
		return str(self.os_id) + ' ' + str(self.gen_dev_id)
	
class Devices(models.Model):
	dev_id = models.AutoField(primary_key=True)
	gen_dev_id = models.ForeignKey(Gen_dev)
	os_dev_id = models.ForeignKey(OS_dev)
	ip = models.GenericIPAddressField(protocol='both', unpack_ipv4=False)
	ip_version = models.PositiveIntegerField()
	port = models.PositiveIntegerField(default=22)
	login_name = models.CharField(max_length=255)
	password_remote = models.CharField(max_length=255)
	password_enable = models.CharField(max_length=255)
	pref_remote_prot = models.CharField(max_length=255, default='ssh')
	
	def __str__(self):
		return str(self.gen_dev_id) + ' - ' + str(self.ip)

class User(models.Model):
	user_id = models.AutoField(primary_key=True)
	username = models.CharField(max_length=255)
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	is_active = models.BooleanField(default=False)
	mode = models.PositiveIntegerField(default = '0')
	
	def __str__(self):
		return self.username

class Roles(models.Model):
	roles_id = models.AutoField(primary_key=True)
	user_id = models.ForeignKey(User)
	dev_id = models.ForeignKey(Devices)

	def __str__(self):
		return str(self.user_id) + ': ' + str(self.dev_id)
