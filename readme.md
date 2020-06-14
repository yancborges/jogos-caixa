## Jogos caixa

This code is meant to be a scrapper from Caixa economica games,
like lotofácil, quina and mega-sena.

A friend asked me if i could store them somewhere for
doing some cool statistics, so, i made this code

### Loader class

This class goes to the url for the wanted game
and download the data

`load = Loader('lotofacil')`

The **data** attribute has a pandas dataframe with scrapped values
It is mounted with the reader class

### Reader class

This class has the work of cleaning and organizing
the data withtin the html files downloaded.

The class recieves a html text as instancing parameter
`analyse = Lotofacil(load.data)'

The function **read** does the job of parsing things to
json and pandas format

### Analyser classes

Here is where the cool mathematical stuff appears.
With the data collected and organized, my friend
says some things we can do with the data, then i write it's function

The **results** property returns the occurencies for each value
in the downloaded history.

Each game needs a exclusive class implemented, since they have
different rules and different analysations

### Games implemented:

- Lotofácil

