from django.db import models

# Create your models here.

# Setting Up DataBase Tables here

class USER_TYPE(models.Model):
    typeID      = models.IntegerField(null=False, primary_key=True)
    typeUser    = models.CharField(max_length=30, null=False)

class USER_MASTER(models.Model):
    userID      = models.IntegerField(primary_key=True, null=False)
    typeID      = models.ForeignKey(USER_TYPE, on_delete=models.CASCADE)
    userName    = models.CharField(max_length=50, null=False)
    gender      = models.CharField(max_length=10, null=False)
    email       = models.EmailField(max_length=200, null=False)
    password    = models.CharField(max_length=16, null=False)
    address     = models.CharField(max_length=80,null=False)
    mobile      = models.BigIntegerField(null=False)
    idProof     = models.CharField(max_length=100, null= False)

class PLAN_MASTER(models.Model):
    planID      = models.IntegerField(primary_key=True, null=False)
    planTitle   = models.CharField(max_length=30, null=False)
    planDetail  = models.CharField(max_length=100, null=False)
    planPrice   = models.DecimalField(decimal_places=2,max_digits=10,null=False)
    planDuration= models.IntegerField(null=False)

class MEMBERSHIP_MASTER(models.Model):
    membershipID    = models.IntegerField(primary_key=True, null=False)
    userID          = models.ForeignKey(USER_MASTER,on_delete=models.CASCADE)
    planID          = models.ForeignKey(PLAN_MASTER,on_delete=models.CASCADE)
    startDate       = models.DateField(null=False)
    endDate         = models.DateField(null=False)
    amount          = models.DecimalField(decimal_places=2,max_digits=10,null=False)
    details         = models.CharField(max_length=100)
    membershipStatus= models.CharField(max_length=50, null=False)

class TRAINER_DETAILS(models.Model):
    trainerID   = models.IntegerField(primary_key=True, null=False)
    userID      = models.ForeignKey(USER_MASTER,on_delete=models.CASCADE)
    salary      = models.IntegerField(null=False)
    details     = models.CharField(max_length=100)

class PAYMENT_MASTER(models.Model):
    paymentID   = models.IntegerField(primary_key=True, null=False)
    membershipID= models.ForeignKey(MEMBERSHIP_MASTER,on_delete=models.CASCADE)
    amount      = models.DecimalField(decimal_places=2,max_digits=10,null=False)
    method      = models.CharField(max_length=20, null=False)
    transactionNumber = models.IntegerField(null=False)
    paymentRecipt = models.CharField(max_length=50, null=False)
    paymentStatus = models.CharField(max_length=10,null=False)

class PRODUCT_MASTER(models.Model):
    productID   = models.IntegerField(primary_key=True
    ,null=False)
    productName = models.CharField(max_length=50,null=False)
    quantity    = models.IntegerField(null=False)
    details     = models.CharField(max_length=100)
    price       = models.IntegerField(null=False)
    productImage= models.URLField(null=False)

class FEEDBACK_MASTER(models.Model):
    feedbackID  = models.IntegerField(primary_key=True,null=False)
    userID      = models.ForeignKey(USER_MASTER,on_delete=models.CASCADE)
    details     = models.CharField(max_length=50, null= False)
    rating      = models.IntegerField(null=False)

class WORKOUT_MASTER(models.Model):
    workoutID   = models.IntegerField(primary_key=True, null=False)
    userID      = models.ForeignKey(USER_MASTER,on_delete=models.CASCADE)
    dietChart   = models.CharField(max_length=50)
    workoutSchedule = models.CharField(max_length=50)
    videos      = models.URLField()
    rewards     = models.CharField(max_length=20)

class ORDER_MASTER(models.Model):
    orderID     = models.IntegerField(primary_key=True, null=False)
    userID      = models.ForeignKey(USER_MASTER,on_delete=models.CASCADE)
    orderDate   = models.DateField(null=False)
    deliveryDate= models.DateField(null=False)
    deliveryStatus = models.CharField(null=False, max_length=10)

class ORDER_DETAILS(models.Model):
    detailsID   = models.IntegerField(primary_key=True, null=False)
    orderID     = models.ForeignKey(ORDER_MASTER,on_delete=models.CASCADE)
    productID   = models.ForeignKey(PRODUCT_MASTER,on_delete=models.CASCADE)
    quantity    = models.IntegerField(null=False)
    price       = models.FloatField(null=False)
    total       = models.FloatField(null=False)

class ATTENDANCE_MASTER(models.Model):
    attendanceID    = models.IntegerField(primary_key=True,null=False)
    userID          = models.ForeignKey(USER_MASTER,on_delete=models.CASCADE)
    attendanceDate  = models.DateField(null=False)
    timeIN          = models.TimeField(null=False)
    timeOUT          = models.TimeField(null=False)