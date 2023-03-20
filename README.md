# Scaffold for Backend-Frontend in Django
Parte della spiegazione è tratta da questo post:https://python.plainenglish.io/how-to-convert-database-model-to-csv-xls-json-etc-and-vice-versa-using-django-import-export-42312aad7dfe
## Questo progetto ha lo scopo di recuperare dei dati da google sheets, inserirli in un database
## Django per poi strutturare il frontend
## Dalle analisi condotte allo stato attuale risulta INUTILE creare un'apposita API per il collegamento
## dei dati da Google Sheets a Django in quanto non esite una vera e propora possibilità di scambio
## In altre parole, pur se possibile effettuare una connessione di dati da Google Sheets all'interno del 
## DB Django non risulta poi possibile effettuare una esposrtazione in continuo di questi dati verso gsheets
## Per questo motivo si preferisce dunque effettuare un'esportazione di questi dati in un formato maggiormente
## digeribile per python attraverso la libreria django-import-export. Effettuata questa prima inizializzazione dei dei dati 
#à e cotruito il modello di importazione i dati saranno poi lavorati direttamente nel DB Django

### Installation on Ubuntu

#### Scaffold the project in VSC
- make new directory for the project. After cd in the new directory
- python3 -m venv venv
- source venv/bin/activate
- pip3 install django
- django-admin startproject <Name_of_the_project>
- create a Django App: django-admin startapp app
- pip3 install django-import-export
- into settings.py add: and add “app” (app name) and “import_export” (django-import-export) to the list of “INSTALLED_APPS”
- Installare (nel caso si voglia realizzare un modello anagrafica personale) le due librerie  pip3 install django-phonenumber-field e pip3 install phonenumbers. Poi inserire in settings:  # Other apps…
    "phonenumber_field" Vedere qui: https://django-phonenumber-field.readthedocs.io/en/latest/index.html - Vedere per questa
    risposta per l'inserimento del widget: https://stackoverflow.com/a/72665157/11233866

## Create Model
Ora è necessario create il modello che possa utilizzare la funzione di importazione dei dati
### Operazioni Preliminari per la gestione del database e del modello

Le operazioni di definizione delle chiavi e la gestioene del modello interagiscono fortemente con il database sottostante. Per cui di seguito si indicano alcuni punti essenziali per la gestione del database e nel caso di crash del modello (spesso quando si effettua python3 runserver migrate) 
- Gestione delle relazioni - LINK 1 https://www.pythontutorial.net/django-tutorial/django-one-to-many/
- Gestione delle relazioni - LINK2: https://medium.com/analytics-vidhya/difference-between-one-to-one-many-to-many-and-many-to-one-relationships-in-django-2304b567152f
- Django Integrity of the database: https://medium.com/@inem.patrick/django-database-integrity-foreignkey-on-delete-option-db7d160762e4
- Shell per interagire con il dtatabase: http://www.learningaboutelectronics.com/Articles/How-to-access-and-use-the-Python-shell-with-Django.php

### Gestione dei Database in Django
#### Operazione Preliminare
Installazione di PostgreSQL - Seguire questo link su [DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-20-04)

La creazione, distruzione, upgrade e nuovo inserimento di Classi in models.py dovuti agli aggiornamenti del database possono condurre lo sviluppo del progetto a risultati disastrosi! Infatti, il database stesso soprattuo con l'inserimento di nuove chiavi può comportare il crash del progetto! Come indicato sopra la soluzione drastica può essere quella di effettuare un ripristino forzato del precedente commit con git reset. Tuttavia questo è un passaggio che non può essere utilizzato nella normalità. Ci si deve invece affidare sia in sviluppo che in produzione ad elementi di backup
Fortunatamente esistono strumenti relativamente semplici sia per il backup del Database, che per il restore che come si vedrà più sotto di backup automatico del database.
Di seguito si riportano i passaggi principali rimandando alle fonti per il dettaglio
:::
#### Installazione django-dbbackup
[fonte](https://www.youtube.com/watch?v=s54HYoJ8wrs)
1. pip3 install django-dbbackup [LINK](https://django-dbbackup.readthedocs.io/en/master/)
2. INSTALLED_APPS = (
    ...
    'dbbackup',  # django-dbbackup
) 
DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
DBBACKUP_STORAGE_OPTIONS = {'location': BASE_DIR/'backup'}

3. creare nella directory di progetto la directory backup
4. creare il primo backup: python3 manage.py dbbackup
5. reinstaurare il backup: python3 manage.py dbrestore

#### Creazione dei task periodici (effettuazione di backup periodico)
1. pip3 install wheel
2. pip3 install django-crontab [LINK pip3](https://pypi.org/project/django-crontab/)
   1. on top on settings.py {'django_crontab', ...} 
   2. now in <project_folder>/cron.py:  
>    from django.core.management import call_command
> def my_backup():
>     try:
>         call_command('dbbackup')
>     except:
>         pass
now add this to settings.py (before MIDDLEWARE): 
CRONJOBS = [('*/5 * * * *', 'myapp.cron.my_scheduled_job')]

I comandi principali sono
 - python manage.py crontab add
 - python manage.py crontab show
 - python manage.py crontab remove


### Creazione del database
Qui si hanno due opzioni a seconda dell'attività da svolgere:
OPZIONE 1: si ha a disposizione un database già completo da una fonte tipo xls, csv etc e lo si vuole importare all'interno di DJANGO. 
Si parte dalla OPZIONE 1 ipotizzando un caso complesso: Database in gsheets


### Importazione di un database gsheets, Gsheets Blueprint
1) Avendo a disposizione un DB da Gsheets si può esportare lo stesso in Json o xls
2) Nella directory pyutils sono state create delle utility per facilitare i task di importazione
3) Il file read_csv.py recupera un file scaricato in csv ed effettua il parsing identificando il nome delle colonne "Column Names": tali colonne saranno gli elementi essenziali per lo scaffolding dell'app models.py

