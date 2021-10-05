import phonenumbers
from phonenumbers import geocoder , carrier , timezone

phone_numbers = phonenumbers.parse("+16695918525")

#Country Name
print((geocoder.description_for_number(phone_numbers,'en')))

#Carrier SimCard
print(carrier.name_for_number(phone_numbers, 'en'))

#TimeZone of this Country
print(timezone.time_zones_for_number(phone_numbers))