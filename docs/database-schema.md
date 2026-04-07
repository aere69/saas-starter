# Full Database Schema Blueprint

Complete relational schema designed for *multi‑tenant SaaS*, *RBAC*, *billing*, and a sample application domain.

## Database Schema

### 1. Tenants

| Field | Type | Notes |
| ----- | ---- | ----- |
| id | UUIS (PK) | Tenant Identifier |
| name | text | Organization Name |
| status | enum(active, suspended) | Lifecycle state |
| created_at | timestamp | |
| updated_at | timestamp | |

### 2. Users

| Field | Type | Notes |
| ----- | ---- | ----- |
| id | UUID (PK) | |
| email | text (unique) | |
| hashed_password | text | |
| is_active | boolean | |
| created_at | timestamp | |

### 3. Tenant Users (Membership)

| Field | Type | Notes |
| ----- | ---- | ----- |
| id | UUID (PK) | |
| tenant_id | UUID (FK -> tenants.id) | |
| user_id | UUID (FK -> users.id) | |
| role_id | UUID (FK -> roles.id) | |
| invited_at | timestamp | |
| joined_at | timestamp | |

Composite unique: `(tenant_id, user_id)`

### 4. Roles

| Field | Type | Notes |
| ----- | ---- | ----- |
| id | UUID (PK) | |
| tenant_id | UUID (FK -> tenants.id) | Roles are tenant-scoped |
| name | text | e.g. admin, member |
| permissions | jsonb | List of permission strings |

### 5. Subscriptions

| Field | Type | Notes |
| ----- | ---- | ----- |
| id | UUID (PK) | |
| tenant_id | UUID (FK -> tenants.id) | |
| stripe_customer_id | text | |
| stripe_subscription_id | text | |
| plan | text | free/pro/enterprise |
| status | enum(active, past_due, canceled) | |
| current-period_end | timestamp | |

### 6. Audit Logs

| Field | Type | Notes |
| ----- | ---- | ----- |
| id | UUID (PK) | |
| tenant_id | UUID (FK -> tenants.id) | |
| user_id | UUID (FK -> users.id) | |
| action | text | |
| metadata | jsonb | |
| created_at | timestamp | |

### 7. Projects (Example Domain)

| Field | Type | Notes |
| ----- | ---- | ----- |
| id | UUID (PK) | |
| tenant_id | UUID (FK -> tenants.id) | |
| name | text | |
| description | text | |
| created_by | UUID (FK -> users.id) | |
| created_at | timestamp | |
| updated_at | timestamp | |

Index: `(tenant_id, name)`

### 8.Row-Level Security (if using RLS)

Example policy:

```sql
CREATE POLICY tenant_isolation ON projects
USING (tenant_id = current_setting(`app.current_tenant`)::uuid);
```

Middleware sets:

```sql
SET app.current_tenant = `<tenant-id>`;
```
