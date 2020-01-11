import urllib.request
from bs4 import BeautifulSoup
import SMS
import re

list_of_pages_to_scrape = ['https://ticket-website/single/SelectSeating.aspx?p=1&z=0',
                           'https://ticket-website/single/SelectSeating.aspx?p=2&z=0']


for quote_page in list_of_pages_to_scrape:
    # query the website and return the html to the variable page
    page = urllib.request.urlopen(quote_page).read()

    # parse the html using beautiful soup
    soup = BeautifulSoup(page, 'html.parser')

    # Search for the corresponding <div> element of the "sold out message" (which is already available)
    error_box = soup.find('div', attrs={'class': 'errDiv'})
    # the element of "available tickets" message taken from another performance
    seats_box = soup.find('div', attrs={'class': 'medium c2 tnew-selectseating-form-minqty-message tn-select-seating__min-qty-message'})
    if seats_box:
        seats_text = seats_box.text.strip()


    if error_box:
        error = error_box.text.strip()
        if 'sold out' in error:
            print(error)
        elif 'tickets left' in seats_text:
            # voila, there are some tickets left!
            number_of_seats = int(re.search(r'\d+', seats_text).group(0))
            # how many seats?
            if int(number_of_seats) > 1:
                # more than 1 seat is available, notify by sending a text message
                SMS.send(str(quote_page.replace('https://', '')))
        else:
            # something has changed on the website - worth checking
            SMS.send(str(quote_page.replace('https://', '')))
    elif 'tickets left' in seats_text:
        # print("tickets available!")
        number_of_seats = int(re.search(r'\d+', seats_text).group(0))
        print(seats_text)
        if int(number_of_seats)>1:
            # print('more than 1')
            SMS.send(str(quote_page.replace('https://', '')))
