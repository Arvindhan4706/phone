import phonenumbers
from Text import number
from phonenumbers import geocoder
from phonenumbers import timezone
from phonenumbers import carrier

number = input("Enter phone number with country code: ")
phoneNumber = phonenumbers.parse(number)
timezone=timezone.time_zones_for_number(phoneNumber)
print("timeZone :" + str(timezone))
geolocation=geocoder.description_for_number(phoneNumber,"en")
print("location :"+geolocation)
service=carrier.name_for_number(phoneNumber,"en")
print("service provider: "+ service)