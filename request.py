import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'rate':5, 'sales_first':200, 'sales_sec':400})

print(r.json())