variable "resource_group_name" { type = string }
variable "location" { type = string }
variable "name_prefix" { type = string }
variable "sku_name" { type = string }

resource "azurerm_postgresql_flexible_server" "db" {
  name                = "${var.name_prefix}-pg"
  resource_group_name = var.resource_group_name
  location            = var.location
  sku_name            = var.sku_name
  storage_mb          = 32768
  version             = "14"

  administrator_login          = "pgadmin"
  administrator_login_password = "ChangeMe123!" # replace with Key Vault / var
}
# (In a real setup you’d wire password via Key Vault or TF vars, but this is enough for the repo.)

resource "azurerm_postgresql_flexible_server_database" "app" {
  name      = "appdb"
  server_id = azurerm_postgresql_flexible_server.db.id
}

output "connection_string" {
  value = "postgresql://pgadmin:ChangeMe123!@${azurerm_postgresql_flexible_server.db.fqdn}:5432/appdb"
}

output "fqdn" {
  value = azurerm_postgresql_flexible_server.db.fqdn
}
