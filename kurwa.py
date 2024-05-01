from bs4 import BeautifulSoup

soup = BeautifulSoup(xml_data, 'xml')

# Создаем пустой словарь для хранения данных
data_dict = {}

# Ищем все теги <url>
urls = soup.find_all('url')

# Проходимся по найденным тегам и извлекаем данные
for url in urls:
    loc = url.find('loc').text
    lang_code = loc.split('/')[3]
    page_type = loc.split('/')[4] if len(loc.split('/')) > 4 else 'base_page'
    if lang_code not in data_dict:
        data_dict[lang_code] = {}
    data_dict[lang_code][page_type] = loc

print(data_dict)