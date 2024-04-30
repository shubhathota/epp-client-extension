import logging
import os
import time

from epp import epp_client


# conn = epp_client.EPPConnection(
# 	host='titan-qa2.iedr.ie',
#     #host='titan-ote.iedr.ie',
# 	port=700,
# 	user='epp-sthota-rar',
#     password='ieDR@04#$!',
#     #user='sthotaepp-ote',
# 	#password='ieDR12#$',
# 	verbose=True,
#     return_soup=True
# )

# login as other RAR for domain transfer
# conn = epp_client.EPPConnection(
# 	host='titan-qa2.iedr.ie',
#    	port=700,
# 	user='epp-shubha-rar',
#     password='ieDR@15#$!',
# 	verbose=True,
#     return_soup=True
# )

#qa1
conn = epp_client.EPPConnection(
	host='titan-qa.iedr.ie',
    port=700,
	user='sthota',
    password='ieDR05#$',
 	verbose=True,
    return_soup=True
)

conn.open()

#qa1
domain_extists = conn.domain_check(domain_name="831cro.ie")
print("domain exists? :", domain_extists)

#qa2
# domain_extists = conn.domain_check(domain_name="acont1.ie")
# print("domain exists? :", domain_extists)

# contact_exists = conn.contact_check("testpytconcreate")
# print("contact_check :", contact_exists)



#8.1 fix
#---------

# contact_update = conn.contact_update("testrant", email="test.1",auth_info="fwL8krsebuVYfwCo")
# print("contact_update :", contact_update)


# contactInfo = conn.contact_info(contact_id="testrant", auth_info="fwL8krsebuVYfwCo")
# print("contact info:", contactInfo)

# contactcreate = conn.contact_create(contact_id="testpytconcreate",
#          email="jdoe@example.com", contacts=[{
#              "type": "loc",
#              "name": "John Doe",
#              "org":"Example Inc.",
#              "address": {
#                  "street":["2 Harbour Square"],
#                  "city": "Dublin",
#                  "sp": "IE-D",
#                  "pc": "A96 D6R0",
#                  "cc": "IE",
#              },
#      }],auth_info="fwL8krsebuVYfwCo", contact_type_extension="abc")

# print("contact_create :", contactcreate)

# contact_update = conn.contact_update("testpytconcreate", email="johnd@exaample.com", auth_info="jkO5liuytePDtmQa")
# print("contact_update :", contact_update)


#domain_create = conn.domain_create(domain_name="pytest.ie", registrant="testpytconcreate", period=1, period_units='y', 
#                      contact_admin="testpytconcreate", contact_billing="testpytconcreate", contact_tech="testpytconcreate", auth_info="e3JichTxAaELu24V")
# print("domain_create :", domain_create)

#domain update to add nameservers
#domain_update = conn.domain_update(domain_name="pytest.ie", auth_info="jkO5liuytePDtmQa", add_nameservers=["ns3.eppdomain.ie", "ns4.eppdomain.ie"])
#print("domain_update :", domain_update)

#domain renew
# domain_renew = conn.domain_renew(domain_name="pytest.ie", cur_exp_date="2027-03-19",  period=1, period_units='y')
# print("domain_renew :", domain_renew)

#domain transfer
#domain_transfer = conn.domain_transfer(domain_name="pytest.ie", auth_info="jkO5liuytePDtmQa",  period=1, period_units='y')
#print("domain_transfer :", domain_transfer)

#host_info
#host_info = conn.host_info(nameserver="ns3.eppdomain.ie")
#print("host_info :", host_info)

#host_check
#host_check = conn.host_check(nameservers_list = ["ns3.asdtest1.ie"])
#print("host_check :", host_check)

#host_create
#host_create = conn.host_create(nameserver="ns1.pytest.ie", ip_addresses_list=["ipv4=192.0.2.8", "ipv6=1062:0:0:0:7:700:100c:412b"])

#host_create
#host_create = conn.host_create(nameserver="ns1.shubhatest.ie", ip_addresses_list=[{'version': 'v4', 'ip': '193.168.100.151'}, {'version': 'v6', 'ip': '2002:65b:1010:25::54'}])
#print("host_create :", host_create)                                                            

conn.close()

