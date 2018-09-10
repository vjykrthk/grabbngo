import requests
import traceback
import csv


def call_store_menu_api():
    store_id = '522fe98a-4c8a-4695-9fb3-505d45656984'
    store_menu_api = 'https://www.ubereats.com/en-IN/rtapi/eats/v2/eater-store'
    url = '{}/{}'.format(store_menu_api, store_id)
    return requests.get(url)


def construct_menu_csv(store_menu_info):
    store_sections = store_menu_info['store']['sections']
    with open('menu_items.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(
            ['Title', 'Description', 'Price', 'ImageUrl'])
        for ss in store_sections:
            for uuid, menu_item in store_menu_info['store']['sectionEntitiesMap'][ss['uuid']]['itemsMap'].items():
                image_url = menu_item['imageUrl'] if 'imageUrl' in menu_item else None
                filewriter.writerow(
                    [menu_item['title'], menu_item['itemDescription'], menu_item['price'], image_url])


def get_menu_items():
    try:
        response = call_store_menu_api()
        if response.status_code == 200:
            store_menu_info = response.json()
            construct_menu_csv(store_menu_info)
    except Exception as e:
        print(traceback.format_exc())


if __name__ == '__main__':
    get_menu_items()
