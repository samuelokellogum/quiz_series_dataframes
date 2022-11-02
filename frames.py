from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile

url = 'http://'


#Question 5
#Create a dataframe from this link https://jsonplaceholder.typicode.com/albums
dff = pd.DataFrame(requests.get('https://jsonplaceholder.typicode.com').json())
print(f'Dataframe is {dff}')