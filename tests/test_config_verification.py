# tests/test_config_verification.py
import pytest
from config.base_config import config

class TestConfigVerification:
    """Test that configuration is properly loaded from .env and json files"""
    
    def test_environment_config_loaded(self):
        """Verify that environment configuration is loaded correctly"""
        print(f"\n🔧 Testing configuration for: {config.environment.upper()} environment")
        
        # Test environment detection
        assert config.environment == "qa", f"Expected 'qa' environment, got '{config.environment}'"
        print("✅ Environment correctly set to 'qa'")
        
        # Test URL from qa.json
        assert config.base_url, "Base URL not loaded from qa.json"
        assert "qa" in config.base_url.lower() or "test" in config.base_url.lower(), \
               f"URL doesn't seem like QA environment: {config.base_url}"
        print(f"✅ QA URL loaded: {config.base_url}")
        
        # Test other settings from qa.json
        assert hasattr(config, 'timeout'), "Timeout not loaded from qa.json"
        print(f"✅ Timeout setting: {config.timeout} seconds")
    
    def test_credentials_loaded_from_env(self):
        """Verify that credentials are loaded from .env file"""
        print("\n🔐 Testing credential loading from .env")
        
        # Test username loading
        username = config.get_username()
        assert username, "Username not loaded from .env file"
        assert "@" in username, f"Username doesn't look like email: {username}"
        assert "qa" in username.lower() or "test" in username.lower(), \
               f"Username doesn't seem like QA account: {username}"
        print(f"✅ Username loaded: {username}")
        
        # Test password loading  
        password = config.get_password()
        assert password, "Password not loaded from .env file"
        assert len(password) >= 8, "Password seems too short"
        print("✅ Password loaded: [SECRET]")
        
        # Verify they're NOT hardcoded values
        assert username != "test_username@qa.com", "Username is hardcoded, not from .env!"
        assert password != "test_password123", "Password is hardcoded, not from .env!"
        print("✅ Credentials are from .env file, not hardcoded")

    def test_configuration_values(self):
        """Display all configuration values for verification"""
        print(f"\n📋 Configuration Summary for {config.environment.upper()}:")
        print(f"   Base URL: {config.base_url}")
        print(f"   Timeout: {getattr(config, 'timeout', 'Not set')}")
        print(f"   Username: {config.get_username()}")
        print(f"   Password: {'*' * len(config.get_password()) if config.get_password() else 'Not set'}")
        print(f"   Headless: {getattr(config, 'headless', 'Not set')}")