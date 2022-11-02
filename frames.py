from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile

url = 'http://'

#Question 1
# What is the result of the code

#Question 2
# Download a CSV file from the link and load it into a dataframe
url = ''
df = pd.read_csv(url)

#Question 3


#Question 4


#Question 5
#Create a dataframe from this link https://jsonplaceholder.typicode.com/albums
dff = pd.DataFrame(requests.get('https://jsonplaceholder.typicode.com').json())
print(f'Dataframe is {dff}')