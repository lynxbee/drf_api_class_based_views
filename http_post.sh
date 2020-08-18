#!/bin/bash

API_URL="http://192.168.0.106:8000/users/"

username="lynxbee"
email="social(at)lynxbee.com"
age="35"

data="{\"username\":\"$username\",\"email\":\"$email\",\"age\":\"$age\"}"
echo $data

curl -v -k -X POST -H "\"Accept: application/json\"" -H "\"Content-Type:application/json\"" -d $data $API_URL


