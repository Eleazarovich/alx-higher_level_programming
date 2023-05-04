#!/bin/bash
#this script takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response
curl -sH GET -H "X-School-User_Id: 98" "$1"
