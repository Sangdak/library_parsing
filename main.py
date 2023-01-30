import os
import requests
from pathlib import Path
from pathvalidate import sanitize_filename
from bs4 import BeautifulSoup
from urllib.parse import unquote, urljoin, urlparse


def download_txt(url, filename, number, folder='books/'):
    """Функция для скачивания текстовых файлов.
        Args:
            url (str): Cсылка на текст, который хочется скачать.
            filename (str): Имя файла, с которым сохранять.
            folder (str): Папка, куда сохранять. По умолчанию "books/"
        Returns:
            str: Путь до файла, куда сохранён текст.
        """
    Path(f'./{folder}').mkdir(parents=True, exist_ok=True)
    filename = sanitize_filename(filename)
    filepath = Path(f'./{folder}/{number}.{filename}.txt')

    response = requests.get(url)
    response.raise_for_status()

    check_for_redirect(response)

    with open(filepath, 'wb') as file:
        file.write(response.content)

    return filepath


def download_book_cover(cover_img_url, folder='images/'):
    """Функция для скачивания изображений обложек книг.
        Args:
            cover_img_url (str): Cсылка на изображение обложки, которое хочется скачать.
            # filename (str): Имя файла, с которым сохранять.
            folder (str): Папка, куда сохранять. По умолчанию "images/"
        # Returns:
        #     str: Путь до файла, куда сохранёна обложка.
        """
    Path(f'./{folder}').mkdir(parents=True, exist_ok=True)
    filename = unquote(urlparse(cover_img_url).path.split('/')[-1])
    filename = sanitize_filename(filename)
    filepath = Path(f'./{folder}/{filename}')

    response = requests.get(cover_img_url)
    response.raise_for_status()

    check_for_redirect(response)

    with open(filepath, 'wb') as file:
        file.write(response.content)

    # return filepath


def fetch_title_n_author_name_n_book_cover_url(page_url):
    response = requests.get(page_url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'lxml')
    title_name_tag = soup.find('body').find('table').find('td', class_='ow_px_td').find('div').find('h1').text
    title_name_tag = title_name_tag.split('   ::   ')

    image_tag = soup.find('div', class_='bookimage').find('img')['src']

    title_tag = title_name_tag[0].strip()
    author_tag = title_name_tag[1].strip()
    return title_tag, image_tag


def check_for_redirect(response):
    if response.history:
        raise requests.exceptions.HTTPError


def main():
    site_url = 'https://tululu.org/'
    for book_id in range(1, 11):
        try:
            url_pattern = urljoin(site_url, f'/txt.php?id={book_id}')
            page_url_pattern = urljoin(site_url, f'/b{book_id}')
            filename, book_cover_url = fetch_title_n_author_name_n_book_cover_url(page_url_pattern)
            book_cover_url = urljoin(site_url, book_cover_url)
            print(book_cover_url)

            # download_txt(url_pattern, filename, book_id)
            download_book_cover(book_cover_url)


        except requests.exceptions.HTTPError:
            print(f"Can't create book {filename}, it does not exist!")
        except IndexError:
            print(f"Can't create book {filename}, it does not exist!")
        except AttributeError:
            print(f"Can't create book {filename}, it does not exist!")


if __name__ == '__main__':
    main()
