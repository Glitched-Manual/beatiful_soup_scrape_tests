#!/bin/bash
 
str1="https://static1.e621.net/data/0f/8c/0f8c4421aa65ebcc7c405517a1a14e5d.png"
str2="https://static1.e621.net/data/preview/0f/8c/0f8c4421aa65ebcc7c405517a1a14e5d.jpg"
str3="https://static1.e621.net/data/0f/8c/0f8c4421aa65ebcc7c405517a1a14e5d.jpg"
 
if [ "$str1" == "$str2" ]; then
    echo "Both Strings are Equal."
else
    echo "Both Strings are not Equal."
fi