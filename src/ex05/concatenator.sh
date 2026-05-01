#!/bin/sh

output="hh_concatenated.csv"

first_file=$(ls *.csv | grep -v "^$output$" | head -n 1)

head -n 1 "$first_file" > "$output"

for file in *.csv; do
    if [ "$file" != "$output" ]; then
        tail -n +2 "$file" >> "$output"
    fi
done
