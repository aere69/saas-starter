locals {
  name_prefix = "${var.project_name}-${var.environment}"
}

resource "azurerm_resource_group" "rg" {
  name     = var.resource_group_name
  location = var.location
}

module "network" {
  source              = "./modules/network"
  resource_group_name = azurerm_resource_group.rg.name
  location            = var.location
  name_prefix         = local.name_prefix
}

module "postgres" {
  source              = "./modules/postgres"
  resource_group_name = azurerm_resource_group.rg.name
  location            = var.location
  name_prefix         = local.name_prefix
  sku_name            = var.postgres_sku_name
}

module "redis" {
  source              = "./modules/redis"
  resource_group_name = azurerm_resource_group.rg.name
  location            = var.location
  name_prefix         = local.name_prefix
  sku_name            = var.redis_sku_name
}

module "keyvault" {
  source              = "./modules/keyvault"
  resource_group_name = azurerm_resource_group.rg.name
  location            = var.location
  name_prefix         = local.name_prefix
}

module "storage" {
  source              = "./modules/storage"
  resource_group_name = azurerm_resource_group.rg.name
  location            = var.location
  name_prefix         = local.name_prefix
}

module "container_apps" {
  source                 = "./modules/container_apps"
  resource_group_name    = azurerm_resource_group.rg.name
  location               = var.location
  name_prefix            = local.name_prefix
  container_image        = var.container_image
  postgres_connection    = module.postgres.connection_string
  redis_connection       = module.redis.connection_string
  keyvault_id            = module.keyvault.id
  storage_account_name   = module.storage.name
}
