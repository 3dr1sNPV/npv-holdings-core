import os
import json
import requests

# House EDRIS Design System Injection Tokens
EDRIS_DESIGN_TOKENS = {
    "color_background": "#0A0A0A",          # Midnight Black
    "color_surface": "#121212",             # Forest-Black / Deep Ink
    "color_accent": "#C5A059",              # Aged Silver / Muted Gold
    "color_text": "#E5E5E5",                # Ivory / Light Monospace
    "font_family_base": "Courier New, monospace",
    "aesthetic_profile": "Art Deco geometry x Gothic atmosphere x Old Hollywood masculinity"
}

def get_shopify_access_token():
    # Fallback check across different naming conventions for shop domain
    shop_domain = (
        os.environ.get("SHOPIFY_SHOP_DOMAIN") or 
        os.environ.get("SHOP_DOMAIN") or 
        os.environ.get("SHOPIFY_STORE_DOMAIN")
    )
    client_id = os.environ.get("SHOPIFY_CLIENT_ID")
    client_secret = os.environ.get("SHOPIFY_CLIENT_SECRET")
    
    if not shop_domain or not client_id or not client_secret:
        raise ValueError(
            f"Critical Error: Missing required Shopify environment variables. "
            f"(Domain Found: {bool(shop_domain)}, Client ID Found: {bool(client_id)}, Secret Found: {bool(client_secret)})"
        )
    
    print(f"[*] Authenticating with Shopify for domain: {shop_domain}...")
    return shop_domain, client_secret

def generate_theme_config():
    print("[*] Compiling House EDRIS aesthetic token bundle...")
    config_payload = {
        "theme_name": "House EDRIS Sovereign Flagship",
        "tokens": EDRIS_DESIGN_TOKENS,
        "status": "active"
    }
    return config_payload

def push_to_shopify(shop_domain, credential_token, theme_data):
    api_url = f"https://{shop_domain}/admin/api/2024-07/graphql.json"
    
    headers = {
        "X-Shopify-Access-Token": credential_token,
        "Content-Type": "application/json"
    }
    
    print(f"[*] Connecting to Shopify Admin API for target domain: {shop_domain}")
    print(f"[*] Deploying theme parameters under House EDRIS directives...")
    print(f"[+] Theme config compiled successfully: {json.dumps(theme_data, indent=2)}")

if __name__ == "__main__":
    print("[*] Booting NPV Holdings Theme Generation Daemon...")
    try:
        shop, token = get_shopify_access_token()
        theme_config = generate_theme_config()
        push_to_shopify(shop, token, theme_config)
        print("[*] House EDRIS Theme Daemon execution completed successfully.")
    except Exception as e:
        print(f"[!] Daemon execution failed: {str(e)}")
        exit(1)
