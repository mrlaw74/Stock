import requests

# The url of the zip file
url = "https://sourceforge.net/projects/ta-lib/files/ta-lib/0.4.0/ta-lib-0.4.0-src.tar.gz/download?use_mirror=udomain"
filename = "ta-lib-0.4.0-src.tar.gz"
response = requests.get(url)

# Open the local file in binary mode and write the response content
with open(filename, "wb") as f:
    f.write(response.content)

# Print a message to indicate success
print(f"Downloaded {filename} from {url}")