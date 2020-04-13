# Progetto di Esempio per sviluppare un bel servizio in python deployabile su Lambda

> Quando incontrate problemi, spendete qualche ora su Google a per risolvere e alla fine riuscite investite 10 minuti per ampliare questo README in modo che chi avrà i vostri stessi problemi non dovra perderci le ore, Grazie.

## Struttura del progetto:

### Pipfile

Documento che contiene le librerie Pipfile [repo](https://github.com/pypa/pipenv)

Per installare le librerie:

```sh
pipenv install
```

**NB: può essere che l'installazione non vada a buon fine a causa della versione di python. Quando si usa pipenv viene utilizzato il python che si ha sul sistema. Se questo differisce da quello nel file Pipfile bisogna esplicitare la propria versione di Python, esempio:**

> nel Pipfile è dichiarato python 3.6 ma sul mio sistema ho python 3.7
> 1. posso installare python 3.6 ed essere sicuro che runno l'ambiente come specificato nel Pipfile
> 2. posso forzare l'utilizzo del python sul mio sistema aggiungendo runnando pipenv install --python 3.7. In questo modo pipenv crea l'ambiente con il mio python (nel Pipfile rimane comunque 3.6)

Per attivare l'ambiente virtuale:

```sh
pipenv shell
```

Per lanciare comandi dall'ambiente virtuale:

```sh
pipenv run <COMANDO>
```

Per disattivare l'ambiente virtuale:

```sh
exit
```

### config.py

File nel quale vengono settate le variabili di ambiente per l'applicazione in base agli ambienti:

* dev: ambiente di lavoro per lo sviluppo in locale
* staging: ambiente di lavoro che deve essere il più simile possibile all'ambiente di prod
* prod: ambiente di produzione, attenti quando toccate le cose qui

Diviso in classi [link](https://flask.palletsprojects.com/en/1.1.x/config/#development-production):

* DefaultFlaskConfig: tutte le variabili per settare Flask [link](https://flask.palletsprojects.com/en/1.1.x/config/)
* DefaultCustomConfig: variabili custom che vogliamo impostare noi
* classi con lo stesso nome dei vari ambienti (dev,staging,prod)

### zappa_settings.json

File di configurazione di zappa, il tool che permette il deploy di tutto su AWS con poco effort.
Per dettagli [link](https://github.com/Miserlou/Zappa#advanced-settings)

>**IMPORTANTE: Ricordatevi di cambiare le proprietà _project_name_ e _s3_bucket_ in modo che rispecchino il vostro progetto. Cambiate anche le varie descrizioni (lambda_description e apigateway_description)**

### app.py

Entry point dell'applicazione Flask.
Espone un Endpoint:
1. RootCheck (aka HealthCheck): alla root del path deve essere sempre possibile fare una GET per vedere che il servizio runni senza problemi

E mappa tutte le funzioni definite nei file della folder 'routes' in Endpoint

**L'idea è che non dobbiate toccare questo file per poter sviluppare il vostro microservizio**

# Folder del Progetto

### models

All'interno di questa folder vanno creati tutti i Documenti MongoDB.
I Document sono classi Python che forniscono un schema per i Document, in modo da forzare uno schema per un database che sarebbe schemaless.
**Un solo file per Document come convenzione**

### controllers

In questa cartella sono presenti i controllers dei models, quindi funzioni Python che incapsulano la business logic, da una semplice _query_ a mandare mail/notifiche ecc. ecc.
**Un file ..._controller.py per ogni file model**

### routes

In questa cartella sono presenti le routes in cui esporre i controllers.
Questa cartella è un po' particolare nel senso che ha delle **importanti regole** da seguire:
1. Assolutamente **vietato** importare le funzioni tramite costrutto _from ... import ..._ es:```from controllers.qualcosa_controller import get_qualcosa```. Per importarle usare invece ```import controllers.qualcosa_controller as controller```
2. Scrivere solo **funzioni che ritornano istanze di oggetti Route**. Se si ha la necessità di scrivere una funzione di utility metterla nel package delle utility o in una folder dentro routes.

Rispettando queste 2 regole riuscirete a creare delle route in men che non si dica!

_Per chi volesse curiosare può aprire il file \_\_init\_\_.py di routes per scoprire che cosa succede dietro le quinte._

### utility

non c'è bisogno di spiegare a cosa serve

# Lavorare al progetto in locale

## Workflow

1. Definisco i miei dati nella folders _models_
2. Definisco i miei controllers nella folders _controllers_. Questi utilizzano i _models_ definiti precedentement
3. Definisco le routes come funzioni nella folder _routes_ le quali usano i controllers.
4. Lancio il server di Flask per vedere che tutto funzioni

per lanciare l'applicazione in locale:

```sh
export FLASK_ENV=dev
pipenv run flask run
```

dovrebbe uscire qualcosa tipo così:

```sh
* Environment: dev
* Debug mode: off
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
* Restarting with stat
* Debugger is active!
* Debugger PIN: 247-025-819
```

Running on è l'indirizo dal quale possiamo testare (usando ad esempio [Postman](https://www.postman.com/)) che le route e i controller che abbiamo creato funzionino

# Deploy del Progetto con Zappa

Per poter utilizzare Zappa dovrete aver **installato e settato aws-cli** (istruzioni più sotto) nel vostro PC.
Il deploy in zappa è easy peasy.
```sh
zappa deploy [AMBIENTE]
```
quindi se dobbiamo deployare in staging:
```sh
zappa deploy staging
```
Questo caricherà e deployerà il progetto usando l'oggetto JSON "staging" nel file *zappa_settings.json* come configurazione.
Il comando finische con un log del genere:
```sh
Deploying API Gateway..
Deployment complete\!: https://kl51s8dohe.execute-api.eu-west-1.amazonaws.com/staging
```
Prendete l'URL e settatelo come WebHook per direzionare il traffico dal server di Telegram al Codice appena deployato.

Se dovete vedere i Log del codice deployato fate:
```sh
zappa tail [AMBIENTE]
```

Una volta che il progetto è deployato se dovete aggiornarlo vi basta:
```sh
zappa update [AMBIENTE]
```
Vi basta aggiornarlo perchè le risorse AWS sono già create e dovete solo cambiare il codice.

## Installare AWS-CLI2 e Settare lo user di default
Per questa operazione vi linko la documentazione così vi guardate in base al vostro Sistema Operativo:
- [Installare](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)
- [Configurare l'utente](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html#cli-quick-configuration)

Di seguito un minimo di comandi per chi non vuole impazzire:
### Linux
>NB: Assolutamente evitate di avere spazi nelle folder del path di installazione altrimenti va tutto a puttana. (è scritto proprio così nella doc)
```sh
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```
Scarica, unzippa e installa.
Per verificare che sia tutto settato:
```sh
aws --version
```
>Nota: può essere che aws non venga trovato come comando e vada usato aws2. In questo caso dovrete ricordarvi che avete aws2 al posto di aws. (in Linux vi fate un alias aws=aws2)

Per configurare il vostro user dovete avere la **vostra** "aws_access_key_id" e la **vostra** "aws_secret_access_key".
Per averle dovete chiederle a [pierluigi.giancola@gmail.com](mailto:pierluigi.giancola@gmail.com).
Una volta che le avete:
```sh
aws configure
AWS Access Key ID [None]: [LA_VOSTRA_aws_access_key_id]
AWS Secret Access Key [None]: [LA_VOSTRA_aws_secret_access_key]
Default region name [None]: eu-west-1 # IMPORTANTE
Default output format [None]: json
```
Ora provate a fare un semplice comando:
```sh
aws s3 ls
```
E se non ci sono errori siete pronti a deployare.

>> Importante: Per deployare il vostro user deve essere parte del gruppo IAM "Zappa" altrimenti potreste non avere i permessi.