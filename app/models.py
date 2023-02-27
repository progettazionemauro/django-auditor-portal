from django.db import models
from phonenumber_field.modelfields import PhoneNumberField



# Create your models here.


    
class SchemaCertificativo(models.Model): #registrato
    
    Scelta_Schema = (
        ('1','ISO 9001:2015'),
        ('2', 'ISO 14001:2018'),
        ('3', 'ISO 45001:2015'),
       )  
    
    
    schema_certificazione = models.CharField(max_length=300, choices = Scelta_Schema,default="ISO 9001:2015") 

    def __str__(self):
        return self.schema_certificazione

class Auditor(models.Model): #registrato
    Scelta_Nome_Auditor = (
        ('1', 'Bassotti'),
        ('2', 'Pezzuca'),
        ('3', 'Cataldo'),
        ('4', "D'Onofrio"),
        ('5', 'Grandolfo'),
        ('6', 'Aiello'),
       )  
    
    
    nome_auditor = models.CharField(max_length=300, choices = Scelta_Nome_Auditor,default="Bassotti") # fare attenzione: nel momento in cui si sostituisce il database è necessario inserire o il valore di default oppure blank and null: vedere qui stackoverflow: https://stackoverflow.com/a/73509787/11233866       
    email_auditor=models.EmailField(max_length=254)
    cellulare_auditor=PhoneNumberField()
    schema_auditing=models.ForeignKey(SchemaCertificativo, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome_auditor
    
# class AnagraficaTeamCliente(models.Model):
#   # Relazione one-To-Many for AnagraficaSitiCliente
#   # Qui vengono riportati: nominativi dei referenti di sito / Ruolo / (prestare attenzione al cambiamento organizzativo) / email / cell

class AnagraficaTeamCliente(models.Model):  #registrato - manca la relazione
    Scelta_ref_cliente = (
        ('1', 'dott. Fabio Fivoli'),
        ('2', 'ing. Marco Bongiorni'),
        ('3', 'Miria Felici'),
        ('4', 'Daniela Paci'),
        ('5', 'Paolo Cacchione'),
        ('6', 'Luigi Roma'),
        ('7', 'Michele Manella'),
       )  
    
    Scelta_ruolo_cliente= (
        ('1', 'RSPP'),
        ('2', 'ASPP'),       
       )  
    
    nome_ref_cliente = models.CharField(max_length=300, choices = Scelta_ref_cliente, default="Marco Bongiorni") # fare attenzione: nel momento in cui si sostituisce il database è necessario inserire o il valore di default oppure blank and null: vedere qui stackoverflow: https://stackoverflow.com/a/73509787/11233866       
    email_ref_cliente=models.EmailField(max_length=254)
    cellulare_ref_cliente=PhoneNumberField()
    ruolo_ref_cliente= models.CharField(max_length=300, choices = Scelta_ruolo_cliente,default="ASPP")
   # sito_rif_cliente=models.ForeignKey(SchemaCertificativo, on_delete=models.PROTECT)

# class AnagraficaSitiCliente(models.Model):
#   # Relazione one-To-Many for EvidenzeAuditSito
#   # Qui vengono riportate evidenze sui siti: n° Sito / Indirizzo Sito / Referente di Sito


# class EvidenzeAuditSito(models.Model): 
#   
#   # qui vengono riportate le evidenze di sito - Colonne: Data / NC minori / NC maggiori/ OSS / Agenda_di_audit / Rapporto_di_Audit / Check_di_Audit / 
#  # / docs_1 (da creare appositamente)/ docs_2 (da creare appositamente)/ docs_3 (da creare appositamente)

# class OpzioniAudit (models.Model)
#   # Relazione one-To-one for AnagraficaSitiCliente
#   # Agenda_Draft / Agenda_Definitiva/ Rapporto_Draft

# class Opzioni(models.Model): 
#   # relazione one-To-many for class EvidenzeSito // Eventuali Query  manyTomany per auditor / manyTomany per AnagraficaSitiCliente
#   # qui vengono riportate le risultanze dell'audit in questa maniera:
#   # Rilievi: Scelta (NC_maggiori / NC_minori / Osservazioni)
#   # Versioni: Scelta(Pre_Draft/Draft/Definitivo)
#   # Ananzamento_Versione. Scelta: (Versione_in_gestione_auditor/Versione_in_gestione_cliente/Verione_Consolidata)
    

 

# """ 
# AUDITOR

# SITO N°
# SITO
# cOSTRUZIONE QUERY DATA 2022
# Struttura Query DATA 2022
# DATE 2022
# M/D, 
# DATA BV 2023 
# NOTE
# DATA SGA
# REGIONE
# cOSTRUZIONE QUERY m/d
# Struttura Query M/D
# cOSTRUZIONE QUERY P/R
# PRES/REM 2022, PREVISIONALE PRES/REM
# PRES/ REM (2022)
# SETT
# PIANIFICATO
# Spese presunte
# Note spese
# STATO
# NCm?
# NC M? 
# OSS?
# PDF REPORT
# PDF CHECK
# DOC REPORT
# DOC CHECK
# DOC Check Sistema
# PDF Check Sistema
# Chiusura Anno 2021
# PDF Report Sistema
# DOC Report Sistema
# AGENDA
# Note
# NC
# OSS
# Criticità
# Punto Check List 1
# Punto Norma 1
# Punto Check List 2
# Punto Norma 2
# Punto Check List 3
# Punto Norma 3
# Punto Check List 4
# Punto Norma 4
# RILEVAZIONE NC?
# RILEVAZIONE OSSERVAZIONI?
# PUNTI CHECK LIST
# PUNTI NORMA """

# app/models.py



