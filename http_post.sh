#!/bin/bash

#API_URL="http://192.168.0.106:8000/users"
API_URL="http://192.168.0.106:8001/user_by_id/my_userid/"

userid="my_userid"
username="lynxbee1"
email="social(at)lynxbee.com"
age="45"

home_no=123
street="my home street"
city="my city"
pincode=123456

address="{\"home_no\":\"$home_no\",\"street\":\"$street\",\"city\":\"$city\",\"pincode\":\"$pincode\"}"

data="{\"userid\":\"$userid\",\"username\":\"$username\",\"email\":\"$email\",\"age\":\"$age\", \"useraddress\":"$address"}"
echo $data

#exit
#curl -v -k -X POST -H "\"Accept: application/json\"" -H "\"Content-Type:application/json\"" -d $data "$API_URL"
echo curl -v -k -X POST -H "\"Accept: application/json\"" -H "\"Content-Type:application/json\"" -d $data "$API_URL"


