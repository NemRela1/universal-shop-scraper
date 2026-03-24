# 🛒 Universal Shop Scraper

[![PyPI version](https://img.shields.io/pypi/v/universal-shop-scraper.svg)](https://pypi.org/project/universal-shop-scraper/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

**Universal Shop Scraper** é uma biblioteca Python focada em **extração confiável e escalável de dados de e-commerce**, utilizando metadados estruturados **JSON-LD (Schema.org)** em vez de scraping tradicional baseado em HTML.

Projetada para cenários reais de **engenharia de dados, monitoramento de preços e inteligência competitiva**.

---

## 🎯 Proposta

Scrapers tradicionais quebram quando o frontend muda.  
Esta biblioteca ignora completamente o layout e extrai diretamente da camada semântica usada por mecanismos de busca.

✔ Menos manutenção  
✔ Mais estabilidade  
✔ Dados estruturados por padrão

---

## ⚙️ Como Funciona

1. Requisição HTTP da página
2. Extração de `<script type="application/ld+json">`
3. Parsing dos dados estruturados
4. Normalização para um formato consistente


---

## 📦 Instalação

```bash
pip install universal-shop-scraper
```

---

## 🔍 Extração de Produto

```python
from universal_shop_scraper import ShopScraper

scraper = ShopScraper()

data = scraper.get_product("https://www.kabum.com.br/produto/626864/")

if "error" not in data:
    print(data)
```

### Exemplo de saída

```json
{
  "name": "Fritadeira Air Fryer Elgin",
  "price": 349.90,
  "currency": "BRL",
  "sku": "1878799",
  "brand": "Elgin",
  "availability": true,
  "url": "https://..."
}
```

---

## 📊 Processamento em Lote

```python
from universal_shop_scraper import ShopScraper

urls = [
    "https://www.gbarbosa.com.br/produto-x",
    "https://www.kabum.com.br/produto-y",
    "https://www.magalu.com.br/produto-z"
]

scraper = ShopScraper()
scraper.save_to_csv(urls, filename="dataset.csv")
```

---

## 🧠 Integração com Data Science

```python
import pandas as pd
from universal_shop_scraper import ShopScraper

urls = [...]
scraper = ShopScraper()

data = [scraper.get_product(url) for url in urls]
df = pd.DataFrame(data)

print(df.head())
```

---

## 📊 Estrutura dos Dados

| Campo        | Tipo   | Descrição                     |
|-------------|--------|------------------------------|
| name        | str    | Nome do produto              |
| price       | float  | Preço                        |
| currency    | str    | Moeda                        |
| sku         | str    | Identificador do produto     |
| brand       | str    | Marca                        |
| availability| bool   | Disponibilidade              |
| url         | str    | URL de origem                |

---

## ⚠️ Limitações

- Nem todos os sites implementam JSON-LD corretamente
- Alguns dados podem estar ausentes ou inconsistentes
- Sites altamente dinâmicos podem não expor metadata no HTML inicial


---

Distribuído sob a licença MIT.
