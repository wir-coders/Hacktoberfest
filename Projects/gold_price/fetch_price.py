from requests import get
from datetime import datetime as now
from bs4 import BeautifulSoup as Soup


PARSER = 'html.parser'
TAG_1 = "div"
DIV_CLASS = "row mb-10 g-rate-box"
TAG_GOLD = 'span'
CLASS_ID = 'id'
CLASS_CLASS = 'class'
SPAN_24K = "lblrate24K"
SPAN_22K = "lblrate22K"
STRF_TIME = "%d-%m-%y %H:%M  GMT +5:30" \
            " Asia/Kolkata"


class GoldPrice:
    
    def __init__(self):
        self.url = 'https://ibjarates.com/'
    
    # Returns Beautiful Soup Object
    def make_soup(self):
        data = get(self.url)
        soup = Soup(data.text, PARSER)
    
        get_data = soup.find(TAG_1,
                             {CLASS_CLASS: DIV_CLASS})
        
        return get_data
    
    # Returns Current Time and with Timezone in IST.
    def get_time(self):
        date_time_now = now.now()
        date_time_now = date_time_now.strftime(STRF_TIME)
        date_time_now = str(date_time_now)
        
        return date_time_now
        
    # Assemble data & Return Price as response.
    def fetch_data(self):
        
        get_data = self.make_soup()
        rate_24_k = get_data.find(TAG_GOLD,
                                  {CLASS_ID: SPAN_24K}).get_text()
        rate_22_k = get_data.find(TAG_GOLD,
                                  {CLASS_ID: SPAN_22K}).get_text()
        
        response = {
            'current_time': self.get_time(),
            '24_karat_price': rate_24_k,
            '22_karat_price': rate_22_k,
            }
        
        return response
        
        
if __name__ == '__main__':
    gp = GoldPrice()
    result = gp.fetch_data()
    print(result)
