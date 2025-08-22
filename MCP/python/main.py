"""
MCP Server - Python Implementation
"""

import os
import json
import requests
from pathlib import Path
from typing import Annotated
from pydantic import Field
from mcp.server.fastmcp import FastMCP

# Create MCP server instance
mcp = FastMCP("MCP Server")

def get_config():
    """Get configuration from environment or config file."""
    class Config:
        def __init__(self):
            self.base_url = os.getenv("API_BASE_URL")
            self.bearer_token = os.getenv("API_BEARER_TOKEN")
            
            # Try to load from config file if env vars not set
            if not self.base_url or not self.bearer_token:
                config_path = Path.home() / ".api" / "config.json"
                if config_path.exists():
                    with open(config_path, 'r') as f:
                        config_data = json.load(f)
                        self.base_url = self.base_url or config_data.get("baseURL")
                        self.bearer_token = self.bearer_token or config_data.get("bearerToken")
    
    return Config()

# Add configuration resource
@mcp.resource("config://settings")
def get_config_resource() -> str:
    """Get current configuration settings."""
    config = get_config()
    return json.dumps({
        "base_url": config.base_url,
        "bearer_token": "***" if config.bearer_token else None
    }, indent=2)

# Tool functions
@mcp.tool()
def post_repertoire(repertoireNom: Annotated[str, Field(description="Input parameter: Nom du répertoire (libellé) à créer")], keyid: Annotated[str, Field(description="Input parameter: Clé API")], repertoireEdit: Annotated[str, Field(description="Input parameter: Action à réaliser doit valoir \"create\" ici.")]) -> str:
    """Gestion repertoire (creation)"""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        pass
        # Build request body
        request_data = {
        "repertoireNom": repertoireNom,
        "keyid": keyid,
        "repertoireEdit": repertoireEdit
        }
        
        # Remove None values
        request_data = {k: v for k, v in request_data.items() if v is not None}
        
        # Make API call
        url = f"{config.base_url}/repertoire"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, headers=headers, json=request_data, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to read response body: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to read response body: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Failed to create request: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Failed to create request: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Failed to create request: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def put_repertoire(keyid: Annotated[str, Field(description="Input parameter: Clé API")], repertoireEdit: Annotated[str, Field(description="Input parameter: action à réaliser, \"add\" pour l\'ajout de numéros, \"del\" pour la suppression de numéros")], repertoireId: Annotated[str, Field(description="Input parameter: repertoireId du répertoire cible")], champ22: Annotated[str, Field(description="Input parameter: Champs U des contacts")], champ6: Annotated[str, Field(description="Input parameter: Champs E des contacts")], champ4: Annotated[str, Field(description="Input parameter: Champs C des contacts")], champ20: Annotated[str, Field(description="Input parameter: Champs S des contacts")], champ10: Annotated[str, Field(description="Input parameter: Champs I des contacts")], champ11: Annotated[str, Field(description="Input parameter: Champs J des contacts")], champ8: Annotated[str, Field(description="Input parameter: Champs G des contacts")], champ17: Annotated[str, Field(description="Input parameter: Champs P des contacts")], champ3: Annotated[str, Field(description="Input parameter: Champs B des contacts")], champ27: Annotated[str, Field(description="Input parameter: Champs Z des contacts")], champ9: Annotated[str, Field(description="Input parameter: Champs H des contacts")], champ19: Annotated[str, Field(description="Input parameter: Champs R des contacts")], champ16: Annotated[str, Field(description="Input parameter: Champs O des contacts")], champ5: Annotated[str, Field(description="Input parameter: Champs D des contacts")], champ24: Annotated[str, Field(description="Input parameter: Champs W des contacts")], champ2: Annotated[str, Field(description="Input parameter: Champs A des contacts")], champ12: Annotated[str, Field(description="Input parameter: Champs K des contacts")], champ21: Annotated[str, Field(description="Input parameter: Champs T des contacts")], champ26: Annotated[str, Field(description="Input parameter: Champs Y des contacts")], champ18: Annotated[str, Field(description="Input parameter: Champs Q des contacts")], champ15: Annotated[str, Field(description="Input parameter: Champs N des contacts")], champ14: Annotated[str, Field(description="Input parameter: Champs M des contacts")], champ25: Annotated[str, Field(description="Input parameter: Champs X des contacts")], num: Annotated[str, Field(description="Input parameter: liste des numéros des téléphone à ajouter ou supprimer")], champ7: Annotated[str, Field(description="Input parameter: Champs F des contacts")], champ13: Annotated[str, Field(description="Input parameter: Champs L des contacts")], champ23: Annotated[str, Field(description="Input parameter: Champs V des contacts")], champ1: Annotated[str, Field(description="Input parameter: Noms des contact")]) -> str:
    """Gestion repertoire (modification)"""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        pass
        # Build request body
        request_data = {
        "keyid": keyid,
        "repertoireEdit": repertoireEdit,
        "repertoireId": repertoireId,
        "champ22": champ22,
        "champ6": champ6,
        "champ4": champ4,
        "champ20": champ20,
        "champ10": champ10,
        "champ11": champ11,
        "champ8": champ8,
        "champ17": champ17,
        "champ3": champ3,
        "champ27": champ27,
        "champ9": champ9,
        "champ19": champ19,
        "champ16": champ16,
        "champ5": champ5,
        "champ24": champ24,
        "champ2": champ2,
        "champ12": champ12,
        "champ21": champ21,
        "champ26": champ26,
        "champ18": champ18,
        "champ15": champ15,
        "champ14": champ14,
        "champ25": champ25,
        "num": num,
        "champ7": champ7,
        "champ13": champ13,
        "champ23": champ23,
        "champ1": champ1
        }
        
        # Remove None values
        request_data = {k: v for k, v in request_data.items() if v is not None}
        
        # Make API call
        url = f"{config.base_url}/repertoire"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.put(url, headers=headers, json=request_data, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to read response body: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to read response body: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Failed to create request: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Failed to create request: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Failed to create request: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def post_smsmulti(gmt_zone: Annotated[str, Field(description="Input parameter: Fuseau horaire de la date d\'envoi")], smslong: Annotated[str, Field(description="Input parameter: Le SMS long permet de dépasser la limite de 160 caractères en envoyant un message constitué de plusieurs SMS. Il est possible d’envoyer jusqu’à 6 SMS concaténés pour une longueur totale maximale de 918 caractères par message. Pour des raisons technique, la limite par SMS concaténé étant de 153 caractères. En cas de modification de l’émetteur, il faut considérer l’ajout automatique de 12 caractères du « STOP SMS ». Pour envoyer un smslong, il faut ajouter le paramètre smslong aux appels. La valeur de SMS doit être le nombre maximum de sms concaténé autorisé. Pour ne pas avoir ce message d’erreur et obtenir un calcul dynamique du nombre de SMS alors il faut renseigner smslong = \"999\"")], date_envoi: Annotated[str, Field(description="Input parameter: Paramètre optionnel, date d\'envoi au format YYYY-MM-DD hh:mm")], emetteur: Annotated[str, Field(description="Input parameter: L\'emetteur doit être une chaîne alphanumérique comprise entre 4 et 11 caractères. Les caractères acceptés sont les chiffres entre 0 et 9, les lettres entre A et Z et l’espace. Il ne peut pas comporter uniquement des chiffres. Pour la modification de l’émetteur et dans le cadre de campagnes commerciales, les opérateurs imposent contractuellement d’ajouter en fin de message le texte suivant : STOP XXXXX De ce fait, le message envoyé ne pourra excéder une longueur de 148 caractères au lieu des 160 caractères, le « STOP » étant rajouté automatiquement.")], nostop: Annotated[str, Field(description="Input parameter: Si le message n’est pas à but commercial, vous pouvez faire une demande pour retirer l’obligation du STOP. Une fois votre demande validée par nos services, vous pourrez supprimer la mention STOP SMS en ajoutant nostop = \"1\"")], numAzur: Annotated[str, Field(description="")], repertoireId: Annotated[str, Field(description="Input parameter: Id du repertoire")], ucs2: Annotated[str, Field(description="Input parameter: Il est également possible d’envoyer des SMS en alphabet non latin (russe, chinois, arabe, etc) sur les numéros hors France métropolitaine. Pour ce faire, la requête devrait être encodée au format UTF-8 et contenir l’argument ucs2 = \"1\" Du fait de contraintes techniques, 1 SMS unique ne pourra pas dépasser 70 caractères (au lieu des 160 usuels) et dans le cas de SMS long, chaque sms ne pourra dépasser 67 caractères.")], keyid: Annotated[str, Field(description="Input parameter: Clé API")], tracker: Annotated[str, Field(description="")], num: Annotated[str, Field(description="")], sms: Annotated[str, Field(description="")]) -> str:
    """Envoyer des SMS"""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        pass
        # Build request body
        request_data = {
        "gmt_zone": gmt_zone,
        "smslong": smslong,
        "date_envoi": date_envoi,
        "emetteur": emetteur,
        "nostop": nostop,
        "numAzur": numAzur,
        "repertoireId": repertoireId,
        "ucs2": ucs2,
        "keyid": keyid,
        "tracker": tracker,
        "num": num,
        "sms": sms
        }
        
        # Remove None values
        request_data = {k: v for k, v in request_data.items() if v is not None}
        
        # Make API call
        url = f"{config.base_url}/smsmulti"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, headers=headers, json=request_data, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to read response body: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to read response body: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Failed to create request: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Failed to create request: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Failed to create request: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def post_sms(keyid: Annotated[str, Field(description="Input parameter: Clé API")], num: Annotated[str, Field(description="Input parameter: Numero de téléphone au format national (exemple 0680010203) ou international (example 33680010203)")], smslong: Annotated[str, Field(description="Input parameter: Le SMS long permet de dépasser la limite de 160 caractères en envoyant un message constitué de plusieurs SMS. Il est possible d’envoyer jusqu’à 6 SMS concaténés pour une longueur totale maximale de 918 caractères par message. Pour des raisons technique, la limite par SMS concaténé étant de 153 caractères. En cas de modification de l’émetteur, il faut considérer l’ajout automatique de 12 caractères du « STOP SMS ». Pour envoyer un smslong, il faut ajouter le paramètre smslong aux appels. La valeur de SMS doit être le nombre maximum de sms concaténé autorisé. Pour ne pas avoir ce message d’erreur et obtenir un calcul dynamique du nombre de SMS alors il faut renseigner smslong = \"999\"")], date_envoi: Annotated[str, Field(description="Input parameter: Date d\'envoi au format YYYY-MM-DD hh:mm . Ce paramètre est optionnel, si il est omis l\'envoi est réalisé immédiatement.")], emetteur: Annotated[str, Field(description="Input parameter: - L\'emetteur doit être une chaîne alphanumérique comprise entre 4 et 11 caractères. - Les caractères acceptés sont les chiffres entre 0 et 9, les lettres entre A et Z et l’espace. - Il ne peut pas comporter uniquement des chiffres. - Pour la modification de l\'émetteur et dans le cadre de campagnes commerciales, les opérateurs imposent contractuellement d\'ajouter en fin de message le texte \"STOP XXXXX\". De ce fait, le message envoyé ne pourra excéder une longueur de 148 caractères au lieu des 160 caractères, le « STOP » étant rajouté automatiquement.")], gmt_zone: Annotated[str, Field(description="Input parameter: Fuseau horaire de la date d\'envoi")], ucs2: Annotated[str, Field(description="Input parameter: Il est également possible d’envoyer des SMS en alphabet non latin (russe, chinois, arabe, etc) sur les numéros hors France métropolitaine. Pour ce faire, la requête devrait être encodée au format UTF-8 et contenir l’argument ucs2 = \"1\" Du fait de contraintes techniques, 1 SMS unique ne pourra pas dépasser 70 caractères (au lieu des 160 usuels) et dans le cas de SMS long, chaque sms ne pourra dépasser 67 caractères.")], tracker: Annotated[str, Field(description="Input parameter: Le tracker doit être une chaine alphanumérique de moins de 50 caractères. Ce tracker sera ensuite renvoyé en paramètre des urls pour les retours des accusés de réception.")], nostop: Annotated[str, Field(description="Input parameter: Si le message n’est pas à but commercial, vous pouvez faire une demande pour retirer l’obligation du STOP. Une fois votre demande validée par nos services, vous pourrez supprimer la mention STOP SMS en ajoutant nostop = \"1\"")], numAzur: Annotated[str, Field(description="")], sms: Annotated[str, Field(description="Input parameter: Message à envoyer aux destinataires. Le message doit être encodé au format utf-8 et ne contenir que des caractères existant dans l\'alphabet GSM. Il est également possible d\'envoyer (à l\'étranger uniquement) des SMS en UCS-2, cf paramètre ucs2 pour plus de détails.")]) -> str:
    """Envoyer un sms"""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        pass
        # Build request body
        request_data = {
        "keyid": keyid,
        "num": num,
        "smslong": smslong,
        "date_envoi": date_envoi,
        "emetteur": emetteur,
        "gmt_zone": gmt_zone,
        "ucs2": ucs2,
        "tracker": tracker,
        "nostop": nostop,
        "numAzur": numAzur,
        "sms": sms
        }
        
        # Remove None values
        request_data = {k: v for k, v in request_data.items() if v is not None}
        
        # Make API call
        url = f"{config.base_url}/sms"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, headers=headers, json=request_data, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to read response body: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to read response body: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Failed to create request: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Failed to create request: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Failed to create request: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def post_shortlink(keyid: Annotated[str, Field(description="")], shortlink: Annotated[str, Field(description="")]) -> str:
    """add a shortlink"""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        pass
        # Build request body
        request_data = {
        "keyid": keyid,
        "shortlink": shortlink
        }
        
        # Remove None values
        request_data = {k: v for k, v in request_data.items() if v is not None}
        
        # Make API call
        url = f"{config.base_url}/shortlink"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, headers=headers, json=request_data, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to read response body: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to read response body: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Failed to create request: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Failed to create request: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Failed to create request: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def post_subaccount(subAccountLogin: Annotated[str, Field(description="")], subAccountPassword: Annotated[str, Field(description="")], keyid: Annotated[str, Field(description="")], subAccountEdit: Annotated[str, Field(description="")]) -> str:
    """Ajoute un sous compte"""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        pass
        # Build request body
        request_data = {
        "subAccountLogin": subAccountLogin,
        "subAccountPassword": subAccountPassword,
        "keyid": keyid,
        "subAccountEdit": subAccountEdit
        }
        
        # Remove None values
        request_data = {k: v for k, v in request_data.items() if v is not None}
        
        # Make API call
        url = f"{config.base_url}/subaccount"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, headers=headers, json=request_data, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to read response body: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to read response body: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Failed to create request: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Failed to create request: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Failed to create request: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def post_getlistenoire(keyid: Annotated[str, Field(description="Clé API")], getListeNoire: Annotated[str, Field(description="Doit valoir \"1\"")]) -> str:
    """Retourne le liste noire"""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        pass
        # Build request body
        request_data = {
        "keyid": keyid,
        "getListeNoire": getListeNoire
        }
        
        # Remove None values
        request_data = {k: v for k, v in request_data.items() if v is not None}
        
        # Make API call
        url = f"{config.base_url}/api/unknown"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, headers=headers, json=request_data, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to format JSON: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to format JSON: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Request failed: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Request failed: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def get_campagne(keyid: Annotated[str, Field(description="Clé API")], rapportCampagne: Annotated[str, Field(description="Doit valoir \"1\"")], date_deb: Annotated[str, Field(description="date de debut au format YYYY-MM-DD hh:mm")], date_fin: Annotated[str, Field(description="date de fin au format YYYY-MM-DD hh:mm")]) -> str:
    """Retourne les SMS envoyés sur une période donnée"""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        if keyid: params["keyid"] = keyid
        if rapportCampagne: params["rapportCampagne"] = rapportCampagne
        if date_deb: params["date_deb"] = date_deb
        if date_fin: params["date_fin"] = date_fin
        
        # Make API call
        url = f"{config.base_url}/api/unknown"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.get(url, headers=headers, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to format JSON: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to format JSON: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Request failed: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Request failed: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def get_credit(keyid: Annotated[str, Field(description="Clé API")], credit: Annotated[str, Field(description="Type de reponse demandée, 1 pour euro, 2 pour euro + estimation quantité")]) -> str:
    """Interrogation credit"""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        if keyid: params["keyid"] = keyid
        if credit: params["credit"] = credit
        
        # Make API call
        url = f"{config.base_url}/api/unknown"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.get(url, headers=headers, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to format JSON: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to format JSON: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Request failed: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Request failed: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def post_setlistenoire(keyid: Annotated[str, Field(description="Clé API")], setlisteNoire: Annotated[str, Field(description="Doit valoir \"1\"")], num: Annotated[str, Field(description="numéro de mobile à insérer en liste noire")]) -> str:
    """Ajoute un numero en liste noire"""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        pass
        # Build request body
        request_data = {
        "keyid": keyid,
        "setlisteNoire": setlisteNoire,
        "num": num
        }
        
        # Remove None values
        request_data = {k: v for k, v in request_data.items() if v is not None}
        
        # Make API call
        url = f"{config.base_url}/api/unknown"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, headers=headers, json=request_data, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to format JSON: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to format JSON: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Request failed: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Request failed: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def post_comptage(nostop: Annotated[str, Field(description="Input parameter: Si le message n’est pas à but commercial, vous pouvez faire une demande pour retirer l’obligation du STOP. Une fois votre demande validée par nos services, vous pourrez supprimer la mention STOP SMS en ajoutant nostop = \"1\"")], num: Annotated[str, Field(description="Input parameter: Numero de téléphone au format national (exemple 0680010203) ou international (example 33680010203)")], sms: Annotated[str, Field(description="Input parameter: Message à envoyer aux destinataires. Le message doit être encodé au format utf-8 et ne contenir que des caractères existant dans l\'alphabet GSM. Il est également possible d\'envoyer (à l\'étranger uniquement) des SMS en UCS-2, cf paramètre ucs2 pour plus de détails.")], tracker: Annotated[str, Field(description="Input parameter: Le tracker doit être une chaine alphanumérique de moins de 50 caractères. Ce tracker sera ensuite renvoyé en paramètre des urls pour les retours des accusés de réception.")], comptage: Annotated[str, Field(description="")], emetteur: Annotated[str, Field(description="Input parameter: - L\'emetteur doit être une chaîne alphanumérique comprise entre 4 et 11 caractères. - Les caractères acceptés sont les chiffres entre 0 et 9, les lettres entre A et Z et l’espace. - Il ne peut pas comporter uniquement des chiffres. - Pour la modification de l\'émetteur et dans le cadre de campagnes commerciales, les opérateurs imposent contractuellement d\'ajouter en fin de message le texte \"STOP XXXXX\". De ce fait, le message envoyé ne pourra excéder une longueur de 148 caractères au lieu des 160 caractères, le « STOP » étant rajouté automatiquement.")], numAzur: Annotated[str, Field(description="")], gmt_zone: Annotated[str, Field(description="Input parameter: Fuseau horaire de la date d\'envoi")], keyid: Annotated[str, Field(description="Input parameter: Clé API")], smslong: Annotated[str, Field(description="Input parameter: Le SMS long permet de dépasser la limite de 160 caractères en envoyant un message constitué de plusieurs SMS. Il est possible d’envoyer jusqu’à 6 SMS concaténés pour une longueur totale maximale de 918 caractères par message. Pour des raisons technique, la limite par SMS concaténé étant de 153 caractères. En cas de modification de l’émetteur, il faut considérer l’ajout automatique de 12 caractères du « STOP SMS ». Pour envoyer un smslong, il faut ajouter le paramètre smslong aux appels. La valeur de SMS doit être le nombre maximum de sms concaténé autorisé. Pour ne pas avoir ce message d’erreur et obtenir un calcul dynamique du nombre de SMS alors il faut renseigner smslong = \"999\"")], ucs2: Annotated[str, Field(description="Input parameter: Il est également possible d’envoyer des SMS en alphabet non latin (russe, chinois, arabe, etc) sur les numéros hors France métropolitaine. Pour ce faire, la requête devrait être encodée au format UTF-8 et contenir l’argument ucs2 = \"1\" Du fait de contraintes techniques, 1 SMS unique ne pourra pas dépasser 70 caractères (au lieu des 160 usuels) et dans le cas de SMS long, chaque sms ne pourra dépasser 67 caractères.")], date_envoi: Annotated[str, Field(description="Input parameter: Date d\'envoi au format YYYY-MM-DD hh:mm . Ce paramètre est optionnel, si il est omis l\'envoi est réalisé immédiatement.")]) -> str:
    """Compter le nombre de caractère"""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        pass
        # Build request body
        request_data = {
        "nostop": nostop,
        "num": num,
        "sms": sms,
        "tracker": tracker,
        "comptage": comptage,
        "emetteur": emetteur,
        "numAzur": numAzur,
        "gmt_zone": gmt_zone,
        "keyid": keyid,
        "smslong": smslong,
        "ucs2": ucs2,
        "date_envoi": date_envoi
        }
        
        # Remove None values
        request_data = {k: v for k, v in request_data.items() if v is not None}
        
        # Make API call
        url = f"{config.base_url}/comptage"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, headers=headers, json=request_data, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to read response body: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to read response body: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Failed to create request: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Failed to create request: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Failed to create request: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def post_hlr(getHLR: Annotated[str, Field(description="Input parameter: Doit valoir \"1\"")], keyid: Annotated[str, Field(description="Input parameter: Clé API")], num: Annotated[str, Field(description="Input parameter: liste de numéros de téléphone")]) -> str:
    """Vérifier la validité d'un numéro"""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        pass
        # Build request body
        request_data = {
        "getHLR": getHLR,
        "keyid": keyid,
        "num": num
        }
        
        # Remove None values
        request_data = {k: v for k, v in request_data.items() if v is not None}
        
        # Make API call
        url = f"{config.base_url}/hlr"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, headers=headers, json=request_data, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to read response body: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to read response body: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Failed to create request: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Failed to create request: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Failed to create request: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def post_dellistenoire(keyid: Annotated[str, Field(description="Clé API")], delListeNoire: Annotated[str, Field(description="Doit valoir \"1\"")], num: Annotated[str, Field(description="numéro de mobile à supprimer")]) -> str:
    """Ajoute un numero en liste noire"""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        pass
        # Build request body
        request_data = {
        "keyid": keyid,
        "delListeNoire": delListeNoire,
        "num": num
        }
        
        # Remove None values
        request_data = {k: v for k, v in request_data.items() if v is not None}
        
        # Make API call
        url = f"{config.base_url}/api/unknown"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, headers=headers, json=request_data, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to format JSON: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to format JSON: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Request failed: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Request failed: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@mcp.tool()
def put_subaccount(subAccountPrice: Annotated[str, Field(description="")], subAccountRestrictionStop: Annotated[str, Field(description="")], subAccountRestrictionTime: Annotated[str, Field(description="")], keyid: Annotated[str, Field(description="Input parameter: Clé API")], subAccountAddCredit: Annotated[str, Field(description="Input parameter: montant du crédit à ajouter")], subAccountCountryCode: Annotated[str, Field(description="")], subAccountEdit: Annotated[str, Field(description="Input parameter: action à réaliser soit setPrice pour définir un prix ou addCredit pour ajouter du credit ou setRestriction modifier la restriction stop /")], subAccountKeyId: Annotated[str, Field(description="Input parameter: keyid du sous-compte")]) -> str:
    """Edit a subaccount"""
    try:
        config = get_config()
        
        if not config.base_url or not config.bearer_token:
            return "Error: Missing API configuration. Please set API_BASE_URL and API_BEARER_TOKEN environment variables."
        
        # Build request parameters
        params = {}
        pass
        # Build request body
        request_data = {
        "subAccountPrice": subAccountPrice,
        "subAccountRestrictionStop": subAccountRestrictionStop,
        "subAccountRestrictionTime": subAccountRestrictionTime,
        "keyid": keyid,
        "subAccountAddCredit": subAccountAddCredit,
        "subAccountCountryCode": subAccountCountryCode,
        "subAccountEdit": subAccountEdit,
        "subAccountKeyId": subAccountKeyId
        }
        
        # Remove None values
        request_data = {k: v for k, v in request_data.items() if v is not None}
        
        # Make API call
        url = f"{config.base_url}/subaccount"
        
        headers = {
            "Authorization": f"Bearer {config.bearer_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.put(url, headers=headers, json=request_data, params=params)
        
        # Handle HTTP errors
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return f"Failed to read response body: {json.dumps(error_data, indent=2)}"
            except json.JSONDecodeError:
                return f"Failed to read response body: {response.text}"
        
        # Parse response
        try:
            result = response.json()
            return json.dumps(result, indent=2)
        except json.JSONDecodeError:
            # Fallback to raw text if JSON parsing fails
            return response.text
            
    except requests.exceptions.ConnectionError as e:
        return f"Failed to create request: Connection error - {str(e)}"
    except requests.exceptions.Timeout as e:
        return f"Failed to create request: Request timeout - {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"Failed to create request: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


if __name__ == "__main__":
    mcp.run()
