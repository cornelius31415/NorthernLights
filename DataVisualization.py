#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 07:42:47 2024

@author: cornelius
"""
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Lade die Daten (ersetze 'file_path' durch den tatsächlichen Dateipfad)
file_path = 'solar_data_kp_values.csv'
data = pd.read_csv(file_path)

# Berechne den täglichen Durchschnitt der KP-Werte
kp_columns = ["Kp1", "Kp2", "Kp3", "Kp4", "Kp5", "Kp6", "Kp7", "Kp8"]
data['average_kp'] = data[kp_columns].mean(axis=1)

# Erstelle eine Datums-Spalte
data['date'] = pd.to_datetime(data[['year', 'month', 'day']])

# Filter für November 2023 bis Oktober 2024
start_date = datetime(2013, 11, 1)
end_date = datetime(2014, 10, 31)
data_last_year = data[(data['date'] >= start_date) & (data['date'] <= end_date)]

# Gruppiere die Daten nach Monat und sortiere chronologisch
data_last_year['year_month'] = data_last_year['date'].dt.to_period('M')
monthly_data = data_last_year.groupby('year_month')

# Setze das Rasterlayout
fig, axs = plt.subplots(3, 4, figsize=(18, 12), sharey=True)
fig.suptitle('Daily Average KP Values from November 2023 to October 2024', fontsize=16, y=1.05)

# Iteriere in chronologischer Reihenfolge
for i, (period, month_data) in enumerate(monthly_data):
    ax = axs[i // 4, i % 4]
    ax.plot(month_data['date'], month_data['average_kp'], color='blue', linewidth=0.7)
    ax.set_title(f'{period.strftime("%B %Y")}', fontsize=12, pad=20)
    ax.set_xlabel('')  # Entfernt die x-Achsen-Beschriftungen
    ax.set_ylabel('Avg KP Value', fontsize=10)
    ax.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)  # Entfernt die x-Ticks
    ax.tick_params(axis='y', labelsize=8)
    ax.grid(True)

# Zusätzlicher Abstand zwischen den Subplots
plt.subplots_adjust(hspace=0.6, wspace=0.4)
plt.tight_layout(rect=[0, 0, 1, 0.96])  # Platz für den Gesamttitel
plt.show()
























