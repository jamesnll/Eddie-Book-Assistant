# Imports
from flask import Flask, request, jsonify, send_file
from urllib.parse import unquote
import os

from vector_search import get_recommendations
from tts import text_to_speech

app = Flask(__name__) # Create Flask app

# TODOs
# Create a logging folder that saves the input request and output response as pairs

@app.route('/')
def home():
    return "Hello from the Flask server!"

# Route to retrieve recommendations
@app.route('/recommend-shows', methods=['GET'])
def recommend_shows():

    # Retrieve query from request
    query = request.args.get("query")

    # Check if query is None or empty
    if not query:
        return jsonify({"error": "The 'query' field is required and cannot be empty."}), 400
    
    # Decode the URL-encoded query
    decoded_query = unquote(query)

    print("Query: " + decoded_query)

    # Query the recommendation service
    results = get_recommendations(decoded_query)

    # Output recommendation text
    print("Results: " + str(results))

    # Convert recommendations to speech
    output_path = text_to_speech(results)

    # Output audio file path
    print("Audio output path:" + output_path)

    # Return the output audio file
    return send_file(
        output_path, 
        mimetype='audio/mpeg', 
        as_attachment=False  # Set to True if you want it to download instead of stream
    )

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)