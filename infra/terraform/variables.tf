variable "project_name" {
  type        = string
  description = "Project name prefix"
}

variable "environment" {
  type        = string
  description = "Environment name (dev, prod)"
}

variable "location" {
  type        = string
  description = "Azure region"
  default     = "westeurope"
}

variable "resource_group_name" {
  type        = string
  description = "Resource group name"
}

variable "container_image" {
  type        = string
  description = "Container image for FastAPI app"
}

variable "postgres_sku_name" {
  type        = string
  default     = "B_Standard_B1ms"
}

variable "redis_sku_name" {
  type        = string
  default     = "Basic"
}
