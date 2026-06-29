Enter ```python
import requests

def check_m3u(input_file, output_file):
with open(input_file, 'r', encoding='utf-8') as f:
lines = f.readlines()

with open(output_file, 'w', encoding='utf-8') as f:
for i in range(len(lines)):
line = lines[i].strip()
# Проверяем, является ли строка ссылкой на поток
if line.startswith("http"):
try:
# Делаем быстрый запрос (только заголовки, чтобы не качать весь поток)
response = requests.head(line, timeout=5, allow_redirects=True)
if response.status_code == 200:
f.write(line + "\n") # Ссылка рабочая, пишем в файл
except:
print(f"Канал не работает: {line}")
else:
f.write(line + "\n") # Пишем название канала (#EXTINF...)

check_m3u('Сармат ТВ.m3u', 'Сармат ТВ_new.m3u')
```
