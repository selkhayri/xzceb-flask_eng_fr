"""
Module Docstring!!!
"""
import os

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from flask import Flask, render_template, request, send_from_directory
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)

app = Flask("Web Translator", template_folder="templates")
language_translator = LanguageTranslatorV3(authenticator=authenticator, version='2018-05-01')
language_translator.set_disable_ssl_verification(True)
language_translator.set_service_url(url)

EN_FR = "en-fr"
FR_EN = "fr-en"


@app.route("/englishToFrench")
def english_to_french(english_text=""):
    """
    This function translates English text to French
    """
    if request:
        text_to_translate = request.args.get('textToTranslate')
    else:
        text_to_translate = english_text

    if text_to_translate == "":
        french_text = ""
        return french_text

    french_text = language_translator.translate( text=text_to_translate,
                                                 model_id=EN_FR).get_result()
    return french_text.get("translations")[0].get("translation")


@app.route("/frenchToEnglish")
def french_to_english(french_text=""):
    """
    This function translates French text to English
    """
    if request:
        text_to_translate = request.args.get('textToTranslate')
    else:
        text_to_translate = french_text

    if text_to_translate == "":
        english_text = ""
        return english_text

    english_text = language_translator.translate( text=text_to_translate,
                                                 model_id=FR_EN).get_result()
    return english_text.get("translations")[0].get("translation")


@app.route("/")
def render_index_page():
    """
    This function renders the index page
    """
    return render_template("index.html")


@app.route("/static/<path:path>")
def static_dir(path):
    """
    This function returns the file whose static path is specified in the URL
    """
    return send_from_directory("static", path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
