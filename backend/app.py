from flask import Flask, jsonify, request
from flask_cors import CORS 
# ^ this is to import CORS - Cross Origin Resource Sharing because React runs on port 3000 and Flask on port 5000

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

app = Flask(__name__)
CORS(app) #this enables CORS for all routes

# Initialize Spark Session (PySpark)
spark = SparkSession.builder \
    .appName("ProductRecommendation") \
    .getOrCreate()

@app.route('/')
def index():
    return "Welcome to the Product Recommendation API!"

@app.route('/api/products', methods=['GET'])
def get_products():
    try:
        # Sample data (replace this with actual PySpark logic)
        data = [
            {"id": 1, "name": "Product 1", "category": "Electronics"},
            {"id": 2, "name": "Product 2", "category": "Clothing"},
        ]
        
        # You can load data from a file or a PySpark DataFrame
        products_df = spark.createDataFrame(data)
        
        # Convert Spark DataFrame to JSON
        products_json = products_df.toPandas().to_dict(orient='records')
        
        return jsonify(products_json)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/recommendations', methods=['GET'])
def get_recommendations():
    # Example recommendation logic (replace with actual PySpark-based logic)
    try:
        recommendations = [
            {"product_id": 1, "recommended_product": "Product 2"},
            {"product_id": 2, "recommended_product": "Product 1"},
        ]
        return jsonify(recommendations)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
