#!/usr/bin/env python3
import requests
import os
import shutil
import subprocess

REGION = "ru-RU"
BASE_URL = f"https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt={REGION}"
BASE_PATH = "/home/kernelpanicattack/Изображения/backgrounds/"
CURRENT_BACKGROUND = os.path.join(BASE_PATH, "current.jpg")

os.makedirs(BASE_PATH, exist_ok=True)

headers = {"User-Agent": "Mozilla/5.0"}

# Получаем JSON с данными обоев
resp = requests.get(BASE_URL, headers=headers, timeout=10)
resp.raise_for_status()
data = resp.json()

# Собираем URL картинки
img_url = "https://www.bing.com" + data["images"][0]["url"]
filename = os.path.join(BASE_PATH, os.path.basename(img_url.split("&")[0]))

# Скачиваем
with requests.get(img_url, stream=True, timeout=20, headers=headers) as r:
    r.raise_for_status()
    with open(filename, "wb") as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)

# Обновляем current.jpg
shutil.copy(filename, CURRENT_BACKGROUND)

# Перезапускаем hyprpaper (чтобы подхватил новое current.jpg)
subprocess.run(["pkill", "hyprpaper"])
subprocess.Popen(["hyprpaper"])
