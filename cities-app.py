from flask import Flask, request
from elasticsearch import Elasticsearch

#creates a Flask application instance.
app = Flask(__name__)

#constants that store the password for the Elasticsearch instance and the URL for the Elasticsearch endpoint.
ELASTIC_PASSWORD = "<password>"
CLOUD_ID = "http://<ElaticSearch_Endpoint>:9200"

#creates an Elasticsearch client instance and sets the authentication credentials and endpoint URL.
es = Elasticsearch(
    cloud_id=CLOUD_ID,
    basic_auth=("elastic", ELASTIC_PASSWORD)
)

#creates a Flask endpoint at the root URL ("/") that returns the string "OK".
@app.route("/")
def health_check():
    return "OK"

#creates a Flask endpoint at the /city URL that can accept POST and PUT requests. 
@app.route("/city", methods=["POST", "PUT"])
def insert_update_city():
    city = request.json["city"]
    population = request.json["population"]

    es.index(index="cities", doc_type="city", body={"city": city, "population": population})

    return "City and population added/updated successfully."

#creates a Flask endpoint at the /city/<city> URL that can accept GET requests and retrieves the population of a city from the Elasticsearch index cities
@app.route("/city/<city>", methods=["GET"])
def retrieve_population(city):
    result = es.search(index="cities", body={"query": {"match": {"city": city}}})

    if result["hits"]["total"]["value"] > 0:
        return "The population of " + city + " is " + str(result["hits"]["hits"][0]["_source"]["population"]) + "."
    else:
        return city + " not found in database."

if __name__ == "__main__":
    app.run(debug=True)
