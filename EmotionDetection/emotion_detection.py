import requests,json
 

def emotion_detector(text_to_analyze):
    url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=header)  
    
    if response.status_code == 200:
        response_json = response.json()
        emotion = response_json['emotionPredictions'][0]['emotion']
        return emotion
    elif response.status_code == 400:
        # return dictionary with all keys None
        return {"emotion": None, "confidence": None, "label": None}
    elif response.status_code == 500:
        return None
