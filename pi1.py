from lara_sdk import Translator, Credentials

LARA_ACCESS_KEY_ID = "S8OISRB7D2VVMVS34IN60R8L61"      # Replace with your Access Key ID
LARA_ACCESS_KEY_SECRET = "jnnes79-SEFSl9AmbiwYlHkI8DkivUIKlMUKfHRKWQU"  # Replace with your Access Key SECRET

if __name__ == '__main__':
    credentials = Credentials(access_key_id=LARA_ACCESS_KEY_ID, access_key_secret=LARA_ACCESS_KEY_SECRET)
    lara = Translator(credentials)

    # This translates your text from English ("en-US") to Italian ("it-IT").
    res = lara.translate(" 真正的智慧在 π 的尽头等待着你",
                         source="zh-CN",
                         target="en-US")

    # Prints the translated text: "Ciao, come stai? Questo testo può essere molto lungo."
    print(res.translation)