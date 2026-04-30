#!/bin/sh

file="../ex03/hh_positions.csv"

awk -F',' '
NR==1 {header=$0; next}
{
    match($2, /T([0-9]{2}:[0-9]{2}:[0-9]{2})/, arr)
    time = arr[1]
    if (!files_created[time]) {
        print header > (time ".csv")
        files_created[time] = 1
    }
    print >> (time ".csv")
}
' "$file"
