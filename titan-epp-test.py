import logging
import os
import time

from epp import epp_client


conn = epp_client.EPPConnection(
	host='titan-qa2.iedr.ie',
    #host='titan-ote.iedr.ie',
	port=700,
	user='epp-sthota-rar',
    password='ieDR@04#$!',
    #user='sthotaepp-ote',
	#password='ieDR12#$',
	verbose=True,
    return_soup=True
)

conn.open()

'''
domain_extists = conn.domain_check(domain_name="acont1.ie")
print("domain exists? :", domain_extists)

#contact_exists = conn.contact_check("testlowfunds")
#print("contact_check :", contact_exists)



#8.1 fix
#---------

#contact_update = conn.contact_update("testrant", email="test.1",auth_info="fwL8krsebuVYfwCo")
#print("contact_update :", contact_update)

'''

# contactInfo = conn.contact_info(contact_id="testrant", auth_info="fwL8krsebuVYfwCo")
# print("contact info:", contactInfo)

contactcreate = conn.contact_create(contact_id="testpytconcreate",
         email="jdoe@example.com", contacts=[{
             "type": "loc",
             "name": "John Doe",
             "org":"Example Inc.",
             "address": {
                 "street":["2 Harbour Square"],
                 "city": "Dublin",
                 "sp": "IE-D",
                 "pc": "A96 D6R0",
                 "cc": "IE",
             },
     }],auth_info="fwL8krsebuVYfwCo", contact_type_extension="abc")

print("contact_create :", contactcreate)


# domain_create = conn.domain_create(domain_name="pytest.ie", registrant="testpytconcreate", period=1, period_units='y', 
#                      contact_admin="testpytconcreate", contact_billing="testpytconcreate", contact_tech="testpytconcreate", auth_info="e3JichTxAaELu24V")
# print("domain_create :", domain_create)



