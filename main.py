import smtplib
import ssl
import requests

api_key = "c9d7096f94d24761a072b21755b909e9"
url = f"https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={api_key}"

# Make request
request = requests.get(url)
contents = request.json()


# Access the article titles and description
def send_mail(message):
    host = "smtp.gmail.com"
    port = 465

    username = "jim.otieno.09@gmail.com"
    password = "hqroyqomrrfrxjhy"

    receiver = "jim.otieno.09@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


# Write email content and format
content_ = "Subject: Today in the tech world"
for content in contents["articles"][:50]:
    content_ += "\n" + str(content["title"]) \
                + "\n" + str(content["description"]) \
                + "\n" + str(content["url"]) + 2 * "\n"

body = content_.encode("utf-8")
send_mail(body)
