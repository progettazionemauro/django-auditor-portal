from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class SchemaCertificativo(models.Model): #registrato
    
    schema_certificazione = models.CharField(max_length=300, unique=True) 
   
    
    class Meta:
        verbose_name_plural="Schema Certificativo"

    def __str__(self):
        return self.schema_certificazione

class Auditor(models.Model): #registrato
    
    nome_auditor = models.CharField(max_length=300, unique=True) # fare attenzione: nel momento in cui si sostituisce il database è necessario inserire o il valore di default oppure blank and null: vedere qui stackoverflow: https://stackoverflow.com/a/73509787/11233866       
    email_auditor=models.EmailField(max_length=254)
    cellulare_auditor=PhoneNumberField()
    schema_certificativo=models.ManyToManyField(SchemaCertificativo)
    
    
    class Meta:
        verbose_name = 'Auditor'
        verbose_name_plural = 'Auditor'

    def __str__(self):
        return f"{self.nome_auditor}"
    

    
# class AnagraficaTeamCliente(models.Model):
#   # Relazione one-To-Many for AnagraficaSitiCliente
#   # Qui vengono riportati: nominativi dei referenti di sito / Ruolo / (prestare attenzione al cambiamento organizzativo) / email / cell

""" class AnagraficaTeamCliente(models.Model):  #registrato - manca la relazione
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
    
    referente_sito= # uno a molti da collegare ad Class AnagraficaTeamCliente
   ruolo_ref_sito= # uno a molti da collegare ad Class AnagraficaTeamCliente
   cell_ref_sito=# uno a molti da collegare ad Class AnagraficaTeamCliente
   acronimo_ref_sito=# uno a molti da collegare ad Class AnagraficaTeamCliente
   ref_sito_note=# uno a molti da collegare ad Class AnagraficaTeamCliente
   ref_sito_acronimo= # uno a molti da collegare ad Class AnagraficaTeamCliente
   
    anagraficasitocliente = models.ForeignKey(
        anagraficasitocliente,
        on_delete=models.PROTECT
    )

class AnagraficaSitiCliente(models.Model):  ## RIPRENDERE DA QUESTA CLASSE##
#   # Relazione one-To-Many for EvidenzeAuditSito
#   # Qui vengono riportate evidenze sui siti: n° Sito / Indirizzo Sito / Referente di Sito
    Scelta_nome_sito= (
        ('15', 'Genova (Ge), Via Puccini 2 / Via Hermada 6b'),       
       )
  
   sito_nome=nome_ref_cliente = models.CharField(max_length=300, choices = Scelta_nome_sito, default="Marco Bongiorni") 
   indirizzo_sito=models.TextField()    
   referente_1_sito= # uno a molti da collegare ad Class AnagraficaTeamCliente
   ruolo_ref_1_sito= # uno a molti da collegare ad Class AnagraficaTeamCliente
   cell_ref_1_sito=# uno a molti da collegare ad Class AnagraficaTeamCliente
   acronimo_ref_1_sito=# uno a molti da collegare ad Class AnagraficaTeamCliente
   ref_1_sito_note=# uno a molti da collegare ad Class AnagraficaTeamCliente
   ref_1_sito_acronimo= # uno a molti da collegare ad Class AnagraficaTeamCliente
   
   referente_2_sito= # uno a molti da collegare ad Class AnagraficaTeamCliente
   ruolo_ref_2_sito= # uno a molti da collegare ad Class AnagraficaTeamCliente
   cell_ref_2_sito=# uno a molti da collegare ad Class AnagraficaTeamCliente
   acronimo_ref_2_sito=# uno a molti da collegare ad Class AnagraficaTeamCliente
   ref_2_sito_note=# uno a molti da collegare ad Class AnagraficaTeamCliente
   ref_2_sito_acronimo= # uno a molti da collegare ad Class AnagraficaTeamCliente
   
   referente_3_sito= # uno a molti da collegare ad Class AnagraficaTeamCliente
   ruolo_ref_3_sito= # uno a molti da collegare ad Class AnagraficaTeamCliente
   cell_ref_3_sito=# uno a molti da collegare ad Class AnagraficaTeamCliente
   acronimo_ref3_sito=# uno a molti da collegare ad Class AnagraficaTeamCliente
   ref_3_sito_note=# uno a molti da collegare ad Class AnagraficaTeamCliente
   ref_3_sito_acronimo= # uno a molti da collegare ad Class AnagraficaTeamCliente
   
    referente_4_sito= # uno a molti da collegare ad Class AnagraficaTeamCliente
   ruolo_ref_4_sito= # uno a molti da collegare ad Class AnagraficaTeamCliente
   cell_ref_4_sito=# uno a molti da collegare ad Class AnagraficaTeamCliente
   acronimo_ref_4_sito=# uno a molti da collegare ad Class AnagraficaTeamCliente
   ref_4_sito_note=# uno a molti da collegare ad Class AnagraficaTeamCliente
   ref_4_sito_acronimo= # uno a molti da collegare ad Class AnagraficaTeamCliente
   
   referente_5_sito= # uno a molti da collegare ad Class AnagraficaTeamCliente
   ruolo_ref_45sito= # uno a molti da collegare ad Class AnagraficaTeamCliente
   cell_ref_5_sito=# uno a molti da collegare ad Class AnagraficaTeamCliente
   acronimo_ref_5_sito=# uno a molti da collegare ad Class AnagraficaTeamCliente
   ref_5_sito_note=# uno a molti da collegare ad Class AnagraficaTeamCliente
   ref_5_sito_acronimo= # uno a molti da collegare ad Class AnagraficaTeamCliente """

# class EvidenzeAuditSito(models.Model): 
#   # Relazione Many-to-One - VersioningAuditSito
#   
#   # qui vengono riportate le evidenze di sito - Colonne: Data / NC minori / NC maggiori/ OSS / Agenda_di_audit / Rapporto_di_Audit / Check_di_Audit / 
#  # / docs_1 (da creare appositamente)/ docs_2 (da creare appositamente)/ docs_3 (da creare appositamente)

# data_audit_dal=
# data_audit_al=
# agenda_di_audit=
# rapporto_di_audit=


# class VersioningAuditSito(models.Model):
#   #   Relazione one-To-many EvidenzeAuditSito
#   # qui vengono riportate le indicazioni del versioning:  
#   # Versioni: Scelta(Pre_Draft_rev_0/Pre_Draft_rev_1/Draft_rev_0//Draft_rev_1 /Draft_rev_1/Definitivo_rev_0/Definitivo_rev_1/Definitivo_rev_2)
#   # Ananzamento_Versione. Scelta: (Versione_in_gestione_auditor/Versione_in_gestione_cliente/Verione_Consolidata)


# class OpzioniAudit (models.Model)
#   # Relazione one-To-one for AnagraficaSitiCliente
#   # Agenda_Draft / Agenda_Definitiva/ Rapporto_Draft

# class Opzioni(models.Model): 
#   # relazione one-To-many for class EvidenzeSito // Eventuali Query  manyTomany per auditor / manyTomany per AnagraficaSitiCliente
#   # qui vengono riportate le risultanze dell'audit in questa maniera:
#   # Rilievi: Scelta (NC_maggiori / NC_minori / Osservazioni)

    

 

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


