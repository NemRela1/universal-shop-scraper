from typing import Dict, List, Optional
from bs4 import BeautifulSoup
import json
import pandas as pd
import requests


class ShopScraper:
    def __init__(self, user_agent: Optional[str] = None):
        self.headers = {
            "User-Agent": user_agent or "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

    def get_product(self, url: str) -> Dict[str, any]:
        """Extrai dados de produtos usando metadados JSON-LD."""
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            json_data = soup.find("script", {"type": "application/ld+json"})

            if json_data:
                data = json.loads(json_data.string)
                item = data[0] if isinstance(data, list) else data

                # Normalização de dados para diferentes padrões de e-commerce
                offers = item.get("offers", {})
                if isinstance(offers, list): offers = offers[0]

                return {"name": item.get("name"), "price": offers.get("lowPrice") or offers.get("price"),
                    "currency": offers.get("priceCurrency"), "sku": item.get("sku") or item.get("productID"),
                    "brand": item.get("brand", {}).get("name") if isinstance(item.get("brand"), dict) else item.get(
                        "brand"), "availability": "InStock" in str(offers.get("availability")), "url": url}
            return {"error": "Metadata not found", "url": url}
        except Exception as e:
            return {"error": str(e), "url": url}

    def save_to_csv(self, urls: List[str], filename: str = "products.csv"):
        """Processa uma lista de URLs e salva o resultado direto em CSV."""
        results = [self.get_product(u) for u in urls]
        df = pd.DataFrame(results)
        df.to_csv(filename, index=False, encoding='utf-8-sig')
        print(f"✅ Arquivo {filename} gerado com {len(results)} itens!")


if __name__ == "__main__":
    scraper = ShopScraper()
    # Exemplo: Scrape de múltiplos sites com um único comando
    urls = ["https://www.kabum.com.br/produto/626864/...", "https://www.gbarbosa.com.br/..."]
    scraper.save_to_csv(urls)
