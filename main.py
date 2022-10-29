from api.index import api

if __name__ == "__main__":
    debug = api.config["DEBUG"]
    port = api.config["PORT"]

    api.run(debug=debug, port=port)
