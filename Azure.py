import streamlit as st
import pandas as pd
import numpy as np

st.title("Azure Api's first Doc")

st.header('Welcome to our page know any language in a minute:')
st.write(":star:"*1, ":heart:"*36 ,":star:"*1)


#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&



Entered_text = st.text_input('Enter the text of your choice:')


#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

st.info('select the languages to display')


lang_telugu=st.checkbox('telugu',key=None)
lang_italy=st.checkbox('italy',key=1)
lang_hindi=st.checkbox('hindi',key=2)

if lang_telugu and lang_italy and lang_hindi:
    lang= 'te','it','hi'
elif lang_telugu and lang_italy:
    lang= 'te','it'
elif lang_telugu and lang_hindi:
    lang= 'te','hi'
elif lang_italy and lang_hindi:
    lang= 'it','hi'
elif lang_telugu:
    lang= 'te'
elif lang_italy:
    lang= 'it'
elif lang_hindi:
    lang= 'hi'


button_translate=st.button('Click me',help='To translate language')
##############################################################################################
if button_translate:
    
    
    import requests, uuid, json

    # Add your subscription key and endpoint
    subscription_key = "4079576ad66b4c7497cc6d654ec51da3"
    endpoint = "https://api.cognitive.microsofttranslator.com/"

    # Add your location, also known as region. The default is global.
    # This is required if using a Cognitive Services resource.
    location = "centralindia"

    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'from': 'en',
        'to': [lang]
    }
    constructed_url = endpoint + path

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = [{
        'text': Entered_text
    }]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()

    st.success(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))



########################################################################################################################




#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&


detect=st.text_input('Enter the text to detect:')

#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&


st.info('select the language to detect')

detect_telugu=st.checkbox('telugu_lang',key=3)
detect_italy=st.checkbox('italy_lang',key=4)
detect_hindi=st.checkbox('hindi_lang',key=5)

if detect_telugu and detect_italy and detect_hindi:
    detect_lang= 'te','it','hi'
elif detect_telugu and detect_italy:
    detect_lang= 'te','it'
elif detect_telugu and detect_hindi:
    detect_lang= 'te','hi'
elif detect_italy and detect_hindi:
    detect_lang= 'it','hi'
elif detect_telugu:
    detect_lang= 'te'
elif detect_italy:
    detect_lang= 'it'
elif detect_hindi:
    detect_lang= 'hi'


button_detect=st.button('Click me',help='To detect language')
########################################################################################################################

if button_detect:
    import requests, uuid, json

    # Add your subscription key and endpoint
    subscription_key = "4079576ad66b4c7497cc6d654ec51da3"
    endpoint = "https://api.cognitive.microsofttranslator.com"

    # Add your location, also known as region. The default is global.
    # This is required if using a Cognitive Services resource.
    location = "centralindia"

    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'to': [detect_lang]
    }
    constructed_url = endpoint + path

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = [{
        'text': detect
    }]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response123 = request.json()


    st.success(json.dumps(response123, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))



###############################################################################################################################






#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&


latin=st.text_input('Enter the text to convert to latin:') 

#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&


st.info('select the language to convert lo latin')



latin_data = ['Telugu','Italy','Hindi']

latin_button=st.radio('Select lang',options=latin_data)



if latin_button=='Telugu':
    latin_lang= 'te'
elif latin_button=='Italy' :
    latin_lang= 'it'
elif latin_button=='Hindi':
    latin_lang= 'hi'




###################################################################################################################################
if latin_button:
    import requests, uuid, json

    # Add your subscription key and endpoint
    subscription_key = "4079576ad66b4c7497cc6d654ec51da3"
    endpoint = "https://api.cognitive.microsofttranslator.com"

    # Add your location, also known as region. The default is global.
    # This is required if using a Cognitive Services resource.
    location = "centralindia"

    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        # to translate
        'to': latin_lang,
        'toScript': 'latn'
    }
    constructed_url = endpoint + path

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = [{
        'text': latin
    }]
    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response444 = request.json()

    st.success(json.dumps(response444, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))


######################################################################################################################################

st.write(":star:"*36)
