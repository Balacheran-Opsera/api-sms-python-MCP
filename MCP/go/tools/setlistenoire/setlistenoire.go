package tools

import (
	"context"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"strings"

	"github.com/api-isendpro/mcp-server/config"
	"github.com/api-isendpro/mcp-server/models"
	"github.com/mark3labs/mcp-go/mcp"
)

func SetlistenoireHandler(cfg *config.APIConfig) func(ctx context.Context, request mcp.CallToolRequest) (*mcp.CallToolResult, error) {
	return func(ctx context.Context, request mcp.CallToolRequest) (*mcp.CallToolResult, error) {
		args, ok := request.Params.Arguments.(map[string]any)
		if !ok {
			return mcp.NewToolResultError("Invalid arguments object"), nil
		}
		queryParams := make([]string, 0)
		if val, ok := args["keyid"]; ok {
			queryParams = append(queryParams, fmt.Sprintf("keyid=%v", val))
		}
		if val, ok := args["setlisteNoire"]; ok {
			queryParams = append(queryParams, fmt.Sprintf("setlisteNoire=%v", val))
		}
		if val, ok := args["num"]; ok {
			queryParams = append(queryParams, fmt.Sprintf("num=%v", val))
		}
		queryString := ""
		if len(queryParams) > 0 {
			queryString = "?" + strings.Join(queryParams, "&")
		}
		url := fmt.Sprintf("%s/setlistenoire%s", cfg.BaseURL, queryString)
		req, err := http.NewRequest("POST", url, nil)
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
		var result models.LISTENOIREReponse
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

func CreateSetlistenoireTool(cfg *config.APIConfig) models.Tool {
	tool := mcp.NewTool("post_setlistenoire",
		mcp.WithDescription("Ajoute un numero en liste noire"),
		mcp.WithString("keyid", mcp.Required(), mcp.Description("Clé API")),
		mcp.WithString("setlisteNoire", mcp.Required(), mcp.Description("Doit valoir \"1\"")),
		mcp.WithString("num", mcp.Required(), mcp.Description("numéro de mobile à insérer en liste noire")),
	)

	return models.Tool{
		Definition: tool,
		Handler:    SetlistenoireHandler(cfg),
	}
}
