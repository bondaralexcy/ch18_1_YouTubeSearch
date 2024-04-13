import os

from src.utils import get_youtube_data, create_database, save_data_to_database
from config import config


def main():
    # api_key = os.getenv('YT_API_KEY')
    api_key = 'AIzaSyCT9YpKoMjsVWNiCwC1TeskAm_PCbEAuVM'
    channel_ids = [
        # 'UC-OVMPlMA3-YCIeg4z5z23A',  # moscowpython
        # 'UCwHL6WHUarjGfUM_586me8w',  # highload
        'UC4NQG2u8P7t29T3aSxmGrTQ'   # metametrika
    ]
    params = config()

    data = get_youtube_data(api_key, channel_ids)
    print(data)
    create_database('youtube', params)
    save_data_to_database(data, 'youtube', params)


if __name__ == '__main__':
    main()
