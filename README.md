# Scaffold for Backend-Frontend in Django
# parte della spiegazione è tratta da questo post:https://python.plainenglish.io/how-to-convert-database-model-to-csv-xls-json-etc-and-vice-versa-using-django-import-export-42312aad7dfe
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
#### Create Model
### Ora è necessario create il modello che possa utilizzare la funzione di importazione dei dati
### Qui si hanno due opzioni a seconda dell'attività da svolgere:
### OPZIONE 1: si ha a disposizione un database già completo da una fonte tipo xls, csv etc e lo si vuole importare all'interno di DJANGO. 
### Si parte dalla OPZIONE 1 ipotizzando un caso complesso: Database in gsheets


### Importazione di un database gsheets, Gsheets Blueprint
1) Avendo a disposizione un DB da Gsheets si può esportare lo stesso in Json o xls
2) Nella directory pyutils sono state create delle utility per facilitare i task di importazione
3) Il file read_csv.py recupera un file scaricato in csv ed effettua il parsing identificando il nome delle colonne "Column Names": tali colonne saranno gli elementi essenziali per lo scaffolding dell'app models.py

### Creazione di models.py in relazione al database da improtare
1) Creaiamo un modello semplice in app / models.py - Vedere qui: https://gist.github.com/progettazionemauro/bd924f79e42e4423bb132d0aaf8a2169
2) Registrare il modello in admin.py dell'app come indicato qui: https://gist.github.com/progettazionemauro/bd924f79e42e4423bb132d0aaf8a2169
2) recuperate dunque le colonne aprire nell'app models.py e copiare le colonne
3) verificare se Django carica correttamente python3 manage.py runserver
4) python3 manage.py runserver
4) Ctr+c
5) python3 manage.py makemigrations
6) python3 manage.py migrate
7) python3 manage.py createsuperuser




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