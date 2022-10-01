
# Torrent Scrapper API

An API to Scrap Magnet/Torrent Links from 1337x, It provides the top seeded result from your query. Scrapping is done using [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) and [Python3](https://www.python.org/). API is hosted on [Heroku](heroku.com).


## Demo
#### API 
https://tscrap.herokuapp.com/
#### Web App
https://magnet-s.vercel.app/
#### Telegram Bot
[Magnet Scrapper BOT](https://t.me/magnetscrapperbot)



## API Reference

#### Get sites available

```http
GET /sites

"No Parameters"
```

#### Search a site for torrents

```http
GET /torrents

Parameters:
  {
    "key" : "key",
    "safe" : true
  }
```

#### Get magnet link and file list

```http
GET /torrents

Parameters:
  {"link" : "link"}
```



## API Examples and Demos

### Try this examples in your system

#### Getting List of sites

https://tscrap.herokuapp.com/sites

#### Returns JSON

```
[
  {
    "id": 1,
    "name": "1337x"
  }
]
```

#### Searching 1337x for Linux torrents

https://tscrap.herokuapp.com/torrents?key=ubuntu

#### Returns JSON

```
[
  {
    "name": "Ubuntu MATE 16.04.2 [MATE][armhf][img.xz][Uzerus]",
    "url": "https://www.1377x.to//torrent/2099267/Ubuntu-MATE-16-04-2-MATE-armhf-img-xz-Uzerus/",
    "seeds": "260",
    "leeches": "2",
    "date": "Apr. 28th '17",
    "size": "1.1 GB",
    "uploader": "Uzerus\n"
  },
  {
    "name": "Ubuntu Linux Unleashed 2021 Edition, 14th Edition",
    "url": "https://www.1377x.to//torrent/4814893/Ubuntu-Linux-Unleashed-2021-Edition-14th-Edition/",
    "seeds": "111",
    "leeches": "9",
    "date": "Mar. 23rd '21",
    "size": "84.2 MB",
    "uploader": "rootmk\n"
  },
  ...
]
```

#### Geting magnet link and file list

https://tscrap.herokuapp.com/magnet?link=https://www.1377x.to//torrent/2099267/Ubuntu-MATE-16-04-2-MATE-armhf-img-xz-Uzerus

#### Returns JSON

```
{
  "magnet": "magnet:?xt=urn:btih:D0F23C109D8662A3FE93.....Fannounce",
  "files": [
    "ubuntu-mate-16.04.2-desktop-armhf-raspberry-pi.img.xz (1.1 GB)"
  ]
}
```
## Run Locally

Clone the project

```bash
git clone https://github.com/kishanmodi/Torrent-Scrapper-API
```

Go to the project directory

```bash
cd Torrent-Scrapper-API
```

Install dependencies

```bash
pip3 install -r requirements.txt
```

Start the server (with given run script)

```bash
./run
```

(else) Start the server manually

```bash
FLASK_APP=app.py
FLASK_ENV=development
flask run
```

Access it using
```
http://server-ip:port/api
```


## Deployment
[![Deploy](https://www.herokucdn.com/deploy/button.svg "Deploy to Heroku")](https://heroku.com/deploy?template=https://github.com/kishanmodi/Torrent-Scrapper-API/main)

To deploy this project on heroku run

#### Login to Heroku
```bash
heroku login
```

#### create a new app on Heroku
```bash
git init
heroku git:remote -a your-app-name
```

#### commit your changes
```bash
git add .
git commit -m'initial changes'
git push heroku main
```

#### Access your app on
```
  https://your-app-name.herokuapp.com
```


## Acknowledgements

 - [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
 - [Heroku](https://readme.so/heroku.com)
 - [Sameer Bidi - Project Reference](https://github.com/SameerBidi)

