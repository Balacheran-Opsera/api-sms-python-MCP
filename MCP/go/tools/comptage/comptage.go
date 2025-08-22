package tools

import (
	"context"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"bytes"

	"github.com/api-isendpro/mcp-server/config"
	"github.com/api-isendpro/mcp-server/models"
	"github.com/mark3labs/mcp-go/mcp"
)

func ComptageHandler(cfg *config.APIConfig) func(ctx context.Context, request mcp.CallToolRequest) (*mcp.CallToolResult, error) {
	return func(ctx context.Context, request mcp.CallToolRequest) (*mcp.CallToolResult, error) {
		args, ok := request.Params.Arguments.(map[string]any)
		if !ok {
			return mcp.NewToolResultError("Invalid arguments object"), nil
		}
		// Create properly typed request body using the generated schema
		var requestBody models.ComptageRequest
		
		// Optimized: Single marshal/unmarshal with JSON tags handling field mapping
		if argsJSON, err := json.Marshal(args); err == nil {
			if err := json.Unmarshal(argsJSON, &requestBody); err != nil {
				return mcp.NewToolResultError(fmt.Sprintf("Failed to convert arguments to request type: %v", err)), nil
			}
		} else {
			return mcp.NewToolResultError(fmt.Sprintf("Failed to marshal arguments: %v", err)), nil
		}
		
		bodyBytes, err := json.Marshal(requestBody)
		if err != nil {
			return mcp.NewToolResultErrorFromErr("Failed to encode request body", err), nil
		}
		url := fmt.Sprintf("%s/comptage", cfg.BaseURL)
		req, err := http.NewRequest("POST", url, bytes.NewBuffer(bodyBytes))
		req.Header.Set("Content-Type", "application/json")
		if err != nil {
			return mcp.NewToolResultErrorFromErr("Failed to create request", err), nil
		}
		// No authentication required for this endpoint
		req.Header.Set("Accept", "application/json")

		resp, err := http.DefaultClient.Do(req)
		if err != nil {
			return mcp.NewToolResultErrorFromErr("Request failed", err), nil
		}
		defer resp.Body.Close()

		body, err := io.ReadAll(resp.Body)
		if err != nil {
			return mcp.NewToolResultErrorFromErr("Failed to read response body", err), nil
		}

		if resp.StatusCode >= 400 {
			return mcp.NewToolResultError(fmt.Sprintf("API error: %s", body)), nil
		}
		// Use properly typed response
		var result models.ComptageReponse
		if err := json.Unmarshal(body, &result); err != nil {
			// Fallback to raw text if unmarshaling fails
			return mcp.NewToolResultText(string(body)), nil
		}

		prettyJSON, err := json.MarshalIndent(result, "", "  ")
		if err != nil {
			return mcp.NewToolResultErrorFromErr("Failed to format JSON", err), nil
		}

		return mcp.NewToolResultText(string(prettyJSON)), nil
	}
}

func CreateComptageTool(cfg *config.APIConfig) models.Tool {
	tool := mcp.NewTool("post_comptage",
		mcp.WithDescription("Compter le nombre de caractère "),
		mcp.WithString("nostop", mcp.Description("Input parameter: Si le message n’est pas à but commercial, vous pouvez faire une demande pour retirer l’obligation du STOP. Une fois votre demande validée par nos services, vous pourrez supprimer la mention STOP SMS en ajoutant nostop = \"1\"")),
		mcp.WithString("num", mcp.Required(), mcp.Description("Input parameter: Numero de téléphone au format national (exemple 0680010203) ou international (example 33680010203)")),
		mcp.WithString("sms", mcp.Required(), mcp.Description("Input parameter: Message à envoyer aux destinataires. Le message doit être encodé au format utf-8 et ne contenir que des caractères existant dans l'alphabet GSM. Il est également possible d'envoyer (à l'étranger uniquement) des SMS en UCS-2, cf paramètre ucs2 pour plus de détails.")),
		mcp.WithString("tracker", mcp.Description("Input parameter: Le tracker doit être une chaine alphanumérique de moins de 50 caractères. Ce tracker sera ensuite renvoyé en paramètre des urls pour les retours des accusés de réception. ")),
		mcp.WithString("comptage", mcp.Required(), mcp.Description("")),
		mcp.WithString("emetteur", mcp.Description("Input parameter: - L'emetteur doit être une chaîne alphanumérique comprise entre 4 et 11 caractères.\n\n- Les caractères acceptés sont les chiffres entre 0 et 9, les lettres entre A et Z et l’espace.\n\n- Il ne peut pas comporter uniquement des chiffres. \n\n- Pour la modification de l'émetteur et dans le cadre de campagnes commerciales, les opérateurs imposent contractuellement d'ajouter en fin de message le texte \"STOP XXXXX\". De ce fait, le message envoyé ne pourra excéder une longueur de 148 caractères au lieu des 160 caractères, le « STOP » étant rajouté automatiquement.\n")),
		mcp.WithString("numAzur", mcp.Description("")),
		mcp.WithString("gmt_zone", mcp.Description("Input parameter: Fuseau horaire de la date d'envoi")),
		mcp.WithString("keyid", mcp.Required(), mcp.Description("Input parameter: Clé API")),
		mcp.WithString("smslong", mcp.Description("Input parameter: Le SMS long permet de dépasser la limite de 160 caractères en envoyant un message constitué\nde plusieurs SMS.\nIl est possible d’envoyer jusqu’à 6 SMS concaténés pour une longueur totale maximale de 918\ncaractères par message.\nPour des raisons technique, la limite par SMS concaténé étant de 153 caractères.\nEn cas de modification de l’émetteur, il faut considérer l’ajout automatique de 12 caractères\ndu « STOP SMS ».\nPour envoyer un smslong, il faut ajouter le paramètre smslong aux appels. La valeur de SMS doit être le nombre maximum de sms concaténé autorisé.   Pour ne pas avoir ce message d’erreur et obtenir un calcul dynamique du nombre de SMS alors il faut renseigner smslong = \"999\"\n")),
		mcp.WithString("ucs2", mcp.Description("Input parameter: Il est également possible d’envoyer des SMS en alphabet non latin (russe, chinois, arabe, etc) sur\nles numéros hors France métropolitaine.\nPour ce faire, la requête devrait être encodée au format UTF-8 et contenir l’argument ucs2 = \"1\"\nDu fait de contraintes techniques, 1 SMS unique ne pourra pas dépasser 70 caractères (au lieu\ndes 160 usuels) et dans le cas de SMS long, chaque sms ne pourra dépasser 67 caractères.\n")),
		mcp.WithString("date_envoi", mcp.Description("Input parameter: Date d'envoi au format YYYY-MM-DD hh:mm . Ce paramètre est optionnel, si il est omis l'envoi est réalisé immédiatement.")),
	)

	return models.Tool{
		Definition: tool,
		Handler:    ComptageHandler(cfg),
	}
}
