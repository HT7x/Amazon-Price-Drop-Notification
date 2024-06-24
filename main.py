import requests
from bs4 import BeautifulSoup
import lxml
import json
import yagmail
import logging


######### Change only this section #########
# Add the url and the corresponding threshhold price for the amazon product, comma separated (The two products are examples)
url_price = {
    "https://a.co/d/0dlwWeDl" : 30, 
    "https://a.co/d/0irn96jy" : 60
}
# email address you want to recieve the notification from
rec_email = ht.bh@live.com
############################################


logging.basicConfig(filename='output.log', 
                    level=logging.DEBUG, 
                    format='%(asctime)s %(levelname)s %(message)s')

def load_config(file_path):
    with open(file_path, 'r') as config_file:
        config = json.load(config_file)
    return config


def send_email_yagmail(sender_email, receiver_email, subject, body, password):
    try:
        yag = yagmail.SMTP(sender_email, password)
        yag.send(
            to=receiver_email,
            subject=subject,
            contents=body
        )
        logging.info("Email sent successfully")
    except Exception as e:
        logging.error(f"Failed to send email: {e}")


headers = { 'Accept-Language' : "en-US,en;q=0.9",
            'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35"}


config_path = 'config.json'
config = load_config(config_path)

YOUR_EMAIL_email = config['email']
YOUR_PASSWORD = config['password']

for url, price_buy in url_price.items():
    while True:
        response = requests.get(url, headers=headers)
        logging.info(response)
        soup = BeautifulSoup(response.content, "lxml")
        price_data = soup.find("span", class_="a-offscreen")
        
        if price_data is not None:
            price = price_data.getText()

            if len(price.split("$")) > 1:
                break 

    split_price = float(price.split("$")[1])
    logging.info(split_price)

    title = soup.find(id="productTitle").get_text().strip()

    if split_price <= price_buy:
        logging.info("BUY NOW, price is at: " + price + "\n")
        message = f"{title} is now {price}"

        send_email_yagmail(
            sender_email=YOUR_EMAIL_email,
            receiver_email=rec_email,
            subject=message,
            body="Buy Now https://a.co/d/0dBRPLJX",
            password=YOUR_PASSWORD
        )
    else:
        logging.info("Don't Buy yet, price is at: " + price + "\n")




