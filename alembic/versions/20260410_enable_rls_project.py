from alembic import op


revision = "20260410_enable_rls_project"
down_revision = "001_initial"
branch_labels = None
depends_on = None


def upgrade():
    # Enable RLS
    op.execute("ALTER TABLE project ENABLE ROW LEVEL SECURITY;")

    # Create tenant isolation policy
    op.execute("""
        CREATE POLICY tenant_isolation ON project
        USING (tenant_id = current_setting('app.current_tenant')::uuid);
    """)


def downgrade():
    op.execute("DROP POLICY IF EXISTS tenant_isolation ON project;")
    op.execute("ALTER TABLE project DISABLE ROW LEVEL SECURITY;")
