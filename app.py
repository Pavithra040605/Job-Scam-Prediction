from flask import Flask, render_template, request
import pickle
import re

app = Flask(__name__)

# Load model and vectorizer
model = pickle.load(open("job_scam_model.pkl", "rb"))
vectorizer = pickle.load(open("tfidf_vectorizer.pkl", "rb"))

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = ""
    confidence = ""

    if request.method == "POST":
        job_desc = request.form["job_desc"]

        cleaned = clean_text(job_desc)
        vect = vectorizer.transform([cleaned])

        # Get scam probability
        scam_proba = model.predict_proba(vect)[0][1]

        if scam_proba > 0.6:
            prediction = "🚨 High Scam Risk"
        elif scam_proba > 0.3:
            prediction = "⚠️ Medium Scam Risk"
        else:
            prediction = "✅ Low Scam Risk"

        display_proba = min(scam_proba, 0.99)
        confidence = f"Scam Probability: {display_proba:.2f}"


    return render_template(
        "index.html",
        prediction=prediction,
        confidence=confidence
    )

if __name__ == "__main__":
    app.run(debug=True)
