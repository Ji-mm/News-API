import os
import smtplib
import ssl
import requests

topic = "samsung"
api_key = "c9d7096f94d24761a072b21755b909e9"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&from=2023-01-03&sortBy=publishedAt&" \
      "apiKey=c9d7096f94d24761a072b21755b909e9&" \
      "language=en"

# Make request
request = requests.get(url)
contents = request.json()


# Access the article titles and description

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


content_ = "Subject: Today in the tech world"
for content in contents["articles"][:20]:
    content_ += "\n" + str(content["title"]) \
                + "\n" + str(content["description"]) \
                + "\n" + str(content["url"]) + 2 * "\n"

body = content_.encode("utf-8")
send_mail(body)
