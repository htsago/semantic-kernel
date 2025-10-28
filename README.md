# Semantic Kernel - Minimaler Konsolenchat

Dieses Projekt zeigt einen minimalen Konsolenchat mit Semantic Kernel und Groq

## Projektstruktur

```
.
├── test.py      # Hauptskript – interaktiver Konsolenchat
└── README.md    # Diese Datei
```

## Funktionsumfang

- Interaktiver Konsolenchat mit Groq-kompatiblem OpenAI-Endpoint
- Chat-Verlauf, Befehle: `exit`/`quit`/`bye`/`q`, `clear`

## Features

1. Minimaler Setup ohne Plugins/Tools
2. Klarer Konsolenflow mit Chat-Verlauf

## Verwendung

```bash
python test.py
```

Das Skript startet einen **interaktiven Chat-Modus** in der Konsole:

1. **Interaktiver Chat**: Sie können Fragen stellen und erhalten Antworten
2. **Ohne Plugins**: Der Chat nutzt ausschließlich das LLM
3. **Chat-Befehle**:
   - `exit`, `quit`, `bye` oder `q` - Beendet das Programm
   - `clear` - Löscht den Chat-Verlauf

### Beispiel-Interaktion:

```
👤 Sie: Was kann dieses Programm?
🤖 Bot: Ich bin ein minimaler Chat-Assistent ohne Plugins. Stelle mir Fragen!
```

## Anforderungen

- Python 3.x
- semantic-kernel
- python-dotenv
- Groq API Key

## Installation

```bash
# Dependencies installieren
pip install -r requirements.txt

# .env Datei erstellen
cp .env.example .env

# API Key in .env eintragen
# Öffne .env und füge deinen Groq API Key ein:
# GROQ_API_KEY=dein_api_key_hier

## Hinweise

- Für Planner/Plugins kann der Chat später erweitert werden.

