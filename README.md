**Scrape Tickets Website**

Scrape a ticket website with a currently sold out performance until the new tickets appear, and get notified by sms when they do. 

Set the list of web pages to check in `list_of_pages_to_scrape` and your GMAIL credentials (required for using GMAIL SMTP server) and the phone number to send sms to in `.env`

run with cron scheduled every minute, saving the output log in cron_result.txt
```
* * * * * /opt/anaconda3/bin/python /Users/MyUser/PycharmProjects/scrape-tickets-website/scrape.py >> /Users/MyUser/PycharmProjects/scrape-tickets-website/cron_result.txt
```