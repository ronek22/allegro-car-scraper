# Allegro car offers scraper
## About project
Project consists of two seperate programs
### [Allegro REST (.NET CORE)](AllegroREST/AllegroREST)
My goal is to scrap all car offers from allegro and group results by dealer. 
Dealer should store data about nickname, link, average_price, average_production_year
I ran immediately into problems, because allegro in new api doesn't provide endpoints for ***details of given offer*** and ***details of user based on his id*** So in this app I just implement authorization (luckily it can be used in webapi) and downloading all offers(offerId, offerTitle, price)
### [Allegro Web Api (Python)](AllegroWebApi)
Firstly, after authorized in REST, you need to manualy copy *secret.json* to webapi project folder(if token expired, you need to refresh it in REST).
Web Api provide endpoints for getting details about offer, this endpoint also return data about nickname so it's all i ever wanted. Also you need to copy *data_without_grouping.json* from REST. I also added multithreading to speed up, because on single thread takes 4 hours to complete, after changes it only requires ~4 minutes, so it's big improvement.

## TODO
* Write script to automatically run two programs 
* Export result to xsl instead of csv
