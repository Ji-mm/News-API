import os
import smtplib
import ssl

import requests

api_key = "c9d7096f94d24761a072b21755b909e9"
url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&api" \
      "Key=c9d7096f94d24761a072b21755b909e9"

# Make request
request = requests.get(url)
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    if article["title"] and article["description"] is not None:
        article1 = article["title"] + "\n" + article["description"] + 2 * "\n"


def send_mail(message):
    host = "smtp.gmail.com"
    port = 465

    username = "jim.otieno.09@gmail.com"
    password = os.getenv("PASSWORD")

    receiver = "jim.otieno.09@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


article3 = article1.encode("utf-8")
send_mail(article3)
