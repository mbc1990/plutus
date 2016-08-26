from django.db import models

# Create your models here.

# TODO: User 

class Opportunity(models.Model):
    '''
    Represents a job opportunity eg a listing  
    '''
    
    # Company
    company = models.CharField(null=False, max_length=128)

    # Title
    title = models.CharField(null=False, max_length=128)

    # Date added
    date_added = models.DateTimeField(null=False)

    # Link to listing
    listing = models.URLField(null=True, max_length=1024)

    # Free form notes
    notes = models.TextField(null=True)

    # Location
    location = models.CharField(null=True, max_length=128)

    # Referral  
    referral = models.CharField(null=True, max_length=128)


class Interview(models.Model):

    # FK -> opportunity 
    opportunity = models.ForeignKey(Opportunity)

    # Type (phone, in person, etc)
    # Maybe whiteboarding, HR screen, etc. 
    TYPE_PHONE = 1
    TYPE_IN_PERSON = 2
    TYPE_CHOICES = (
        (TYPE_PHONE, "Phone Interview"),
        (TYPE_IN_PERSON, "In Person Interview"),
    )
    interview_type = models.IntegerField(null=False, choices=TYPE_CHOICES)

    # Stage (this is the Nth interview for this postiion)
    stage = models.IntegerField(null=False)

    # Date added
    date_added = models.DateTimeField(null=False)

    # Time
    time = models.DateTimeField(null=False)

    # Location (if in person)
    location = models.CharField(null=True, max_length=128)

    # Notes
    notes = models.TextField(null=True)

    # Outcome - Passed/failed
    outcome = models.NullBooleanField(null=True)

class Offer(models.Model):
    
    # fk -> opportunity
    opportunity = models.ForeignKey(Opportunity)

    # deadline
    deadline = models.DateTimeField(null=False)

    # salary
    salary = models.DecimalField(max_digits=6, decimal_places=2)

    # benefits (free form)
    benefits = models.TextField(null=True)

    # notes 
    notes = models.TextField(null=True)
