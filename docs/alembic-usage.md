# Alembic

## ⭐ What Alembic Is (in practical terms)

Alembic is the database migration engine for SQLAlchemy.

It solves one core problem:

>Your database schema changes over time, and you need a safe, versioned, automated way to evolve it across all environments.

**Summary:** Alembic is the schema migration engine that keeps your database in sync with your application code.
It provides versioned, reversible, automated migrations that make your SaaS platform safe, reproducible, and production‑ready.
It belongs at the project root, with migration files stored in `alembic/versions/` and your models in `app/models/`.

## ⭐ Alembic gives you

### ✔ Versioned schema migrations

Every change to your models becomes a migration file with an **upgrade()** and **downgrade()** function.

### ✔ Safe, repeatable deployments

You can apply migrations in:

- Local dev
- Demo mode
- CI pipelines
- Staging
- Production

### ✔ A single source of truth for schema evolution

Your database schema becomes **code**, not tribal knowledge.

### ✔ Rollbacks

If something breaks, you can downgrade to the previous version.

### ✔ Environment‑agnostic

Works with PostgreSQL, MySQL, SQLite, etc.

### ✔ Perfect for multi‑tenant SaaS

You can:

- Run migrations once per shared DB
- Or once per tenant DB (if using DB‑per‑tenant architecture)

### ✔ Perfect for Demo Mode

Your `saasctl demo reset` command uses:

```sh
alembic downgrade base
alembic upgrade head
```

This gives you a **clean, reproducible environment** every time.

## ⭐ Why You Use Alembic (the real reasons)

### 1. Your schema will evolve constantly

New features → new tables, columns, indexes.

Alembic ensures every environment stays in sync.

### 2. Manual SQL is error‑prone

Alembic generates migrations automatically from SQLAlchemy models.

### 3. You need deterministic deployments

CI/CD pipelines rely on Alembic to apply migrations safely.

### 4. You need rollback capability

If a migration breaks production, you can revert.

### 5. You need auditability

Every migration is a file with a timestamp and unique revision ID.

### 6. You need reproducible demo environments

Your demo mode depends on Alembic to rebuild the schema cleanly.

## ⭐ How Alembic Works (under the hood)

### 1. You define your models in SQLAlchemy

Example:

```py
class User(Base):
    id = Column(String, primary_key=True)
    email = Column(String)
```

### 2. Alembic compares your models to the DB

Using `alembic revision --autogenerate`.

### 3. It generates a migration file

Example:

```txt
alembic/versions/20240409_add_users_table.py
```

Inside:

```py
def upgrade():
    op.create_table(...)

def downgrade():
    op.drop_table(...)
```

### 4. You apply migrations

Using:

```txt
alembic upgrade head
```

### 5. Alembic tracks which migrations ran

In a table called:

```txt
alembic_version
```

This ensures migrations run once and in the correct order.

## ⭐ How Alembic Integrates With the SaaS Platform

### ✔ Demo Mode

Your `saasctl demo reset` uses Alembic to rebuild the schema:

```txt
alembic downgrade base
alembic upgrade head
```

### ✔ Synthetic Traffic

Your synthetic traffic generator depends on the schema being correct.

### ✔ Multi‑Tenant Admin Console

Your CRUD operations rely on the schema being up‑to‑date.

### ✔ Billing & Subscription Manager

Your subscription + invoice tables are created via Alembic.

### ✔ Observability

Your trace + event tables (if any) are also managed via Alembic.

### ✔ CI/CD

Your deployment pipeline will run:

```txt
alembic upgrade head
```

before starting the app.
