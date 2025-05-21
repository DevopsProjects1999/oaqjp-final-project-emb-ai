"""Flask app for Emotion Detector."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detector")
@app.route("/emotionDetector")
def emotion_detector_route() -> str:
    """Process emotion detection request and return result or error message."""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response is None:
        return "Invalid text! Please try again!"
    if isinstance(response, dict):
        dominant_emotion = response.get('emotion')
        if dominant_emotion is None:
            return "Invalid text! Please try again!"
        result = dominant_emotion
    else:
        result = response
        if result is None:
            return "Invalid text! Please try again!"
    return (
        f"For the given statement, the system response is dict{response} . "
        f"The dominant emotion is {result}"
    )
@app.route("/")
def render_index_page() -> str:
    """Render the home page."""
    return render_template('index.html')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000)
