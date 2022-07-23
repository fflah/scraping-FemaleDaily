import csv               
import random
import json
from datetime import datetime
import requests

def main(): 
    url = "https://reviews.femaledaily.com/api"
    payload={}
    result = []

    # get data form page 1-4
    for count in range(0, 4):
        headers = {
        'key': 'client03-hsjuebbbjasqqqivAAAbr-XkQQjannesQBlob',
        'version': '1.5',
        'device': '3',
        'endpoint': f'https://api.femaledaily.com/app/v1/reviews?product_slug=sun-protection-spf-30-pa&age_range_ids=&skin_type_ids=&skin_tone_ids=&skin_undertone_ids=&hair_texture_ids=&hair_type_ids=&sort=newest&limit=10&page={count+1}',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'if-none-match': 'W/"523f0-Hl5Fix7TIwRGgbKSpu0SxIjk6CI"',
        'te': 'trailers'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        raw = response.json()
        for data in raw['data']:
            date = datetime.strptime(data['created_at'], '%Y-%m-%dT%H:%M:%S.%f%z').strftime('%d-%m-%Y %I:%M %p')
            value = {
                'username profile': data['user']['username'], 
                'rate': data['rating'],
                'date': date,
                'reviews': data['text']
            }
            result.append(value)
    
    # save to csv    
    keys = result[0].keys()
    with open(f'data_review_femaleDaily.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(result)    
    print('finish')

if __name__ == '__main__':    
    main()