package models

import (
	"context"
	"github.com/mark3labs/mcp-go/mcp"
)

type Tool struct {
	Definition mcp.Tool
	Handler    func(ctx context.Context, req mcp.CallToolRequest) (*mcp.CallToolResult, error)
}

// SMSReponseetatetat represents the SMSReponseetatetat schema from the OpenAPI specification
type SMSReponseetatetat struct {
	Code int `json:"code,omitempty"` // Code retour. Voir "tableau des code retour" dans l'annexe de la documentation
	Message string `json:"message,omitempty"` // Libellé associé au code de retour
	Smslong string `json:"smslong,omitempty"` // Nombre de SMS longs facturés
	Tel string `json:"tel,omitempty"` // Numero de téléphone concerné
}

// SubaccountAddResponse represents the SubaccountAddResponse schema from the OpenAPI specification
type SubaccountAddResponse struct {
	Etat map[string]interface{} `json:"etat,omitempty"`
}

// CreditResponseetat represents the CreditResponseetat schema from the OpenAPI specification
type CreditResponseetat struct {
	Credit float64 `json:"credit,omitempty"` // Montant du crédit restant
	Quantite string `json:"quantite,omitempty"` // Equivalence du crédit en nombre de SMS vers la France Métropolitaine.
}

// HLRReponseetat represents the HLRReponseetat schema from the OpenAPI specification
type HLRReponseetat struct {
	Etat []HLRReponseetatetat `json:"etat"` // liste des retours
}

// SubaccountResponse represents the SubaccountResponse schema from the OpenAPI specification
type SubaccountResponse struct {
	Etat map[string]interface{} `json:"etat,omitempty"`
}

// Erreuretat represents the Erreuretat schema from the OpenAPI specification
type Erreuretat struct {
	Etat []Erreuretatetat `json:"etat,omitempty"`
}

// REPERTOIREcreaterequest represents the REPERTOIREcreaterequest schema from the OpenAPI specification
type REPERTOIREcreaterequest struct {
	Keyid string `json:"keyid"` // Clé API
	Repertoireedit string `json:"repertoireEdit"` // Action à réaliser doit valoir "create" ici.
	Repertoirenom string `json:"repertoireNom"` // Nom du répertoire (libellé) à créer
}

// REPERTOIREmodifreponse represents the REPERTOIREmodifreponse schema from the OpenAPI specification
type REPERTOIREmodifreponse struct {
	Etat REPERTOIREmodifreponseetat `json:"etat,omitempty"`
}

// LISTENOIREReponse represents the LISTENOIREReponse schema from the OpenAPI specification
type LISTENOIREReponse struct {
	Etat LISTENOIREReponseetat `json:"etat,omitempty"`
}

// REPERTOIREcreatereponse represents the REPERTOIREcreatereponse schema from the OpenAPI specification
type REPERTOIREcreatereponse struct {
	Etat REPERTOIREcreatereponseetat `json:"etat,omitempty"`
}

// REPERTOIREmodifreponseetat represents the REPERTOIREmodifreponseetat schema from the OpenAPI specification
type REPERTOIREmodifreponseetat struct {
	Etat []REPERTOIREmodifreponseetatetat `json:"etat,omitempty"`
}

