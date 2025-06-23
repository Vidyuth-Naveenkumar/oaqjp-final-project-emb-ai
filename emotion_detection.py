import requests
import json
  
def emotion_detector(text_to_analyse):  
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  
    myobj = { "raw_document": { "text": text_to_analyse } } 
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} 
    
    response = requests.post(url, json=myobj, headers=header) 
    formatted_response = json.loads(response.text)

    # Emotional values
    emotional_data = formatted_response['emotionPredictions'][0]['emotionMentions'][0]['emotion']
    
    anger_score = emotional_data['anger']
    sadness_score = emotional_data['sadness']
    joy_score = emotional_data['joy']
    disgust_score = emotional_data['disgust']
    fear_score = emotional_data['fear']

    # Fixed typo here
    dominant_emotion = max(emotional_data, key=emotional_data.get)

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
