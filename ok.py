import requests
import glob
import http.client
import json
conn = http.client.HTTPSConnection("api.apyhub.com")
pdf_files = glob.glob("./resume/*.pdf") 
def newurl(url):
    idx=url.index('com')+4
    ans="/"
    for i in range(idx,len(url)):
            ans+=url[i]
    return ans

for pdf_file in pdf_files:
    with open(pdf_file, 'rb') as file: 
        files = {
            'file': open(file.name, 'rb'),
            'language': (None, 'English'),
        }
        response = requests.post('https://api.apyhub.com/sharpapi/api/v1/hr/parse_resume', headers={'apy-token': 'APY0af2rBTFNDGPfze9ov32JbqlLBKGV9rtVSOfvvyJQ5Ymy08mHhKAUUrOEJUx93HxkItFCDB'}, files=files)
        d=json.loads(response.text)
        x=newurl(d["status_url"])
        conn.request("GET",x,headers={
    'apy-token': 'APY0af2rBTFNDGPfze9ov32JbqlLBKGV9rtVSOfvvyJQ5Ymy08mHhKAUUrOEJUx93HxkItFCDB',
    'Content-Type': "application/json"})
        res = conn.getresponse()
        data = res.read()
        print(data.decode('utf-8'))
       


        