// REPERTOIREmodifrequest represents the REPERTOIREmodifrequest schema from the OpenAPI specification
type REPERTOIREmodifrequest struct {
	Champ16 []string `json:"champ16,omitempty"` // Champs O des contacts
	Champ5 []string `json:"champ5,omitempty"` // Champs D des contacts
	Champ24 []string `json:"champ24,omitempty"` // Champs W des contacts
	Champ2 []string `json:"champ2,omitempty"` // Champs A des contacts
	Champ12 []string `json:"champ12,omitempty"` // Champs K des contacts
	Champ21 []string `json:"champ21,omitempty"` // Champs T des contacts
	Champ26 []string `json:"champ26,omitempty"` // Champs Y des contacts
	Champ18 []string `json:"champ18,omitempty"` // Champs Q des contacts
	Champ15 []string `json:"champ15,omitempty"` // Champs N des contacts
	Champ14 []string `json:"champ14,omitempty"` // Champs M des contacts
	Champ25 []string `json:"champ25,omitempty"` // Champs X des contacts
	Num []string `json:"num"` // liste des numéros des téléphone à ajouter ou supprimer
	Champ7 []string `json:"champ7,omitempty"` // Champs F des contacts
	Champ13 []string `json:"champ13,omitempty"` // Champs L des contacts
	Champ23 []string `json:"champ23,omitempty"` // Champs V des contacts
	Champ1 []string `json:"champ1,omitempty"` // Noms des contact
	Repertoireid string `json:"repertoireId"` // repertoireId du répertoire cible
	Champ22 []string `json:"champ22,omitempty"` // Champs U des contacts
	Champ6 []string `json:"champ6,omitempty"` // Champs E des contacts
	Champ4 []string `json:"champ4,omitempty"` // Champs C des contacts
	Champ20 []string `json:"champ20,omitempty"` // Champs S des contacts
	Keyid string `json:"keyid"` // Clé API
	Champ10 []string `json:"champ10,omitempty"` // Champs I des contacts
	Champ11 []string `json:"champ11,omitempty"` // Champs J des contacts
	Champ8 []string `json:"champ8,omitempty"` // Champs G des contacts
	Repertoireedit string `json:"repertoireEdit"` // action à réaliser, "add" pour l'ajout de numéros, "del" pour la suppression de numéros
	Champ17 []string `json:"champ17,omitempty"` // Champs P des contacts
	Champ3 []string `json:"champ3,omitempty"` // Champs B des contacts
	Champ27 []string `json:"champ27,omitempty"` // Champs Z des contacts
	Champ9 []string `json:"champ9,omitempty"` // Champs H des contacts
	Champ19 []string `json:"champ19,omitempty"` // Champs R des contacts
}

// SMSRequest represents the SMSRequest schema from the OpenAPI specification
type SMSRequest struct {
	Sms []string `json:"sms"`
	Gmt_zone string `json:"gmt_zone,omitempty"` // Fuseau horaire de la date d'envoi
	Smslong string `json:"smslong,omitempty"` // Le SMS long permet de dépasser la limite de 160 caractères en envoyant un message constitué de plusieurs SMS. Il est possible d’envoyer jusqu’à 6 SMS concaténés pour une longueur totale maximale de 918 caractères par message. Pour des raisons technique, la limite par SMS concaténé étant de 153 caractères. En cas de modification de l’émetteur, il faut considérer l’ajout automatique de 12 caractères du « STOP SMS ». Pour envoyer un smslong, il faut ajouter le paramètre smslong aux appels. La valeur de SMS doit être le nombre maximum de sms concaténé autorisé. Pour ne pas avoir ce message d’erreur et obtenir un calcul dynamique du nombre de SMS alors il faut renseigner smslong = "999"
	Tracker []string `json:"tracker,omitempty"`
	Date_envoi string `json:"date_envoi,omitempty"` // Paramètre optionnel, date d'envoi au format YYYY-MM-DD hh:mm
	Num []string `json:"num"`
	Emetteur string `json:"emetteur,omitempty"` // L'emetteur doit être une chaîne alphanumérique comprise entre 4 et 11 caractères. Les caractères acceptés sont les chiffres entre 0 et 9, les lettres entre A et Z et l’espace. Il ne peut pas comporter uniquement des chiffres. Pour la modification de l’émetteur et dans le cadre de campagnes commerciales, les opérateurs imposent contractuellement d’ajouter en fin de message le texte suivant : STOP XXXXX De ce fait, le message envoyé ne pourra excéder une longueur de 148 caractères au lieu des 160 caractères, le « STOP » étant rajouté automatiquement.
	Nostop string `json:"nostop,omitempty"` // Si le message n’est pas à but commercial, vous pouvez faire une demande pour retirer l’obligation du STOP. Une fois votre demande validée par nos services, vous pourrez supprimer la mention STOP SMS en ajoutant nostop = "1"
	Numazur string `json:"numAzur,omitempty"`
	Repertoireid string `json:"repertoireId,omitempty"` // Id du repertoire
	Ucs2 string `json:"ucs2,omitempty"` // Il est également possible d’envoyer des SMS en alphabet non latin (russe, chinois, arabe, etc) sur les numéros hors France métropolitaine. Pour ce faire, la requête devrait être encodée au format UTF-8 et contenir l’argument ucs2 = "1" Du fait de contraintes techniques, 1 SMS unique ne pourra pas dépasser 70 caractères (au lieu des 160 usuels) et dans le cas de SMS long, chaque sms ne pourra dépasser 67 caractères.
	Keyid string `json:"keyid"` // Clé API
}

