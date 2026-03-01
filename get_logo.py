import urllib.request
import ssl
import base64

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://upload.wikimedia.org/wikipedia/en/2/27/National_Institute_of_Technology%2C_Hamirpur_Logo.png'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    with urllib.request.urlopen(req, context=ctx) as response:
        img_data = response.read()
        b64 = base64.b64encode(img_data).decode('utf-8')
        with open('nith_logo_base64.txt', 'w') as f:
            f.write(b64)
        print('Success!')
except Exception as e:
    print('Error:', e)
