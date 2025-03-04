This is a prototype AI-powered recommendation system that suggests products to users based on their preferences. The system uses Retrieval-Augmented Generation (RAG) to enhance recommendations by incorporating additional knowledge about products.

The system consists of:

Backend: Flask (Python) API for handling product recommendations.
Frontend: HTML + JavaScript to interact with the user.
Data Retrieval: A knowledge base that provides extra product details.

TO RUN REPOSITORY
1. Clone the Repository - First, download the project from GitHub

2. Set Up and Run the Backend (Flask) 
 -> Install Python dependencies: pip install flask flask-cors
 -> Run the Flask server: python app.py

3. Run the Frontend (HTML)
 -> Open the index.html file in any web browser
 -> Enter product effects (e.g., "relaxation, energy boost") and click "Get Recommendations"
 -> View AI-powered product recommendations with extra contextual information

Assumptions and Simplifications
 -> The dataset consists of mock products (e.g., "Relaxation Tea", "Energy Booster Coffee")
 -> No authentication or user-specific learning is implemented (basic prototype)
 -> The recommendation algorithm is rule-based (simple keyword matching instead of ML models)
 -> The knowledge base is a static dictionary (no external data sources are used)

Recommendation Algorithm
 -> The system matches user input (e.g., "relaxation") with product effects.
 -> It filters products that have relevant effects.

Retrieval-Augmented Generation (RAG) Implementation
 -> Each product has ingredients (e.g., Chamomile, Ginseng).
 -> The system retrieves extra knowledge about these ingredients from a knowledge base.
 -> This additional knowledge is added to the product description dynamically.
 -> The final augmented recommendation is displayed to the user

Potential Areas for Improvement
1. Improve the Recommendation Algorithm
 -> Use Machine Learning (ML) models like Collaborative Filtering (e.g., Scikit-Learn, TensorFlow).
 -> Implement Natural Language Processing (NLP) for better understanding of user preferences.

2. Expand the Knowledge Base
 -> Connect to external APIs for more accurate recommendations.
 -> Store product details in a database (MySQL, PostgreSQL, MongoDB) instead of a static dictionary.




