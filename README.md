# Kirjakerho


## Välipalautus 1 :
* Sovelluksessa käyttäjät pystyvät etsimään Luku kerhoa jossa keskustellaan kirjoista. Ilmoituksessa lukee missä ja milloin kerhoa vietetään sekä tapahtuman keskusteluaiheen.
* Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
* Käyttäjä pystyy lisäämään ilmoituksia järjestämistään kirjakerho tapahtumista, sekä muokkaamaan ja poistamaan niitä.
* Käyttäjä näkee sovellukseen lisätyt ilmoitukset.
* Käyttäjä pystyy etsimään ilmoituksia ajankohdan tai paikan,ja aiheen perusteella.
* Käyttäjäsivu näyttää, montako ilmoitusta käyttäjä on lähettänyt ja listan ilmoituksista.
* Käyttäjä pystyy valitsemaan ilmoitukselle yhden tai useamman luokittelun (esim. Aika-ja paikkatiedot,Kirjan teema, Kirjan tyyppi(sarjakuvat,Novellit,Romaanit).
* Käyttäjä pystyy ilmoittautumaan kerhoiltaan. Ilmoituksessa näytetään, ketkä käyttäjät ovat ilmoittautuneet.

## Välipalautus 2 (Käyttöönotto):
*Kloonaa repositorio
*Aloita Kirjakerhon hakemistossa virtuaalinen python ympäristö: venv\Scripts\activate (windows)
*Luo sovelluksen tarvitsema tietokanta: sqlite3 database.db < schema.sql
*Aloita sovellus: flask run
*Navigoi url linkin kautta testaamaan sovellusta

*Jotta sovelluksen toimintojen testaaminen onnistuu, on listättävä tietokantaan ensin tietokohteita
*Ensin, tee käyttäjä ja kirjaudu sisään
*Sisäänkirjautuneena on mahdollista järjestää kirjakerhon tapahtumia
*Sovelluksen tapahtumiin on mahdollista valita otsikko, aika, paikka, kirjan teema ja kirjan tyyppi
*Tämän lisäksi laatikkoon voi kirjoittaa laajemmin tapahtuman keskusteluaiheesta tai ohjelmasta
*Omia ilmoituksia pitäisi olla mahdollista muokata ja poistaa
*Tapahtumia on mahdollista hakea Aiheen tai paikan perusteella
*Etusivulta voi katsoa luotuja tapahtumia, ja linkkiä klikaamalla on mahdollista tarkastaa sen tarkempia tietoja.

