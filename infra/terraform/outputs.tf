output "api_url" {
  value       = module.container_apps.api_url
  description = "Public URL of the FastAPI application"
}

output "postgres_fqdn" {
  value = module.postgres.fqdn
}

output "redis_hostname" {
  value = module.redis.hostname
}
