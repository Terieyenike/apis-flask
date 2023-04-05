from flask import Flask
import requests
# import os

app = Flask(__name__)

COINCAP_URL = 'https://api.coincap.io/v2/assets/bitcoins'

@app.get("/crypto")
def crypto():
  response = requests.get(COINCAP_URL)
  data = response.json()
  if response.status_code != 200:
    err_msg = "Error displaying the crypto exchange result."
    return {"error": err_msg}
  else:
    return data, 201


# if __name__ == '__main__':
#     port = int(os.environ.get("PORT", 5000))
#     app.run(debug=True, host='0.0.0.0', port=port)