"""This module provides a function to run emotion detection."""

import requests
import json

def emotion_detector(text_to_analyze):
    """Analyze the emaition based on the input text."""  
      
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=header, timeout=5)
    emotions = {}
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        emotions['dominant_emotion'] = max(emotions, key=emotions.get)
    elif response.status_code == 400:
        emotions = {'anger'  : None, 'disgust'         : None,
                    'fear'   : None, 'joy'             : None,
                    'sadness': None, 'dominant_emotion': None}
        
    return emotions
