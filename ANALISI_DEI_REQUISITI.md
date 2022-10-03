# Analisi dei Requisiti

## Indice

1. Scopo del documento
2. Obiettivi del progetto
3. Requisiti Funzionali
4. Requisiti Non Funzionali
5. Front-End
6. Back-End

## 1. Scopo del documento

Il presente documento riporta l'analisi dei requisiti di sistema del progetto <!-- NOME PROGETTO --> in linguaggio naturale.
L'obiettivo di questo documento è quello di:

- presentare gli obiettivi del progetto;
- definire i requisiti funzionali e non funzionali;
- presentare il design e le funzionalità del Front-End;
- presentare i sistemi esterni con cui <!-- NOME PROGETTO --> si dovrà interfacciare (Back-End).

## 2. Obiettivi del progetto

Il progetto ha come obiettivo la realizzazione di un sito web per l'ordinazione di cibo take away, in grado di gestire menù, dettagli e le prenotazioni degli ordini di quei ristoranti che aderiscono.
Nello specifico <!-- NOME PROGETTO --> deve permettere i seguenti scenari:

- Visualizzare i ristoranti e ordinarli in base alle preferenze dell'utente;
- Gestione dell'autenticazione dei vari utenti;
- Visualizzare le informazioni e i menù di ogni ristorante
- Lasciar visualizzare all'utente anonimo la descrizione di ogni ristornate. Per la prenotazione online del cibo è obbligatorio essere autenticati;
- Personalizzazione delle pietanze;
- Gestione del carrello per un'eventuale modifica dell'ordine;
- Creare una sezione per i ristoranti preferiti.

- Opzionale: pagamento online (per adesso alla consegna);

## 3. Requisiti Funzionali

<!-- - Il progetto dovrà essere un sito web compatibile con i browser più comuni per desktop e dispositivi mobili (Google Chrome, Firefox, Safari, etc.); -->

- Il sistema di autenticazione funziona tramite "Autenticazione con Google" (account "@gmail.com" e "@studenti.unitn.it")
- Navigazione e calcolo della distanza con Google Maps
- Gli utenti si suddividono in 3 categorie:

  - _Utente anonimo_: può visualizzare i ristoranti con i rispettivi dettagli e menù
  - _Utente autenticato_: ha le stesse funzionalità dell'utente anonimo, inoltre può effettuare ordinazioni
  - _Utente autenticato (dominio "@studenti.unitn.it")_: ha le stesse funzionalità dell'utente autenticato, inoltre può ricevere degli "sconti studente" sui vari prodotti
  - _Responsabile ristorante_: può modificare le informazioni e il menù del ristorante, può gestire le ordinazioni

- Il sito dovrà provvedere le seguenti funzionalità:

  - L'_utente autenticato_ può effettuare una ordinazione, il _responsabile ristorante_ ha la possibilità di accettare o rifiutare l'ordine
  - I ristoranti possono essere suddivisi in base al nome o alla tipologia
  - Si può anche ricercare direttamente il nome del ristorante che si vuole visualizzare o tutti i ristoranti in una determinata zona
  - I ristoranti hanno una descrizione contenente orari di apertura, indirizzo, numero di telefono e menù
  - Una sezione dedicata ai propri ristoranti preferiti per una ricerca più rapida

- Sistema di ordinazione:

  - L'utente autenticato accede al menù, seleziona le pietanze che vuole
  - Nel menù di selezione è possibile personalizzare gli ingredienti
  - Una volta completato si invia al carrello
  - Nel carrello è presente un riepilogo dell'ordine
  - L'utente invia l'ordine
  - Viene ricevuto dal responsabile del ristorante il quale accetta o rifiuta l'ordinazione

## 4. Requisiti Non Funzionali

- Privacy: il sito deve rispettare la normativa GDPR
- Sicurezza: non vengono salvate password (perché viene usata l'autenticazione con Google), il sito deve essere https
- Scalabilità: il sito deve permettere la continua aggiunta e aggiornamento dei ristoranti
- Compatibilità: il sito deve essere compatibile con le ultime versioni dei browser più popolari (Google Chrome, Firefox, Safari, etc.), sia desktop che mobile
- Usabilità: l'utente deve essere in grado di usufruire di ogni funzionalità del sito in modo efficace e pratico (senza perdere tempo)
- Disponibilità: l'applicazione deve essere in grado di svolgere le proprie funzioni in un determinato lasso di tempo

## 5. Front-End

Nel seguente paragrafo vengono riportati alcune schermate del sito web da realizzare. Queste schermate hanno l'obiettivo di rappresentare come il sito web si dovrà presentare all'utente finale nel caso dei segueti rerquisiti funzionali descritti precedentemente:
- Schermata di autenticazione;
- Schermata con tutti i ristoranti
- Schermata del singolo ristorante
- Schermata del carrello


## 6. Back-End
