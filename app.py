import os

from flask import Flask
from dotenv import load_dotenv
from portfolio.commonLibs.initialiseLogging import InitialiseLogging
from portfolio.commonLibs.globalVariables import GlobalVariables
from portfolio.routes import routes

load_dotenv()
InitialiseLogging().setupLogging()
GlobalVariables.LOGGER.info("Portfolio app")
app = Flask(__name__)
app.register_blueprint(routes.pages)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=int(os.environ.get("PORT")),debug=True)