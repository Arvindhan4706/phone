import phonenumbers
from Text import number
from phonenumbers import geocoder
from phonenumbers import timezone
from phonenumbers import carrier

ch_number = phonenumbers.parse(number,'CH')
print(geocoder.description_for_number(ch_number,'en'))

from phonenumbers import carrier
service_number = phonenumbers.parse(number,'RO')
print(carrier.name_for_number(service_number,'en'))
