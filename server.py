"""
Flask web application for emotion detection using a Watson NLP API.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emotion_analyzer():
    """
    Handle GET requests to /emotionDetector.
    Extracts the text input from query parameters,
    analyzes emotions, and returns a formatted string with results.
    """
    text_to_analyze = request.args.get('textToAnalyze', default='', type=str)
    emotion_result = emotion_detector(text_to_analyze)

    anger = emotion_result['anger']
    disgust = emotion_result['disgust']
    fear = emotion_result['fear']
    sadness = emotion_result['sadness']
    joy = emotion_result['joy']
    dominant_emotion = emotion_result['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'sadness': {sadness}, and 'joy': {joy}. "
        f"The dominant emotion is {dominant_emotion}."
    )


@app.route("/")
def render_index_page():
    """
    Render the homepage HTML.
    """
    return render_template('index.html')


def main():
    """
    Entry point for running the Flask application.
    """
    app.run(host="0.0.0.0", port=5000)


if __name__ == "__main__":
    main()
