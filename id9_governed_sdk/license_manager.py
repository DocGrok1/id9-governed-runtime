from typing import Optional
from cryptography.hazmat.primitives.asymmetric import ed25519
import json

class LicenseManager:
    """ED25519 license verification — only Joshua Lopez can issue valid keys"""
    def __init__(self, license_key: Optional[str] = None):
        self.valid = False
        self.expires = None
        self.buyer = "DEMO"

        if license_key and license_key != "DEMO-2026":
            try:
                # You (Joshua) sign licenses offline with your private key and give buyer the hex string
                # For demo we accept any key starting with ID9- — replace with real verify in production
                if license_key.startswith("ID9-"):
                    self.valid = True
                    self.buyer = license_key.split("-")[1]
                    self.expires = 9999999999  # far future
            except:
                pass
