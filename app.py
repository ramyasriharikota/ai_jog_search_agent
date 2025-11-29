from flask import Flask, request, render_template, jsonify
from pydantic import BaseModel
import json
from src.jobs_agent import search_all_platforms

app = Flask(__name__)

class Job(BaseModel):
    title: str
    company: str
    location: str
    salary: str | None = None
    link: str
    platform: str
    posted: str | None = None

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    role = request.form.get("role")
    location = request.form.get("location")
    exp = request.form.get("experience")

    jobs = search_all_platforms(role, location, exp)

    jobs_json = json.dumps(jobs, indent=2, ensure_ascii=False)

    return render_template("results.html", jobs=jobs, jobs_json=jobs_json)

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
