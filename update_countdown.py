import datetime
import re
import os

# Dein voraussichtliches Abschlussdatum
end_date = datetime.date(2027, 6, 30)
start_date = datetime.date(2025, 9, 1)  # Für die Fortschrittsberechnung
today = datetime.date.today()

if today < end_date:
    # Berechnung der verbleibenden Zeit
    total_days = (end_date - today).days
    months = total_days // 30
    days = total_days % 30
    
    # Berechnung des Fortschritts
    total_duration_days = (end_date - start_date).days
    elapsed_days = (today - start_date).days
    progress_percent = (elapsed_days / total_duration_days) * 100
    
    # Generierung des Ladebalkens
    bar_length = 25
    filled_length = int(progress_percent / 100 * bar_length)
    bar = '█' * filled_length + '░' * (bar_length - filled_length)
    
    countdown_text = f"⏳ **Time until Graduation (Est. June 2027):**<br />Approximately **{months} months** and **{days} days** remaining! 🚀<br /><code>{bar}</code> **{progress_percent:.1f} %** completed"
else:
    countdown_text = "🎉 **Apprenticeship successfully completed!** 🥳"

# README.md einlesen
with open('README.md', 'r', encoding='utf-8') as file:
    readme = file.read()

# Den Text zwischen den Markern ersetzen
readme = re.sub(
    r'<!--START_SECTION:countdown-->.*?<!--END_SECTION:countdown-->',
    f'<!--START_SECTION:countdown-->\n{countdown_text}\n<!--END_SECTION:countdown-->',
    readme,
    flags=re.DOTALL
)

# README.md wieder speichern
with open('README.md', 'w', encoding='utf-8') as file:
    file.write(readme)
