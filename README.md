## INDICE

<!-- TODO -->

## Scopo del documento

```
Il presente documento riporta l'analisi di sitstema del progetto "...":
-
-
-
-
-
```

## IDEE

### Ristoranti tutti nello stesso sito Web

Sito web con un menù di ogni ristorante che aderisce. Premendo su un ristorante -> visualizzi il menù e, se aderisce, prenotazione del tavolo online. Sta ai gestori mettere all'interno del sito i tavoli già prenotati da chiamate.
Utente anonimo può visualizzare tutto, ma non può prenotare il tavolo.
Utente deve loggarsi e può farlo tramite google, facebook, etc...
Tasto di ricerca con cui puoi cercare il ristorante in base a:

- Nome
- Luogo
- Tipologia

Premendo su un ristorante vai alla pagina dettagli -> All'interno c'è la pagina menù -> Per chi aderisce prenotazione tavoli

**DA CHIEDERE -> implemetazione parte dei panini**

### PranzoTN

#### Obiettivi del progetto

Il progetto PranzoTN consiste nello sviluppo di un sito web con lo scopo di permettere ad attività di ristorazione di avere un portale web dove gli studenti dell'univeristà di Trento possono visualizzare i loro menù e fare ordinazioni. Il sito permette all'utente anonimo di visualizzare i menù di ogni ristorante, mentre l'utente loggato può aggiungere al carrello e modificare ogni ordine.
Nello specifico:

- Trattenere dagli acquisti una commissione che verrà utilizzata per la manutenzione del sito

#### Idee progetto

Sito web panini (RistoTN Web):

- Autenticazione
- Panini più popolari (sempre custom)
- Partire da 0 con aggiunte
- Solo panini ?
- Idea di Deliveroo in loco
- I gestori possono iscirversi
  - Due tipi diversi di Autenticazione
- Login generico con mail unitn
- Login gestori con pagamento mensile per restare
- Utente può ordinare da diversi gestori
- Dopo l'ordine **DEVI** pagare online (API Stripe)
- Utente anonimo può visualizzare ogni ristorante presente nel sito. Premendo uno dei ristoranti si accede all'area di Login. Loggandosi si accede ai menù
- Pagina menù non interattiva, per poter personalizzare devi loggarti
- Utente anonimo che preme su un panino viene portato alla pagina di login
- Se sei loggato e premi il panino ti manda al carrello
- Se sei loggato e premi custom -> Menù di custom
- No registrazione -> Direttamente con login Google
- Allergie e parte cibi ecosostenibili
- Richiesta del luogo per effettuare la ricerca
