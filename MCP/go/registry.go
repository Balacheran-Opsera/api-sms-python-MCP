package main

import (
	"github.com/api-isendpro/mcp-server/config"
	"github.com/api-isendpro/mcp-server/models"
	tools_sms "github.com/api-isendpro/mcp-server/tools/sms"
	tools_credit "github.com/api-isendpro/mcp-server/tools/credit"
	tools_dellistenoire "github.com/api-isendpro/mcp-server/tools/dellistenoire"
	tools_hlr "github.com/api-isendpro/mcp-server/tools/hlr"
	tools_campagne "github.com/api-isendpro/mcp-server/tools/campagne"
	tools_repertoire "github.com/api-isendpro/mcp-server/tools/repertoire"
	tools_add_subaccount "github.com/api-isendpro/mcp-server/tools/add_subaccount"
	tools_edit_subaccount "github.com/api-isendpro/mcp-server/tools/edit_subaccount"
	tools_getlistenoire "github.com/api-isendpro/mcp-server/tools/getlistenoire"
	tools_comptage "github.com/api-isendpro/mcp-server/tools/comptage"
	tools_setlistenoire "github.com/api-isendpro/mcp-server/tools/setlistenoire"
	tools_add_shortlink "github.com/api-isendpro/mcp-server/tools/add_shortlink"
)

func GetAll(cfg *config.APIConfig) []models.Tool {
	return []models.Tool{
		tools_sms.CreateSendsmsTool(cfg),
		tools_sms.CreateSendsmsmultiTool(cfg),
		tools_credit.CreateGetcreditTool(cfg),
		tools_dellistenoire.CreateDellistenoireTool(cfg),
		tools_hlr.CreateGethlrTool(cfg),
		tools_campagne.CreateGetcampagneTool(cfg),
		tools_repertoire.CreateRepertoirecreaTool(cfg),
		tools_repertoire.CreateRepertoireTool(cfg),
		tools_add_subaccount.CreateSubaccountaddTool(cfg),
		tools_edit_subaccount.CreateSubaccounteditTool(cfg),
		tools_getlistenoire.CreateGetlistenoireTool(cfg),
		tools_comptage.CreateComptageTool(cfg),
		tools_setlistenoire.CreateSetlistenoireTool(cfg),
		tools_add_shortlink.CreateAddshortlinkTool(cfg),
	}
}
