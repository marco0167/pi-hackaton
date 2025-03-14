from lara_sdk import Translator, Credentials
from fastapi import FastAPI

LARA_ACCESS_KEY_ID = "S8OISRB7D2VVMVS34IN60R8L61"      # Replace with your Access Key ID
LARA_ACCESS_KEY_SECRET = "jnnes79-SEFSl9AmbiwYlHkI8DkivUIKlMUKfHRKWQU"  # Replace with your Access Key SECRET

def translate_text(text, leanguage):
	credentials = Credentials(access_key_id=LARA_ACCESS_KEY_ID, access_key_secret=LARA_ACCESS_KEY_SECRET)
	lara = Translator(credentials)
	res = lara.translate(text,
						 source="it-IT",
						 target=leanguage)
	return res.translation

app = FastAPI()

@app.post("/translate")
async def translate(text: str, leanguage: str):
	return {"translation": translate_text(text, leanguage)}

if __name__ == '__main__':
	import uvicorn
	uvicorn.run(app, host="0.0.0.0", port=8000)
