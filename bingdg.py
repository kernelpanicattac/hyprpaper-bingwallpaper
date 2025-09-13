#!/usr/bin/env python3
import requests
import os
import shutil
import subprocess

# Настройки
REGION = "ru-RU"
BASE_URL = f"https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt={REGION}"
BASE_PATH = "/home/kernelpanicattack/Изображения/backgrounds/"
CURRENT_BACKGROUND = os.path.join(BASE_PATH, "current.jpg")

# Создаём папку, если её нет
os.makedirs(BASE_PATH, exist_ok=True)

headers = {"User-Agent": "Mozilla/5.0"}

# Получаем JSON с информацией об обоях
resp = requests.get(BASE_URL, headers=headers, timeout=10)
resp.raise_for_status()
data = resp.json()

# Базовый URL картинки без параметров
base_img_url = "https://www.bing.com" + data["images"][0]["url"].split("&")[0]

# Список разрешений в порядке приоритета
resolutions = ["_UHD", "_2560x1440", "_1920x1080", "_1366x768"]

# Ищем первое существующее разрешение
for suffix in resolutions:
    img_url = base_img_url.rsplit("_", 1)[0] + suffix + ".jpg"
    r = requests.head(img_url, headers=headers)
    if r.status_code == 200:
        break
else:
    raise Exception("Не удалось найти рабочее разрешение изображения")

# Скачиваем найденное изображение
filename = os.path.join(BASE_PATH, os.path.basename(img_url))
with requests.get(img_url, stream=True, timeout=20, headers=headers) as r:
    r.raise_for_status()
    with open(filename, "wb") as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)

# Копируем в current.jpg для hyprpaper
shutil.copy(filename, CURRENT_BACKGROUND)

# Перезапускаем hyprpaper, чтобы подхватил новые обои
subprocess.run(["pkill", "hyprpaper"])
subprocess.Popen(["hyprpaper"])

print(f"Скачано изображение: {filename}")
print(f"Используется как current.jpg для hyprpaper")
