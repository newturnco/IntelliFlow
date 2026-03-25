import asyncio
from temporalio.client import Client
from temporalio.worker import Worker
from .blueprint_workflow import sales_blueprint_workflow  # LangGraph + Temporal

async def main():
    client = await Client.connect("temporal:7233")
    worker = Worker(
        client,
        task_queue="crm-tasks",
        workflows=[sales_blueprint_workflow],
        activities=[]  # add your activities here
    )
    await worker.run()

if __name__ == "__main__":
    asyncio.run(main())