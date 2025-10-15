# Kirjakerho


## Sovelluksen toiminnot :
* Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
* Käyttäjä pystyy luomaan kirjakerho tapahtumia sekä muokkaamaan ja poistamaan niitä.
* Käyttäjä näkee sovellukseen lisätyt tapahtumat.
* Käyttäjä pystyy etsimään tapahtumia hakusanalla. Haku kohdistuu paikka, otsikko, ja keskusteluhaihekenttiin.
* Käyttäjäsivu näyttää, montako tapahtumaa käyttäjä järjestää ja listan tapahtumista.
* Käyttäjä pystyy valitsemaan kirjakerhon tapahtumalle kahdesta luokasta: Laji (esim. Scifi, kauhu) ja teoksen tyyppi (esim. sarjakuvat/manga, novelli, romaani).
* Käyttäjä pystyy ilmoittautumaan kirjakerhon tapahtumaan. Ilmoituksessa näytetään, ketkä käyttäjät osallistuvat tapahtumaan.
* Tapahtuman järjestäjä aina automaattisesti osallistuu luomaansa tapahtumaan.
  

## Käyttöönotto :
Kloonaa repositorio

Luo projektihakemistossa virtuaalinen python ympäristö:

```
python -m venv venv

```

Aloita virtuaalinen python ympäristö:

```

.\venv\Scripts\Activate

``` 


Asenna Flask -kirjasto:

```
pip install flask

```

Alusta tietokanta tarvittavilla tauluilla. Lisää luokat tauluun.

```
sqlite3 database.db < schema.sql
sqlite3 database.db < init.sql

```

Käynnistä sovellus

```
flask run 

```

Nyt sovellusta voi testata osoitteessa:

```
http://127.0.0.1:5000/

```
