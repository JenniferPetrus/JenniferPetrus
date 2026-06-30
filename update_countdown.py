import datetime
import re
import os

# Dein voraussichtliches Abschlussdatum
end_date = datetime.date(2027, 6, 30)
today = datetime.date.today()

if today < end_date:
    # Berechnung der verbleibenden Zeit
    total_days = (end_date - today).days
    months = total_days // 30
    days = total_days % 30
    
    countdown_text = f"Noch **{months} Monate** und **{days} Tage** bis zum Abschluss! 🚀"
else:
    countdown_text = "Ausbildung erfolgreich beendet! 🎉"

# README.md einlesen
with open('README.md', 'r', encoding='utf-8') as file:
    readme = file.read()

# Den Text zwischen den Markern ersetzen
readme = re.sub(
    r'<!--START_SECTION:countdown-->.*?<!--END_SECTION:countdown-->',
    f'<!--START_SECTION:countdown-->\n⏳ **Ausbildungscountdown:** {countdown_text}\n<!--END_SECTION:countdown-->',
    readme,
    flags=re.DOTALL
)

# README.md wieder speichern
with open('README.md', 'w', encoding='utf-8') as file:
    file.write(readme)
