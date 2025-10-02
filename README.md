# Kirjakerho


## Kirjakerhosovellus :
* Sovelluksessa käyttäjät pystyvät etsimään kirjakerhon tapahtumia jossa keskustellaan kirjoista. Ilmoituksessa lukee missä ja milloin kerhoa vietetään, tapahtuman keskusteluaiheen, sekä tiedot oleellisista luokista: teoksen lajista ja tyypistä.
* Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
* Käyttäjä pystyy luomaan ommia kirjakerho tapahtumia sekä muokkaamaan ja poistamaan niitä, kunhan on luonut tunnuksen ja on kirjautunut sisään.
* Käyttäjä näkee sovellukseen lisätyt tapahtumat.
* Käyttäjä pystyy etsimään ilmoituksia hakusanalla. Haku kohdistuu paikka-, otsikko-, ja keskusteluhaihekenttiin.
* Käyttäjäsivu näyttää, montako tapahtumaa käyttäjä järjestää ja listan tapahtumista.
* Käyttäjä pystyy valitsemaan kirjakerhon tapahtumalle kahdesta luokasta: Laji (esim. Scifi, kauhu) ja teoksen tyyppi (esim. sarjakuvat/manga, novelli, romaani).
* Käyttäjä pystyy ilmoittautumaan kirjakerhon tapahtumaan. Ilmoituksessa näytetään, ketkä käyttäjät osallistuvat tapahtumaan.
* Tapahtuman järjestäjä aina automaattisesti osallistuu luomaansa tapahtumaan.

## Käyttöönotto :
* Kloonaa repositorio
* Aloita Kirjakerhon hakemistossa virtuaalinen python ympäristö: venv\Scripts\activate (windows).
* Luo sovelluksen tarvitsema tietokanta: sqlite3 database.db < schema.sql.
* Aloita sovellus: flask run.
* Navigoi url-linkin kautta testaamaan sovellusta.
* Jotta sovelluksen toimintojen testaaminen onnistuu, on listättävä tietokantaan ensin tietokohteita.
* Ensin, tee käyttäjä ja kirjaudu sisään.
* Sisäänkirjautuneena on mahdollista järjestää kirjakerhon tapahtumia.
* Sovelluksen tapahtumiin on mahdollista valita otsikko, aika, paikka, kirjan laji ja teoksen tyyppi.
* Tämän lisäksi laatikkoon voi kirjoittaa laajemmin tapahtuman keskusteluaiheesta tai ohjelmasta.
* Omia ilmoituksia on mahdollista muokata ja poistaa.
* Tapahtumia on mahdollista hakea hakusanalla.
* Etusivulta voi katsoa luotuja tapahtumia, ja linkkiä klikaamalla on mahdollista tarkastaa sen tarkempia tietoja.

