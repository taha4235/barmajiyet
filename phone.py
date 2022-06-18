import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder 
taha = input("enter ph nb:")
num = phonenumbers.parse(taha)
print(geocoder.description_for_number(number,"en"))
print(carrier.name_for_number(number,"en"))
