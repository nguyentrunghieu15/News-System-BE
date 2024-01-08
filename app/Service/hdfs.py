
import os
import requests


class hdfs():
    def __init__(self) -> None:
        pass

    def put_news(path_file,url,delete=False):
        print(f'Put hdfs {url}, file:{path_file}')
        # Specify the file you want to upload
        files = {'file': (path_file, open(path_file, 'rb'))}

        # Make the POST request
        response = requests.post(url, files=files)

        # Check the response
        if response.status_code == 200:
            print("File uploaded successfully")
        else:
            print(f"Failed to upload file. Status code: {response.status_code}")
            print(response.text)
        
        if delete:
            try:
                os.remove(path_file)
                print(f"File '{path_file}' deleted successfully.")
            except FileNotFoundError:
                print(f"File '{path_file}' not found.")
            except Exception as e:
                print(f"An error occurred: {e}")
    
    def put_stocks(path_file,url,delete=False):
        # Specify the file you want to upload
        files = {'file': (path_file, open(path_file, 'rb'))}

        # Make the POST request
        response = requests.post(url, files=files)

        # Check the response
        if response.status_code == 200:
            print("File uploaded successfully")
        else:
            print(f"Failed to upload file. Status code: {response.status_code}")
            print(response.text)
        
        if delete:
            try:
                os.remove(path_file)
                print(f"File '{path_file}' deleted successfully.")
            except FileNotFoundError:
                print(f"File '{path_file}' not found.")
            except Exception as e:
                print(f"An error occurred: {e}")
    
    def ls(path,url):
        response = requests.get(f'{url}{path}')
        # Check the response
        if response.status_code == 200:
            return response.json()            
        else:
            print(f"Failed to req. Status code: {response.status_code}")
            print(response.text)