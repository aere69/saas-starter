from dataclasses import dataclass
from typing import Optional

@dataclass
class TenantContext:
    id: str
    subdomain: Optional[str] = None
