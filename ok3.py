import http.client
import glob
conn = http.client.HTTPSConnection("api.apyhub.com")

headers = {
    'apy-token': "APY0af2rBTFNDGPfze9ov32JbqlLBKGV9rtVSOfvvyJQ5Ymy08mHhKAUUrOEJUx93HxkItFCDB",
    'Content-Type': "application/json"
    }

conn.request("GET", "/sharpapi/api/v1/hr/parse_resume/job/status/c399ac54-cfe7-4d90-a105-26abf90f9dff", headers=headers)

res = conn.getresponse()
data = res.read()

pdf_files = glob.glob("./resume/*.pdf") 

for pdf_file in pdf_files:
    with open(pdf_file, 'rb') as file:  # Open each PDF file in binary mode ('rb')
        
        # You can add code here to process the PDF content if needed
        # Example: You could parse the PDF using libraries like PyPDF2

