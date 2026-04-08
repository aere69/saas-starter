variable "resource_group_name" { type = string }
variable "location" { type = string }
variable "name_prefix" { type = string }
variable "container_image" { type = string }
variable "postgres_connection" { type = string }
variable "redis_connection" { type = string }
variable "keyvault_id" { type = string }
variable "storage_account_name" { type = string }

resource "azurerm_container_app_environment" "env" {
  name                = "${var.name_prefix}-cae"
  location            = var.location
  resource_group_name = var.resource_group_name
}

resource "azurerm_container_app" "api" {
  name                         = "${var.name_prefix}-api"
  resource_group_name          = var.resource_group_name
  container_app_environment_id = azurerm_container_app_environment.env.id
  revision_mode                = "Single"

  template {
    container {
      name   = "api"
      image  = var.container_image
      cpu    = 0.5
      memory = "1Gi"

      env {
        name  = "DATABASE_URL"
        value = var.postgres_connection
      }

      env {
        name  = "REDIS_URL"
        value = var.redis_connection
      }

      env {
        name  = "STORAGE_ACCOUNT_NAME"
        value = var.storage_account_name
      }
    }
  }

  ingress {
    external_enabled = true
    target_port      = 8000
    transport        = "auto"
  }
}

output "api_url" {
  value = azurerm_container_app.api.latest_revision_fqdn
}
