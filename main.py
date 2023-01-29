import requests
from pathlib import Path
from pathvalidate import sanitize_filename


def download_txt(url, filename, folder='books/'):
    """Функция для скачивания текстовых файлов.
        Args:
            url (str): Cсылка на текст, который хочется скачать.
            filename (str): Имя файла, с которым сохранять.
            folder (str): Папка, куда сохранять. По умолчанию "books/"
        Returns:
            str: Путь до файла, куда сохранён текст.
        """
    filename = sanitize_filename(filename)
    Path(f'./{folder}').mkdir(parents=True, exist_ok=True)
    filepath = Path(f'./{folder}/{filename}.txt')
    # try:
    response = requests.get(url)
    print('test!')
    response.raise_for_status()

    # check_for_redirect(response)

    with open(filepath, 'wb') as file:
        file.write(response.content)

    # except requests.exceptions.HTTPError:
    #     print(f'Can not create book {filename}, it does not exist!')

    return filepath


# def check_for_redirect(response):
#     if response.history:
#         raise requests.exceptions.HTTPError


def main():
    url = 'http://tululu.org/txt.php?id=1'

    filepath = download_txt(url, 'Али\\би')
    print(filepath)  # Выведется books/Алиби.txt

    # dir_name = 'books'
    # for book_id in range(1, 11):
    #     Path(f'./{dir_name}').mkdir(parents=True, exist_ok=True)
    #     link_pattern = f'https://tululu.org/txt.php?id={book_id}'
    #     output = Path(f'./{dir_name}/id{book_id}.txt')
    #
    #     try:
    #         download_books(link_pattern, output)
    #     except requests.exceptions.HTTPError:
    #         print(f'Can not create book {output}, it does not exist!')


if __name__ == '__main__':
    main()
