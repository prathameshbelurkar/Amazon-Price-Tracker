import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

# ___________________________________VARIABLES AND CONSTAMTS__________________________________________________________

URL = "https://www.amazon.in/Crucial-Ballistix-Desktop-Gaming-BL2K16G30C15U4R/dp/B083TRRT1L/ref=sr_1_1_sspa?dchild=1&keywords=ddr4+ram+32gb+lamp&qid=1613274030&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyMTZCOUY0U0NZOVNWJmVuY3J5cHRlZElkPUEwNzE5MTkwM09ES1YyRTZONVgySCZlbmNyeXB0ZWRBZElkPUEwNzcxNjk2M1QyVkRaSjZKUUtaJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,fr;q=0.8",
}

SMTP = "smtp.gmail.com"
EMAIL = "prathamesh.belurkar@gmail.com"
PASSWORD = "Thi$_is_Prathamesh_Belurkar_@15"

# ___________________________GETTING THE RESPONSE________________________________________
response = requests.get(url=URL, headers=header)
web_page = response.text
soup = BeautifulSoup(web_page, "lxml")

# _________________________GETTING THE PRICE_______________________________
price_with_symbol = soup.find(name="span", class_="a-size-medium a-color-price priceBlockBuyingPriceString").getText()
updated_price = price_with_symbol.split()[1].split(",")
int_price = float(updated_price[0] + updated_price[1])
print(int_price)

if int_price <= 7600:
    message = f"The item you wanted to purchase. Now has a Price: {int_price} Rupees.\nWhy wait for...\n Buy Now."
    with smtplib.SMTP(SMTP, port=587) as connection:
        connection.starttls()
        result = connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs="prathameshb1236@gmail.com",
            msg=f"Subject: Amazon Price Alert!\n\n{message}\n\n{URL}",
        )