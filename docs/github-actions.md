# GitHub Actions CI/CD for SaaS Multi-Tenant Platform

Two workflows are created:

1. *ci.yml* -> Runs on PR and pushes
2. *cd.yml* -> Deploys to Azure using Terraform (dev/prod)

## CI

📁 `.github/workflows/ci.yml`

This workflow:

- Installs Python
- Installs dependencies
- Runs linting (ruff)
- Runs type checking (mypy)
- Runs tests (pytest)
- Builds Docker image
- Pushes to GitHub Container Registry (GHCR)

## CD

📁 `.github/workflows/cd.yml`

This workflow:

- Deploys to Azure
- Runs Terraform init/plan/apply
- Uses environment‑specific variables
- Deploys the container image built in CI

It supports dev and prod via GitHub Environments.

## 🔐 Required GitHub Secrets

Configure these secrets:

| Secret | Purpose |
| ------ | ------- |
| `AZURE_CREDENTIALS` | Service principal JSON for Azure login |
| `TFSTATE_RG` | Resource group for Terraform state |
| `TFSTATE_STORAGE` | Storage account for Terraform state |
| `GHCR_PAT` (optional) | If pushing to GHCR from outside GitHub token scope |

Azure credentials example (store as JSON in secret):

```json
{
  "clientId": "xxxx",
  "clientSecret": "xxxx",
  "subscriptionId": "xxxx",
  "tenantId": "xxxx"
}
```

## 🚀 Deployment Flow

### 1. Developer pushes to `dev` branch

CI runs → tests → builds → pushes image → ready for deploy.

### 2. Deploy to dev

Manual trigger:

```txt
Actions → CD → Run workflow → environment: dev
```

### 3. Promote to prod

Same workflow:

```txt
Actions → CD → Run workflow → environment: prod
```
