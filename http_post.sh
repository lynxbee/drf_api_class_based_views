#!/bin/bash

API_URL="http://192.168.0.106:8000/user"

userid="my_userid"
username="lynxbee1"
email="social(at)lynxbee.com"
age="45"

data="{\"userid\":\"$userid\",\"username\":\"$username\",\"email\":\"$email\",\"age\":\"$age\"}"
echo $data

curl -v -k -X POST -H "\"Accept: application/json\"" -H "\"Content-Type:application/json\"" -d $data "$API_URL/$userid/"


