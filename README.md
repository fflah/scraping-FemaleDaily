# Scraping Data Review femaledaily.com

## Url page: https://reviews.femaledaily.com/products/moisturizer/sun-protection-44/emina/sun-protection-spf-30-pa?cat=&cat_id=0&age_range=&skin_type=&skin_tone=&skin_undertone=&hair_texture=&hair_type=&order=newest&page=1
</br>

## Nomenklatur Dataset ##
Atribut       | Penjelasan
------------- | -------------
username profile         | nama user yang memberikan review
rate         | rate yang diberikan pada produk
date       | tanggal terbit review
review       | isi text review

## Setup run.py ##

- Buat virtual environment -> python -m venv env
- Activate environment -> source env/bin/activate (linux dan mac)
- Install requirement.txt ->  pip install -r requirements.txt
- Jalankan scraping_eprint_ums.py -> python run.py 