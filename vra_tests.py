from __future__ import print_function
import getpass
import json

import vralib


vra = vralib.Session.login(username, password, cloudurl, tenant, ssl_verify=False)
#create_service = vra.get_catalogitem_byname(name="create service")
#create_service = vra.get_catalogitem_byname(name="ubuntu")

#print(create_service)
#print(vra.get_catalogitem_byid(create_service[0]['id']))
#BrequestId:=962feba2-fa96-4084-88e1-c6e23919e5f4,actionId:=fc67a70c-c814-4efb-bced-9e251a4505f3
idr = 'fc67a70c-c814-4efb-bced-9e251a4505f3'
idr2 = '1b1b7381-e151-4b0e-88c1-0f0af07e830e'
idr3 = '962feba2-fa96-4084-88e1-c6e23919e5f4' # Other server
idr4 = '0733766b-109b-476d-bc9d-d2207c8e61cc' # CIS server
#print(vra.get_requests(request_id=None))

# print(vra.get_requests(request_id=idr3))
# print("==============================")
# print(json.dumps(vra.get_resource_view(resource_id='45d019e8-4a58-4232-abf7-1d255d5a1a4d')))
# print("==============================")


# print(vra.get_requests(request_id=idr4))
# print("==============================")
data = vra.get_resource_view(resource_id='784923a7-da7b-4c10-9ec9-42f20a8f446c')
data = data['data']
data['PowerOn'] = False
print(data)
# print("==============================")
# print(json.dumps(vra.get_resource_view(resource_id='784923a7-da7b-4c10-9ec9-42f20a8f446c')))
#print(vra.get_requests_forms_details(resource_id='784923a7-da7b-4c10-9ec9-42f20a8f446c'))

# Power off action ID fc67a70c-c814-4efb-bced-9e251a4505f3
# Power on action ID 3f9e21c5-45c8-4ade-9d75-da19c20a7e46

print(vra.put_resource_action(resource_id='784923a7-da7b-4c10-9ec9-42f20a8f446c',
	                          action_id='fc67a70c-c814-4efb-bced-9e251a4505f3',
	                          payload=""))


# PowerOn	:	true




# PowerOff	:	true
		
# Reboot	:	true
		
# Reset	:	true
		
# Shutdown	:	true
		
# Suspend	:	true

