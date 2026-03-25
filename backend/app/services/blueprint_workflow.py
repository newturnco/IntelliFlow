from temporalio import workflow
from datetime import timedelta
from langgraph import StateGraph

@workflow.defn
class SalesBlueprintWorkflow:
    @workflow.run
    async def run(self, deal_id: int, tenant_id: str):
        # Full end-to-end journey using LangGraph inside Temporal
        state = {"deal_id": deal_id}
        # ... execute stages with mandatory fields, approvals, AI calls
        return {"status": "completed", "next_action": "send_proposal"}