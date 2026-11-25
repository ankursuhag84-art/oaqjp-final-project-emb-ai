"""Flask server for the emotion detection web application."""
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emotion_detection_route():
    """Analyse the submitted text and return a formatted response."""
    text_to_analyse = request.args.get("textToAnalyze")
    result = emotion_detector(text_to_analyse)

    # Blank or invalid input
    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (
        "For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


@app.route("/")
def render_index_page():
    """Render the home page."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
