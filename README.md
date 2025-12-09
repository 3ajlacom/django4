# MCP Project - Model Context Protocol Servers

Ce projet contient plusieurs serveurs MCP (Model Context Protocol) pour interagir avec des LLMs comme Claude Desktop.

## Serveurs MCP

### 1. Calculator Server (`main.py`)
Serveur de calcul mathématique avec les outils:
- `add` - Addition de deux nombres
- `subtract` - Soustraction de deux nombres
- `multiply` - Multiplication de deux nombres
- `divide` - Division de deux nombres
- `say_hello` - Dire bonjour à quelqu'un

### 2. Flights Server (`flights_server.py`)
Serveur de gestion de vols avec les outils:
- `find_flight` - Trouve un vol par son numéro
- `flights_to` - Liste les vols vers une destination
- `flights_by_status` - Filtre les vols par statut
- `get_flight_statistics` - Statistiques sur les vols
- Resource: `flights://data` - Accès aux données JSON des vols

### 3. OpenLibrary Server (`openlibrary_mcp.py`)
Serveur d'accès à l'API OpenLibrary avec les outils:
- `search_books` - Recherche de livres
- `get_book_details` - Détails d'un livre spécifique

## Installation

```bash
# Installer uv (gestionnaire de paquets Python)
pip install uv

# Installer les dépendances
uv sync
```

## Configuration Claude Desktop

Ajoutez dans `~/.config/Claude/claude_desktop_config.json` (ou `%APPDATA%\Claude\claude_desktop_config.json` sur Windows):

```json
{
  "mcpServers": {
    "mcp-project": {
      "command": "python",
      "args": ["path/to/main.py"]
    },
    "flights": {
      "command": "python",
      "args": ["path/to/flights_server.py"]
    },
    "openlibrary": {
      "command": "python",
      "args": ["path/to/openlibrary_mcp.py"]
    }
  }
}
```

## Test avec l'inspecteur MCP

```bash
npx @modelcontextprotocol/inspector uv run main.py
```

## Exemples d'utilisation dans Claude

**Calculatrice:**
- "Calcule 25 + 17"
- "Multiplie 8 par 9"

**Vols:**
- "Trouve le vol AF1234"
- "Montre-moi les vols retardés"
- "Donne-moi les statistiques des vols"

**Livres:**
- "Cherche des livres sur Python"
- "Trouve des livres de Harry Potter"
