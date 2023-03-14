import requests
from bs4 import BeautifulSoup
def save_to_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)
    print(f"Saved '{filename}' successfully!")
def save_word_to_file(word):
    with open("usernames.txt", "a") as file:
        file.write(word + "\n")
def search_website(url, word):
    # Check if URL has correct format
    if not url.startswith('http://') and not url.startswith('https://'):
        print("Invalid URL format. Please enter a valid URL starting with 'http://' or 'https://'")
        return

    # Request webpage and create BeautifulSoup object
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Check if word is present on page
        if word in soup.get_text():
            save_word_to_file(url)
        else:
            print(f"The word '{word}' was not found on the page.")
    else:
        print("Error: Failed to retrieve website content.")
def iterate_words(filename):
    with open(filename, 'r') as f:
        # Read all lines from file and join into single string
        text = ' '.join(f.readlines())
        
        # Split text into words using whitespace as separator
        words = text.split()
        
        # Iterate through words and print each one
        for word in words:
            search_website('https://fragment.com/?query='+word, 'Unavailable')
iterate_words('words.txt')

