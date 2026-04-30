#!/bin/sh

response=$(curl -s "https://api.hh.ru/vacancies?text=data+scientist&limit=20&order_by=publication_time&page=0")

echo "$response" | jq -R 'fromjson?' > hh.json
