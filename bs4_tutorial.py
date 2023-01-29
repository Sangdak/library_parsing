import requests
from bs4 import BeautifulSoup


#url = 'https://www.franksonnenbergonline.com/blog/are-you-grateful/'
url = 'https://tululu.org/b1/'
response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'lxml')
# print(soup.prettify())
title_tag = soup.find('body').find('table').find('td', class_='ow_px_td').find('div').find('h1').text
title_tag = title_tag.split('   ::   ')

title_tag[0].strip()
title_tag[1].strip()
print(title_tag)

# title_text = title_tag.text
# print(title_text)

# img_url = soup.find('img', class_='attachment-post-image')['src']
# print(img_url)
#
# post_text = soup.find('div', class_='entry-content')
# print(post_text.text)
