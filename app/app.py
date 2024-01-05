import sys   
sys.path.append('./Service')   
import os
from flask import Flask
from Service.crawl import Fetching
from Service.hdfs import hdfs 

PATH_DATA = './app/data'


def create_app():
    app = Flask(__name__)

    app.config.from_pyfile('settings.py')

    hdfs_service = hdfs()
    crawl_service = Fetching(api_key=app.config.get("NEWS_API_KEY"),url_fetch=app.config.get("FECTH_DATA_URL"))

    #create base data
    # Get a list of file names in the specified path
    file_names = [f for f in os.listdir(PATH_DATA) if os.path.isfile(os.path.join(PATH_DATA, f))]
    if len(file_names)==0:
        file_paths=crawl_service.crawlData()
        for file_path in file_paths:
            hdfs.put_news(f'{PATH_DATA}/{file_path}',url=f'{app.config["HDFS_API_URL"]}/fsputnew')
    else :
        files_in_hdfs = hdfs.ls('news',url=f'{app.config.get("HDFS_API_URL")}/fsls/')
        file_names = [item for item in file_names if item not in files_in_hdfs]
        for file_path in file_names:
            hdfs.put_news(f'{PATH_DATA}/{file_path}',url=f'{app.config["HDFS_API_URL"]}/fsputnew')

    @app.route('/get-common-news')
    def get_common_news():
        pass

    return app