// ComptageReponse represents the ComptageReponse schema from the OpenAPI specification
type ComptageReponse struct {
	Etat ComptageReponseetat `json:"etat,omitempty"`
}

// ComptageRequest represents the ComptageRequest schema from the OpenAPI specification
type ComptageRequest struct {
	Emetteur string `json:"emetteur,omitempty"` // - L'emetteur doit être une chaîne alphanumérique comprise entre 4 et 11 caractères. - Les caractères acceptés sont les chiffres entre 0 et 9, les lettres entre A et Z et l’espace. - Il ne peut pas comporter uniquement des chiffres. - Pour la modification de l'émetteur et dans le cadre de campagnes commerciales, les opérateurs imposent contractuellement d'ajouter en fin de message le texte "STOP XXXXX". De ce fait, le message envoyé ne pourra excéder une longueur de 148 caractères au lieu des 160 caractères, le « STOP » étant rajouté automatiquement.
	Numazur string `json:"numAzur,omitempty"`
	Gmt_zone string `json:"gmt_zone,omitempty"` // Fuseau horaire de la date d'envoi
	Keyid string `json:"keyid"` // Clé API
	Smslong string `json:"smslong,omitempty"` // Le SMS long permet de dépasser la limite de 160 caractères en envoyant un message constitué de plusieurs SMS. Il est possible d’envoyer jusqu’à 6 SMS concaténés pour une longueur totale maximale de 918 caractères par message. Pour des raisons technique, la limite par SMS concaténé étant de 153 caractères. En cas de modification de l’émetteur, il faut considérer l’ajout automatique de 12 caractères du « STOP SMS ». Pour envoyer un smslong, il faut ajouter le paramètre smslong aux appels. La valeur de SMS doit être le nombre maximum de sms concaténé autorisé. Pour ne pas avoir ce message d’erreur et obtenir un calcul dynamique du nombre de SMS alors il faut renseigner smslong = "999"
	Ucs2 string `json:"ucs2,omitempty"` // Il est également possible d’envoyer des SMS en alphabet non latin (russe, chinois, arabe, etc) sur les numéros hors France métropolitaine. Pour ce faire, la requête devrait être encodée au format UTF-8 et contenir l’argument ucs2 = "1" Du fait de contraintes techniques, 1 SMS unique ne pourra pas dépasser 70 caractères (au lieu des 160 usuels) et dans le cas de SMS long, chaque sms ne pourra dépasser 67 caractères.
	Date_envoi string `json:"date_envoi,omitempty"` // Date d'envoi au format YYYY-MM-DD hh:mm . Ce paramètre est optionnel, si il est omis l'envoi est réalisé immédiatement.
	Nostop string `json:"nostop,omitempty"` // Si le message n’est pas à but commercial, vous pouvez faire une demande pour retirer l’obligation du STOP. Une fois votre demande validée par nos services, vous pourrez supprimer la mention STOP SMS en ajoutant nostop = "1"
	Num string `json:"num"` // Numero de téléphone au format national (exemple 0680010203) ou international (example 33680010203)
	Sms string `json:"sms"` // Message à envoyer aux destinataires. Le message doit être encodé au format utf-8 et ne contenir que des caractères existant dans l'alphabet GSM. Il est également possible d'envoyer (à l'étranger uniquement) des SMS en UCS-2, cf paramètre ucs2 pour plus de détails.
	Tracker string `json:"tracker,omitempty"` // Le tracker doit être une chaine alphanumérique de moins de 50 caractères. Ce tracker sera ensuite renvoyé en paramètre des urls pour les retours des accusés de réception.
	Comptage string `json:"comptage"`
}

// HLRrequest represents the HLRrequest schema from the OpenAPI specification
type HLRrequest struct {
	Keyid string `json:"keyid"` // Clé API
	Num []string `json:"num"` // liste de numéros de téléphone
	Gethlr string `json:"getHLR"` // Doit valoir "1"
}

// SMSReponse represents the SMSReponse schema from the OpenAPI specification
type SMSReponse struct {
	Etat SMSReponseetat `json:"etat,omitempty"`
}

// ShortlinkResponse represents the ShortlinkResponse schema from the OpenAPI specification
type ShortlinkResponse struct {
	Etat map[string]interface{} `json:"etat,omitempty"`
}

