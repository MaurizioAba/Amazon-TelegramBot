from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from urllib.parse import urlparse, parse_qs
#from bitlyshortener import Shortener
import random
import requests

  # Initialize TinyURL API URL
tinyurl_api_url = "https://tinyurl.com/api-create.php"

# This function allow us to create an HTML message to send
# You can edit all fields of message using HTML syntax

# Funzione per creare il link di affiliazione abbreviato con Bitly
# def create_shortened_affiliate_link(long_url, bitly_token):
#     shortener = Shortener(tokens=[bitly_token])
#     short_url = shortener.shorten_urls([long_url])
#     return short_url[long_url]


def create_item_html(items):
    response = []
    print(f'{5 * "*"} Creating post {5 * "*"}')

    # Shuffling items
    random.shuffle(items)

    # Iterate over items
    for item in items:
        # If item has an active offer
        if 'off' in item:
            # Creating buy button
            # keyboard = [
            #     [InlineKeyboardButton("🛒 Acquista ora 🛒", callback_data='buy', url=item["url"])],
            # ]
            # reply_markup = InlineKeyboardMarkup(keyboard)

            # Creating message body

            html = ""
            html += f"🎁 <b>{item['title']}</b> 🎁\n\n"

            if 'description' in list(item.keys()):
                html += f"{item['description']}\n"

            html += f"<a href='{item['image']}'>&#8205</a>\n"

            if 'savings' in list(item.keys()):
                html += f"❌ Non più: {item['original_price']}€ ❌\n\n"

            html += f"💰 <b>Al prezzo di: {item['price']}</b> 💰\n\n"

            if 'savings' in list(item.keys()):
                html += f"✅ <b>Risparmi: {item['savings']}€</b> ✅\n\n"

            # Show the product link as text
           # html += f"<b>Link al prodotto:</b> {item['url']}"
            
            #ATTUALE
            
            # # Get the ASIN (Amazon Standard Identification Number) from the product URL
            # parsed_url = urlparse(item['url'])
            # if parsed_url.netloc == 'amzn.to':
            # #     # If the URL is an Amazon shortened link, extract the ASIN from the path
            #     asin = parsed_url.path.split("/")[-1]
            #     html += f"<b>Link al prodotto:</b> https://www.amazon.it/dp/{asin}"
            # else:
            #     # Otherwise, use the full product URL
            #     html += f"<b>Link al prodotto:</b> {item['url']}"
                
             # Abbrevia il link Amazon con TinyURL
            amazon_url = item['url']  # Link Amazon
            tinyurl_params = {"url": amazon_url}
            tinyurl_response = requests.get(tinyurl_api_url, params=tinyurl_params)

            if tinyurl_response.status_code == 200:
                shortened_url = tinyurl_response.text
                html += f"<b>Link al prodotto: 👉🏻 Amazon</b> {shortened_url}"
            else:
                html += f"<b>Link al prodotto:</b> {amazon_url}"

                
            # NUOVO TEST
            # Get the ASIN (Amazon Standard Identification Number) from the product URL
            # parsed_url = urlparse(item['url'])
            # asin = parsed_url.path.split("/")[-1]

            # Create the affiliate link with the tag and the ASIN
            # affiliate_link = f"https://www.amazon.it/dp/{asin}?tag={affiliate_tag}"
            
            # Shorten the affiliate link with Bitly
            # shortened_affiliate_link = create_shortened_affiliate_link(affiliate_link, bitly_token)
            
            # html += f"<b>Link al prodotto:</b> {shortened_affiliate_link}"
                
            #  # Get the ASIN (Amazon Standard Identification Number) from the product URL
            # asin = parse_qs(urlparse(item['url']).query).get('ASIN', [''])[0]

            # # Show the truncated product link with the ASIN
            # html += f"<b>Link al prodotto:</b> https://www.amazon.it/dp/{asin}"


            response.append(html)
            #response.append(reply_markup)
    return response
