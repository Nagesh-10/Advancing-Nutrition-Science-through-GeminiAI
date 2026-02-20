
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

# Configure your Gemini API Key here
genai.configure(api_key="AIzaSyBTi1iS9vhmqlBiJkILesKpkMWnSpEVBaY")

model = genai.GenerativeModel("gemini-pro")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/nutrition", methods=["POST"])
def get_nutrition():
    data = request.json
    food = data.get("food")

    prompt = f"""
    Provide detailed nutritional breakdown for:
    {food}

    Include:
    - Calories
    - Protein
    - Carbohydrates
    - Fats
    - Vitamins
    - Minerals
    - Health benefits
    """

    response = model.generate_content(prompt)

    return jsonify({"result": response.text})

@app.route("/mealplan", methods=["POST"])
def meal_plan():
    data = request.json
    goal = data.get("goal")
    diet = data.get("diet")

    prompt = f"""
    Create a 7-day meal plan for:
    Goal: {goal}
    Dietary preference: {diet}

    Include:
    - Breakfast, Lunch, Dinner
    - Macronutrient breakdown
    - Total daily calories
    - Grocery list
    """

    response = model.generate_content(prompt)

    return jsonify({"result": response.text})

if __name__ == "__main__":
    app.run(debug=True)
