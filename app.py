from flask import Flask, jsonify, request
from flask_cors import CORS
 

app = Flask(__name__)
CORS(app)

# Product dataset
products = [
    {
        "id": 1,
        "name": "Relaxation Tea",
        "type": "beverage",
        "description": "A soothing herbal tea blend designed for relaxation and stress relief.",
        "effects": ["relaxation", "stress relief"],
        "ingredients": ["Chamomile", "Lavender"],
        "price": 12.99,
    },
    {
        "id": 2,
        "name": "Energy Booster Coffee",
        "type": "beverage",
        "description": "A strong coffee blend designed to increase energy and focus.",
        "effects": ["energy boost", "focus"],
        "ingredients": ["Coffee Beans", "Ginseng"],
        "price": 15.99,
    }
]

# Knowledge base for RAG
knowledge_base = {
    "Chamomile": "Chamomile has a mild, floral aroma and is known for its calming effects. It is commonly used to reduce stress and improve sleep.",
    "Lavender": "Lavender is known for its soothing properties and is often used in aromatherapy to reduce anxiety and promote relaxation.",
    "Coffee Beans": "Coffee beans contain caffeine, which boosts alertness and energy. They are widely consumed for mental focus and productivity.",
    "Ginseng": "Ginseng is an adaptogenic herb that improves mental performance, reduces fatigue, and enhances overall well-being."
}

# RAG-enhanced recommendation function
def recommend_products(preferences):
    recommended_products = []
    
    for product in products:
        if any(effect in product["effects"] for effect in preferences.get("effects", [])):
            # Retrieve additional knowledge for each ingredient
            additional_info = []
            for ingredient in product["ingredients"]:
                if ingredient in knowledge_base:
                    additional_info.append(f"{ingredient}: {knowledge_base[ingredient]}")
            
            # Create an enhanced recommendation response
            product_info = {
                "name": product["name"],
                "description": product["description"],
                "price": product["price"],
                "augmented_info": additional_info  # RAG-enhanced data
            }
            recommended_products.append(product_info)

    return recommended_products

@app.route('/recommendations', methods=['POST'])
def get_recommendations():
    preferences = request.json.get("preferences", {})
    recommendations = recommend_products(preferences)
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
