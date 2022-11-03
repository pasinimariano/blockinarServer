from api.index import api

if __name__ == "__main__":
    debug = api.config["DEBUG"]

    api.run(debug=debug, port=3001)
