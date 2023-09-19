import requests
from bs4 import BeautifulSoup
import pandas as pd
base_url = 'https://www.olx.ua/uk/elektronika/tv-videotehnika/televizory/?currency=UAH&search%5Bfilter_enum_tv_type%5D%5B0%5D=pdp'
all_data = []
num_pages = 25
for page in range(1, num_pages + 1):
    url = f'{base_url}?page={page}'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        ads = soup.find_all('a', class_="css-rc5s2u")
        for ad in ads:
            title = ad.find('h6', class_="css-16v5mdi er34gjf0").text.strip()
            price = ad.find('p', class_="css-10b0gli er34gjf0").text.strip()
            link = ad['href']
            klo = 'olx.ua' + link
            all_data.append({'Название': title, 'Цена': price, 'Ссылка': klo})
    else:
        print(f'Не удалось получить доступ к странице {page}')
df = pd.DataFrame(all_data)
septaor = ";"
encoding = 'cp1251'
# Сохраняем данные в CSV-файл
df.to_csv('C:/User/Andrey/nast parser/OlX-parser.csv', index=False, sep=septaor, encoding=encoding)
print('Данные успешно сохранены в olx_data.csv')