### Creazione di models.py in relazione al database da importare
1) Creaiamo un modello semplice in app / models.py - Vedere qui: https://gist.github.com/progettazionemauro/bd924f79e42e4423bb132d0aaf8a2169
2) Registrare il modello in admin.py dell'app come indicato qui: https://gist.github.com/progettazionemauro/bd924f79e42e4423bb132d0aaf8a2169
2) recuperate dunque le colonne aprire nell'app models.py e copiare le colonne
3) verificare se Django carica correttamente python3 manage.py runserver
4) python3 manage.py runserver
4) Ctr+c
5) python3 manage.py makemigrations
6) python3 manage.py migrate
7) python3 manage.py createsuperuser

### Inserimento di dati Geografici
L'inserimento di dati geografici, seppur esiste uno specifico Django Field (GeoDjango) ed apparentemente molto semplice da installare è qualcosa che all'atto pratico si rivela molto complesso.
La causa non è da attribuirsi a Django ma a due fattori: la complessità dell'installazione di PostGis che risulta molto dipendente dalla macchina sulla quale si sta effettuando l'attività e (Secondo fattore) l'installazione dell'API di Google Maps. Si sono provate molte API di Google Maps ed alcune funzionano. Il problema connesso a Google Maps è che oltre tutto risulta difficile comprendere quali siano le quote che si raggiungono per cui sforando i limiti potrebbero arrivare salatissimi conti sulla c/credito.
Dai precedenti discorsi si è tentata con successo una terza via e cioè quela di lavorare con OpenStreetMap. L'app funziona ed è stato uno specifico commit. L'app di riferiemnto è la seguente [django-location-field](https://django-location-field.readthedocs.io/en/latest/index.html) peraltro valida anche per Google Maps e Maps Street. L'attività al momento risulta soltanto accennata




git clone --branch <name_of_branch> <http:// github link>
ls -la
cd gsheets-with-frontend
pip3 install -r requirements.txt
pip3 install -U django-gsheets-import
Google Sheets Template Preparation
Prepare the database
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py loaddata authors works
Run the project
python3 manage.py runserver <port ...8081, 8082....>
go to localhost/admin
If all is OK you can see the data imported from google sheet template
Now we go to scaffold Google Sheets template
Setting up a Google Cloud Project¶
create a Google Sheet - here is the example
Share and give editor rights to that account
go in GCC (Google Cloud Console)
go in Cloud Ovierview / Dashboard / Create New Project
Go in “Enable API Services” > Library and select the following API: Google Sheets API and Google Picker API
Go in “Enable API Services” > Credentials for official reference
Go in API > APIs and Services > Ouauth Consent Screen > External > Create: a) only App name, b) User support email and c) Developer contact information > Save and Continue
Go in “Enable API Services” > Credentials > Create Credentials > OAuth client ID > Application Type: Web Application > Name: Create > and after Authorised JavaScript origins for local testing http://localhost:8000 and after you can also add multiple relevant URIs here
Dowload JSON: here you can find Your Client ID and Your Client Secret
Note: Accessing the selected Google Sheet while only using the non-sensitive .../auth/drive.file scope requires the project’s App ID to be set. It is automatically created with each Google Cloud Project and can be found as Project number on your project’s dashboard or under the same name at Main Menu > IAM & Admin > Settings.
Go in Iam Admin > Create Service Account > Service Account Name > Create and Continue after Grant this Service ... > Select Role > Owner > Continue > Done
Copy the generated email
Now in Google Sheets Template that you have created > Sharing > paste the generated email
Back to the project
Only for testing (not in production) in file settings.py
The Browser API key; see "Key" under "APIs & Services" > "Credentials" > "API Keys"
GSHEETS_IMPORT_API_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

The Client ID; see "Client ID" under "APIs & Services" > "Credentials" > "OAuth 2.0 Client IDs"
GSHEETS_IMPORT_CLIENT_ID = 'XXXXXXXXXXXXXXXXXXXXX'

The App ID; see "Project Number" under "IAM & Admin" > "Settings"
GSHEETS_IMPORT_APP_ID = 'XXXXXXXXXXXX'