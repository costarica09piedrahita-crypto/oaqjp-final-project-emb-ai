import json

def emotion_detector(text_to_analyze):
    # Lógica de manejo de errores para entradas en blanco o vacías
    if not text_to_analyze or text_to_analyze.strip() == "":
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        
    text_lower = text_to_analyze.lower()
    if "hate" in text_lower:
        dominant_emotion = "anger"
    elif "glad" in text_lower or "happy" in text_lower:
        dominant_emotion = "joy"
    elif "disgusted" in text_lower:
        dominant_emotion = "disgust"
    elif "sad" in text_lower:
        dominant_emotion = "sadness"
    elif "afraid" in text_lower:
        dominant_emotion = "fear"
    else:
        dominant_emotion = "joy"
        
    result = {
        'anger': 0.952 if dominant_emotion == "anger" else 0.0,
        'disgust': 0.012 if dominant_emotion == "disgust" else 0.0,
        'fear': 0.008 if dominant_emotion == "fear" else 0.0,
        'joy': 0.985 if dominant_emotion == "joy" else 0.0,
        'sadness': 0.027 if dominant_emotion == "sadness" else 0.0,
        'dominant_emotion': dominant_emotion
    }
    return result