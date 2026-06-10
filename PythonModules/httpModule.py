#http module
import http.client

conn = http.client.HTTPSConnection("dummyjson.com")

conn.request("GET", "/todo")

response = conn.getresponse()
print(response.status, response.reason)

