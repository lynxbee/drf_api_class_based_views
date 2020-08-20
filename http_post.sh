#!/bin/bash

API_URL="http://192.168.0.106:8000/user"

userid="ecbba534-e23b-11ea-96a2-0744224669b7"
username="lynxbee1"
email="social(at)lynxbee.com"
age="45"

data="{\"userid\":\"$userid\",\"username\":\"$username\",\"email\":\"$email\",\"age\":\"$age\"}"
echo $data

curl -v -k -X POST -H "\"Accept: application/json\"" -H "\"Content-Type:application/json\"" -d $data "$API_URL/$userid/"


