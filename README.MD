# Python Fulbacho API Wrapper

Fulbacho Python API Wrapper to use with resultados-futbol.com .
Tested on Python 3.6

[Go to resultados-futbol](http://www.resultados-futbol.com/)

## Dev Setup

Install the libs

    pip install -r requirements.txt

Rename .env.example > .env

The File fulbacho.ini will be created at the initilization config.

When you start it the app create a file called fulbacho.ini

## Installation

    pip install git+https://github.com/villadalmine/fulbacho.git

## Usage

Setup (APITOKEN requiered):

    import fulbacho
    from fulbacho import fulbacho
    from fulbacho.fulbacho import Fulbacho
    futbol = Fulbacho()
    futbol.initialize_config()
    #List loaded leagues
    fulbol.getListOfLeagues()
    #Get info of a country
    futbol.getLeaguesInfo("Argentina")
    #Get info of a league
    futbol.getInfoLeague("33424")


Resultados-Futbol  API Doc:
[http://www.resultados-futbol.com/api](http://www.resultados-futbol.com/api)

## Unit Test

Go to test directory and run

## TO-DO

--- IMPORTANT ---
* CHECK HOW TO RELOAD CONFIG fulbacho.ini

* Function get_url_status neet to be checked because one previous error on the api was saved in headers of response and faill all.

--- TO INTEGRATE WITH BOT ---

* Make a function to show all data of a specific League

## Licence

The MIT License (MIT)

Copyright (c) 2016 Felipe Aránguiz | Sebastián Aránguiz

See [LICENSE](LICENSE)

## Based on

[scottjbarr/bitfinex](https://github.com/scottjbarr/bitfinex)

[delta575/python-surbtc-api](https://github.com/delta575/python-surbtc-api)

[architv/soccer-cli](https://github.com/architv/soccer-cli)
