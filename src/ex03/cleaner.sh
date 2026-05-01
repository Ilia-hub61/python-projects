#!/bin/sh

awk -F, 'BEGIN{OFS=","}
NR==1{print $0; next}
{
    if (tolower($3) ~ /junior/) name="Junior";
    else if (tolower($3) ~ /middle/) name="Middle";
    else if (tolower($3) ~ /senior/) name="Senior";
    else name="-";
    print $1, $2, name, $4, $5
}' ../ex02/hh_sorted.csv > hh_positions.csv
