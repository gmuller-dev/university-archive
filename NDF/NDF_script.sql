
Create or Replace table NDF_FACTURES
    (
    idNDF INT Primary KEY NOT NULL AUTO_INCREMENT,
    azNDF VARCHAR(100),
    dMontant DOUBLE(7,2),
    iCTime INT(11),
    iCTimeValid INT(11),
    idUser INT(11) NOT NULL,
    idUserValid INT(11),
    azFileName VARCHAR(254)
    );
Create or Replace index   PK_NDF_FACTURE
  on NDF_FACTURES (idNDF);
Create or Replace index   FK_NDF_USER
  on NDF_FACTURES (idUser);
Create or Replace table NDF_ACCOUNT
    (
    idNDFACCOUNT INT Primary KEY NOT NULL AUTO_INCREMENT,
    idNDF INT ,
    dMontant DOUBLE(7,2),
    iCTime INT(11),
    idUser INT(11) NOT NULL
    );
Create or Replace index   PK_NDF_ACCOUNT
  on NDF_ACCOUNT (idNDFACCOUNT);
Create or Replace index   FK_NDFACCOUNT_USER
  on NDF_ACCOUNT (idUser);
Create or Replace index   FK_NDFACCOUNT_NDF
  on NDF_ACCOUNT (idNDF);