// LISTENOIREReponseetatetat represents the LISTENOIREReponseetatetat schema from the OpenAPI specification
type LISTENOIREReponseetatetat struct {
	Listenoire string `json:"listeNoire"` // Doit valoir "OK"
	Tel string `json:"tel"` // Numéro de téléphone à placer en liste noire. Format national Français ou international.
}

// SubaccountAddRequest represents the SubaccountAddRequest schema from the OpenAPI specification
type SubaccountAddRequest struct {
	Subaccountedit string `json:"subAccountEdit"`
	Subaccountlogin string `json:"subAccountLogin"`
	Subaccountpassword string `json:"subAccountPassword"`
	Keyid string `json:"keyid"`
}

// ShortlinkRequest represents the ShortlinkRequest schema from the OpenAPI specification
type ShortlinkRequest struct {
	Keyid string `json:"keyid"`
	Shortlink string `json:"shortlink"`
}

// REPERTOIREcreatereponseetat represents the REPERTOIREcreatereponseetat schema from the OpenAPI specification
type REPERTOIREcreatereponseetat struct {
	Etat []REPERTOIREcreatereponseetatetat `json:"etat,omitempty"`
}

// HLRReponseetatetat represents the HLRReponseetatetat schema from the OpenAPI specification
type HLRReponseetatetat struct {
	Tel string `json:"tel"` // Numero de téléphone concerné
	Operateur string `json:"operateur"` // Opérateur associé (si numéro valide)
}

// Erreur represents the Erreur schema from the OpenAPI specification
type Erreur struct {
	Etat Erreuretat `json:"etat,omitempty"`
}

// HLRReponse represents the HLRReponse schema from the OpenAPI specification
type HLRReponse struct {
	Etat HLRReponseetat `json:"etat,omitempty"`
}

// SubaccountRequest represents the SubaccountRequest schema from the OpenAPI specification
type SubaccountRequest struct {
	Subaccountkeyid string `json:"subAccountKeyId,omitempty"` // keyid du sous-compte
	Subaccountprice string `json:"subAccountPrice,omitempty"`
	Subaccountrestrictionstop string `json:"subAccountRestrictionStop,omitempty"`
	Subaccountrestrictiontime string `json:"subAccountRestrictionTime,omitempty"`
	Keyid string `json:"keyid"` // Clé API
	Subaccountaddcredit string `json:"subAccountAddCredit,omitempty"` // montant du crédit à ajouter
	Subaccountcountrycode string `json:"subAccountCountryCode,omitempty"`
	Subaccountedit string `json:"subAccountEdit"` // action à réaliser soit setPrice pour définir un prix ou addCredit pour ajouter du credit ou setRestriction modifier la restriction stop /
}

// REPERTOIREcreatereponseetatetat represents the REPERTOIREcreatereponseetatetat schema from the OpenAPI specification
type REPERTOIREcreatereponseetatetat struct {
	Repertoireid string `json:"repertoireId,omitempty"` // repertoireId du repertoire crée.
	Code string `json:"code"` // Code retour. Voir "tableau des code retour" dans l'annexe de la documentation
	Message string `json:"message,omitempty"` // Libellé associé au code retour.
}

// REPERTOIREmodifreponseetatetat represents the REPERTOIREmodifreponseetatetat schema from the OpenAPI specification
type REPERTOIREmodifreponseetatetat struct {
	Tel string `json:"tel,omitempty"` // Numéro de téléphone
	Code string `json:"code"` // Code retour. Voir "tableau des code retour" dans l'annexe de la documentation
	Message string `json:"message,omitempty"` // Libellé associé au code retour.
	Repertoireid string `json:"repertoireId,omitempty"` // repertoireId passé en argument lors de l'appel
}

// SMSReponseetat represents the SMSReponseetat schema from the OpenAPI specification
type SMSReponseetat struct {
	Etat []SMSReponseetatetat `json:"etat,omitempty"`
}

