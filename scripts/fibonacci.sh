#!/bin/bash

if [ $# -lt 1 ]
then
    echo "Call script with a parameter:"
    echo 'sh fibonacci.sh 30'
    exit 1
fi

input=$1
scale=$(expr $input - 3)

first=1
second=1
for i in $(seq $input)
do
    echo $first
    first=$(expr $first + $second)
    echo $second
    second=$(expr $first + $second)
done
