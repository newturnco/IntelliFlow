# IntelliFlow CRM - Production SaaS

AI-Driven Multitenant CRM | Full Customer Lifecycle Automation

## Tech Stack
- Backend: FastAPI + PostgreSQL + Redis + LangChain
- Frontend: Next.js 15 (App Router) + Tailwind + shadcn/ui
- Storage: AWS S3 / Wasabi / Azure Blob / Cloudflare R2 (pluggable per tenant)
- AI: OpenAI GPT-4o / Grok / Claude (configurable)
- Orchestration: Temporal.io (optional, included)
- Multitenancy: Row-Level Security + tenant_id on every table

## Quick Deploy on Ubuntu VM (10 minutes)

```bash
sudo bash scripts/setup-ubuntu-vm.sh