// SmsUniqueRequest represents the SmsUniqueRequest schema from the OpenAPI specification
type SmsUniqueRequest struct {
	Date_envoi string `json:"date_envoi,omitempty"` // Date d'envoi au format YYYY-MM-DD hh:mm . Ce paramètre est optionnel, si il est omis l'envoi est réalisé immédiatement.
	Emetteur string `json:"emetteur,omitempty"` // - L'emetteur doit être une chaîne alphanumérique comprise entre 4 et 11 caractères. - Les caractères acceptés sont les chiffres entre 0 et 9, les lettres entre A et Z et l’espace. - Il ne peut pas comporter uniquement des chiffres. - Pour la modification de l'émetteur et dans le cadre de campagnes commerciales, les opérateurs imposent contractuellement d'ajouter en fin de message le texte "STOP XXXXX". De ce fait, le message envoyé ne pourra excéder une longueur de 148 caractères au lieu des 160 caractères, le « STOP » étant rajouté automatiquement.
	Gmt_zone string `json:"gmt_zone,omitempty"` // Fuseau horaire de la date d'envoi
	Ucs2 string `json:"ucs2,omitempty"` // Il est également possible d’envoyer des SMS en alphabet non latin (russe, chinois, arabe, etc) sur les numéros hors France métropolitaine. Pour ce faire, la requête devrait être encodée au format UTF-8 et contenir l’argument ucs2 = "1" Du fait de contraintes techniques, 1 SMS unique ne pourra pas dépasser 70 caractères (au lieu des 160 usuels) et dans le cas de SMS long, chaque sms ne pourra dépasser 67 caractères.
	Tracker string `json:"tracker,omitempty"` // Le tracker doit être une chaine alphanumérique de moins de 50 caractères. Ce tracker sera ensuite renvoyé en paramètre des urls pour les retours des accusés de réception.
	Nostop string `json:"nostop,omitempty"` // Si le message n’est pas à but commercial, vous pouvez faire une demande pour retirer l’obligation du STOP. Une fois votre demande validée par nos services, vous pourrez supprimer la mention STOP SMS en ajoutant nostop = "1"
	Numazur string `json:"numAzur,omitempty"`
	Sms string `json:"sms"` // Message à envoyer aux destinataires. Le message doit être encodé au format utf-8 et ne contenir que des caractères existant dans l'alphabet GSM. Il est également possible d'envoyer (à l'étranger uniquement) des SMS en UCS-2, cf paramètre ucs2 pour plus de détails.
	Keyid string `json:"keyid"` // Clé API
	Num string `json:"num"` // Numero de téléphone au format national (exemple 0680010203) ou international (example 33680010203)
	Smslong string `json:"smslong,omitempty"` // Le SMS long permet de dépasser la limite de 160 caractères en envoyant un message constitué de plusieurs SMS. Il est possible d’envoyer jusqu’à 6 SMS concaténés pour une longueur totale maximale de 918 caractères par message. Pour des raisons technique, la limite par SMS concaténé étant de 153 caractères. En cas de modification de l’émetteur, il faut considérer l’ajout automatique de 12 caractères du « STOP SMS ». Pour envoyer un smslong, il faut ajouter le paramètre smslong aux appels. La valeur de SMS doit être le nombre maximum de sms concaténé autorisé. Pour ne pas avoir ce message d’erreur et obtenir un calcul dynamique du nombre de SMS alors il faut renseigner smslong = "999"
}

// ComptageReponseetat represents the ComptageReponseetat schema from the OpenAPI specification
type ComptageReponseetat struct {
	Etat []ComptageReponseetatetat `json:"etat,omitempty"`
}

// CreditResponse represents the CreditResponse schema from the OpenAPI specification
type CreditResponse struct {
	Etat CreditResponseetat `json:"etat,omitempty"`
}

// LISTENOIREReponseetat represents the LISTENOIREReponseetat schema from the OpenAPI specification
type LISTENOIREReponseetat struct {
	Etat []LISTENOIREReponseetatetat `json:"etat"`
}

// ComptageReponseetatetat represents the ComptageReponseetatetat schema from the OpenAPI specification
type ComptageReponseetatetat struct {
	Nb_caractere string `json:"nb_caractere,omitempty"` // nombre de caractères
	Nb_sms string `json:"nb_sms,omitempty"` // nombre de sms nécessaires
	Tel string `json:"tel,omitempty"` // numéro de téléphone
}

// Erreuretatetat represents the Erreuretatetat schema from the OpenAPI specification
type Erreuretatetat struct {
	Code string `json:"code,omitempty"` // Code retour. Voir "tableau des code retour" dans l'annexe de la documentation
	Message string `json:"message,omitempty"` // Libellé associé au code de retour
}
