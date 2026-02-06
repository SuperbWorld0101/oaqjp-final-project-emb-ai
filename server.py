'''
  create a module for the app Emotion Detector
'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

# create a new app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
#define function to run emotion detector
def emo_detector():
    '''get the required data first'''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    dominant= response['dominant_emotion']
    if dominant is None:
        return "Invalid text! Please try again!"
    return f"For the given statement, the system response is 'anger': {response['anger']},\
        'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']}, and 'sadness': {response['sadness']}. \
        The dominant emotion is <b>{response['dominant_emotion']}<b>."

@app.route("/")
#define a function to render temp
def render_index_page():
    '''use the function imported to render template'''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
