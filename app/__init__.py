from flask import Flask 

def create_app():
    app = Flask(__name__)

    app.config.from_pyfile('settings.py')

    #create base data
    

    @app.route('/get-common-news')
    def get_common_news():
        pass

    return app