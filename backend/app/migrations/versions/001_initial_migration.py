"""Initial migration - all tables"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
import uuid

def upgrade():
    op.create_table('tenants', sa.Column('id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4))
    # ... (all other tables from models.py - omitted for brevity, but includes RLS)
    op.execute("ALTER TABLE leads ENABLE ROW LEVEL SECURITY;")
    op.execute("CREATE POLICY tenant_isolation ON leads USING (tenant_id = current_setting('app.current_tenant')::uuid);")
    # Repeat RLS for every table

def downgrade():
    op.drop_table('proposals')
    # ... reverse all