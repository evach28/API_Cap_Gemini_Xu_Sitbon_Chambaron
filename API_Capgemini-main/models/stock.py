from datetime import date
from pydantic import BaseModel
from typing import Union

# Define a Pydantic BaseModel for representing Stock data
class Stock(BaseModel):
    # Basic information
    siren: int
    nic: int
    siret: int

    # Establishment details
    statutDiffusionEtablissement: str
    dateCreationEtablissement: Union[str, date]
    trancheEffectifsEtablissement: int
    anneeEffectifsEtablissement: int
    activitePrincipaleRegistreMetiersEtablissement: str
    dateDernierTraitementEtablissement: str
    etablissementSiege: bool
    nombrePeriodesEtablissement: int

    # Address information
    complementAdresseEtablissement: str
    numeroVoieEtablissement: int
    indiceRepetitionEtablissement: str
    typeVoieEtablissement: str
    libelleVoieEtablissement: str
    codePostalEtablissement: int
    libelleCommuneEtablissement: str
    libelleCommuneEtrangerEtablissement: str
    distributionSpecialeEtablissement: str
    codeCommuneEtablissement: str
    codeCedexEtablissement: str
    libelleCedexEtablissement: str
    codePaysEtrangerEtablissement: str
    libellePaysEtrangerEtablissement: str

    # Additional address details
    complementAdresse2Etablissement: str
    numeroVoie2Etablissement: str
    indiceRepetition2Etablissement: str
    typeVoie2Etablissement: str
    libelleVoie2Etablissement: str
    codePostal2Etablissement: str
    libelleCommune2Etablissement: str
    libelleCommuneEtranger2Etablissement: str
    distributionSpeciale2Etablissement: str
    codeCommune2Etablissement: str
    codeCedex2Etablissement: str
    libelleCedex2Etablissement: str
    codePaysEtranger2Etablissement: str
    libellePaysEtranger2Etablissement: str

    # Other details
    dateDebut: Union[str, date]
    etatAdministratifEtablissement: str
    enseigne1Etablissement: str
    enseigne2Etablissement: str
    enseigne3Etablissement: str
    denominationUsuelleEtablissement: str
    activitePrincipaleEtablissement: str
    nomenclatureActivitePrincipaleEtablissement: str
    caractereEmployeurEtablissement: str
    libelleCommune2Etablissement: str