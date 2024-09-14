import http.client

conn = http.client.HTTPSConnection("api.apyhub.com")

headers = {
    'apy-token': "APY0af2rBTFNDGPfze9ov32JbqlLBKGV9rtVSOfvvyJQ5Ymy08mHhKAUUrOEJUx93HxkItFCDB",
    'Content-Type': "application/json"
    }

conn.request("GET", "/sharpapi/api/v1/hr/parse_resume/job/status/c399ac54-cfe7-4d90-a105-26abf90f9dff", headers=headers)

res = conn.getresponse()
data = res.read()


with open('dhenu.txt', 'w') as file:
    file.write(data.decode('utf-8'))
