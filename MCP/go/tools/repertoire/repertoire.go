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

func RepertoireHandler(cfg *config.APIConfig) func(ctx context.Context, request mcp.CallToolRequest) (*mcp.CallToolResult, error) {
	return func(ctx context.Context, request mcp.CallToolRequest) (*mcp.CallToolResult, error) {
		args, ok := request.Params.Arguments.(map[string]any)
		if !ok {
			return mcp.NewToolResultError("Invalid arguments object"), nil
		}
		// Create properly typed request body using the generated schema
		var requestBody models.REPERTOIREmodifrequest
		
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
		url := fmt.Sprintf("%s/repertoire", cfg.BaseURL)
		req, err := http.NewRequest("PUT", url, bytes.NewBuffer(bodyBytes))
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
		var result models.REPERTOIREmodifreponse
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

func CreateRepertoireTool(cfg *config.APIConfig) models.Tool {
	tool := mcp.NewTool("put_repertoire",
		mcp.WithDescription("Gestion repertoire (modification)"),
		mcp.WithArray("champ22", mcp.Description("Input parameter: Champs U des contacts")),
		mcp.WithArray("champ6", mcp.Description("Input parameter: Champs E des contacts")),
		mcp.WithArray("champ4", mcp.Description("Input parameter: Champs C des contacts")),
		mcp.WithArray("champ20", mcp.Description("Input parameter: Champs S des contacts")),
		mcp.WithString("keyid", mcp.Required(), mcp.Description("Input parameter: Clé API")),
		mcp.WithArray("champ10", mcp.Description("Input parameter: Champs I des contacts")),
		mcp.WithArray("champ11", mcp.Description("Input parameter: Champs J des contacts")),
		mcp.WithArray("champ8", mcp.Description("Input parameter: Champs G des contacts")),
		mcp.WithString("repertoireEdit", mcp.Required(), mcp.Description("Input parameter: action à réaliser, \"add\" pour l'ajout de numéros, \"del\" pour la suppression de numéros")),
		mcp.WithArray("champ17", mcp.Description("Input parameter: Champs P des contacts")),
		mcp.WithArray("champ3", mcp.Description("Input parameter: Champs B des contacts")),
		mcp.WithArray("champ27", mcp.Description("Input parameter: Champs Z des contacts")),
		mcp.WithArray("champ9", mcp.Description("Input parameter: Champs H des contacts")),
		mcp.WithArray("champ19", mcp.Description("Input parameter: Champs R des contacts")),
		mcp.WithArray("champ16", mcp.Description("Input parameter: Champs O des contacts")),
		mcp.WithArray("champ5", mcp.Description("Input parameter: Champs D des contacts")),
		mcp.WithArray("champ24", mcp.Description("Input parameter: Champs W des contacts")),
		mcp.WithArray("champ2", mcp.Description("Input parameter: Champs A des contacts")),
		mcp.WithArray("champ12", mcp.Description("Input parameter: Champs K des contacts")),
		mcp.WithArray("champ21", mcp.Description("Input parameter: Champs T des contacts")),
		mcp.WithArray("champ26", mcp.Description("Input parameter: Champs Y des contacts")),
		mcp.WithArray("champ18", mcp.Description("Input parameter: Champs Q des contacts")),
		mcp.WithArray("champ15", mcp.Description("Input parameter: Champs N des contacts")),
		mcp.WithArray("champ14", mcp.Description("Input parameter: Champs M des contacts")),
		mcp.WithArray("champ25", mcp.Description("Input parameter: Champs X des contacts")),
		mcp.WithArray("num", mcp.Required(), mcp.Description("Input parameter: liste des numéros des téléphone à ajouter ou supprimer")),
		mcp.WithArray("champ7", mcp.Description("Input parameter: Champs F des contacts")),
		mcp.WithArray("champ13", mcp.Description("Input parameter: Champs L des contacts")),
		mcp.WithArray("champ23", mcp.Description("Input parameter: Champs V des contacts")),
		mcp.WithArray("champ1", mcp.Description("Input parameter: Noms des contact")),
		mcp.WithString("repertoireId", mcp.Required(), mcp.Description("Input parameter: repertoireId du répertoire cible")),
	)

	return models.Tool{
		Definition: tool,
		Handler:    RepertoireHandler(cfg),
	}
}
