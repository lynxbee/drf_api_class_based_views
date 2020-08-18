#!/bin/bash

API_URL="http://192.168.0.106:8000/users/"

username="lynxbee"
email="sociallynxbee.com"
age="35"

data="{\"username\":\"$username\",\"email\":\"$email\",\"age\":\"$age\"}"
echo $data

curl -v -k -H "\"Accept: application/json\"" -H "\"Content-Type:application/json\"" -d $data $API_URL


