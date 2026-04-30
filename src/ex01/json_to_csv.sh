#!/bin/sh

jq -rf filter.jq ../ex00/hh.json > hh.csv

sed -i '1i"id","created_at","name","has_test","alternate_url"' hh.csv
