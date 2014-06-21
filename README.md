# Metin2 Login Interface

Dieses Projekt stellt ein Login-Interface für Metin2 P-Server bereit, ursprünglich veröffentlicht auf elitepvpers ([Beitrag vom 21.06.2014](https://www.elitepvpers.com/forum/metin2-pserver-designs-websites-scripts/3310474-release-login-interface.html)).

## Inhalt

Die ZIP-Datei enthält folgende Hauptbestandteile:

- **lib/s_info.py** – Python-Modul zur Serverinfo-Verwaltung.
- **locale_de/** – Lokalisierte UI-Dateien und Bilder:
  - `login.jpg`, `login.sub` – Login-Grafiken.
  - Ladebildschirme: `loading0.jpg` bis `loading3.jpg` inkl. zugehöriger `.sub`-Dateien.
  - `.tga`-Dateien für UI-Elemente (Kanäle, Verbinden, usw.)
  - `loadingwindow.py`, `loginwindow.py` – Python UI-Skripte.

## Verwendung

1. **Einbindung ins Client-Dateisystem**: Die `locale_de`-Ordnerstruktur muss entsprechend in den Clientordner kopiert werden.
2. **Anpassung von UI-Skripten**: Inhalte der `*.py`-Dateien ggf. an die eigene Serverkonfiguration anpassen.
3. **TGA- und JPG-Dateien**: Diese Dateien müssen korrekt mit den zugehörigen `.sub`-Dateien verknüpft sein.

## Autor & Quelle

- Originallink: [elitepvpers Beitrag](https://www.elitepvpers.com/forum/metin2-pserver-designs-websites-scripts/3310474-release-login-interface.html)
