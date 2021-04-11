import sys
import time
from pathlib import Path

from selenium.common import exceptions as EXCPT

# BASE_PATH = Path(__file__).resolve().parent.parent.parent
# sys.path.append(str(BASE_PATH))
# print(sys.path)

from rumah123.scrapper.rumah123 import Rumah123Scrapper
from rumah123.settings import HOME_PAGE, RECOMMEND_CSS, NEW_PROPERTY_CSS_SELECTORS
from rumah123.items import Item
from HomeScrapperSelenium.Scrapper import Scrapper, DriverType

START_URL = HOME_PAGE

if __name__ == '__main__':
    print("init main")
    print("OS platform:",sys.platform)

    rumah123 = Rumah123Scrapper(DriverType.CHROME,START_URL)
        
    time.sleep(5)
    rumah123.get_by_location("Jawa Barat")
    # rumah123.get_recommends()
    # populars = rumah123.get_populars()
    # rumah123.save_to_file(rumah123.toJson(populars),
    #     str(Path(__file__).resolve().parent),
    #     filename="json_raw.json")
