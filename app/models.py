from django.db import models
from phonenumber_field.modelfields import PhoneNumberField



# Create your models here.


    
class SchemaCertificativo(models.Model):
    
    Scelta_Schema = (
        ('1','ISO 9001:2015'),
        ('2', 'ISO 14001:2018'),
        ('3', 'ISO 45001:2015'),
       )  
    
    
    schema_certificazione = models.CharField(max_length=300, choices = Scelta_Schema,default="ISO 9001:2015") 

    def __str__(self):
        return self.schema_certificazione

class Auditor(models.Model):
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






class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

