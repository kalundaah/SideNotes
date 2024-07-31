"""
Initializes the Flask server and the React server as well.
Both servers rely on an understanding of a .env file
"""
# Dependencies
import os
from flask import Flask

# load env file
from dotenv import load_dotenv
load_dotenv('.env')

#Initialize the Flask model
from server import create_app

app = create_app()

if __name__ == "__main__":
    host = os.getenv("HOST_ADDRESS","0.0.0.0")
    port = os.getenv("POST_NUMBER",5000)
    app.run(host=host,
            port=port,
            threaded=True,
            debug=True)
    