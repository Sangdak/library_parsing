import requests
from pathlib import Path


def download_books(url, filename):
    response = requests.get(url)
    response.raise_for_status()

    with open(filename, 'wb') as file:
        file.write(response.content)


dir_name = 'books'
for book_id in range(1, 11):
    Path(f'./{dir_name}').mkdir(parents=True, exist_ok=True)
    link_pattern = f'https://tululu.org/txt.php?id={book_id}'
    output = Path(f'./{dir_name}/id{book_id}.txt')
    download_books(link_pattern, output)
