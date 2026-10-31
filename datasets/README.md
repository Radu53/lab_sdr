# Dataset: Carti bestseller de pe Amazon

## Descriere

Dataset-ul contine o colectie de informatii despre carti alese pentru a fi folosite in sisteme de recomandare si dezvoltare de chatbot-uri. Pentru fiecare inregistrare sunt disponibile codurile ISBN (International standard book number) de 13 si 10 cifre pentru identificare si date descriptive precum titlul, subtitlul, autori, categorii, anul publicarii si media recenziilor.

## Sursa datelor

Dataset-ul a fost descarcat de pe [Kaggle](https://www.kaggle.com/datasets/abdallahwagih/books-dataset) si este disponibil in fisierul `datasets/bestsellers.csv`.

## Structura dataset-ului

Fisierul este in format CSV si contine urmatoarele coloane:

| Coloana | Tip de date | Descriere |
| --- | --- | --- |
| title | string | Titlul cartii |
| subtitle | string | Subtitlul cartii |
| authors | string | Autorii cartii |
| categories | string | Categoria cartii |
| description | string | Descrierea cartii |
| published_year | int | Anul publicarii |
| average_rating | int | Nota medie a recenziilor |
| ratings_count | int | Numarul de recenzii |
| num_pages | int | Numarul de pagini |

## Exemple de inregistrari

| isbn13 | isbn10 | title | subtitle | authors | cathegories | thumbnail | description | published_year | average_rating | num_pages | ratings_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
9780002005883 | 0002005883 | Gilead |  | Marilynne Robinson | Fiction | http://books.google.com/books/content?id=KQZCPgAACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api | "A NOVEL THAT READERS and critics have ..." | 2004 | 3.85 | 247 | 361
9780002261982 | 0002261987 | Spider's Web | A Novel | Charles Osborne;Agatha Christie | Detective and mystery stories | http://books.google.com/books/content?id=gA5GPgAACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api | "A new 'Christie for Christmas' -- a full-length ..." | 2000 | 3.83 | 241 | 5164
9780006163831 | 0006163831 | The One Tree |  | Stephen R. Donaldson | American fiction | http://books.google.com/books/content?id=OmQawwEACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api | Volume Two of Stephen Donaldson's acclaimed ... | 1982 | 3.97 | 479 | 172

## Utilizarea in sistemul de recomandare

Proprietatile disponibile permit descrierea cartilor si generarea de recomandari pe baza unor caracteristici precum autorul, categoria sau nota recenzii.

Dupa adaugarea interactiunilor utilizatorilor, precum vizualizari sau evaluari, sistemul poate genera recomandari personalizate.
