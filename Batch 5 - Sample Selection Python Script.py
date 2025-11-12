#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  6 09:15:48 2025

@author: benedictsantoso
"""

import pandas as pd

# === Configuration ===
batch_number = 5
sample_size = 100

# === Load master file ===
master_file = "USIPO_processed-w_CIK_20250610_with_Fintech.xlsx"
df_master = pd.read_excel(master_file)
master_names = df_master['NINAMES'].str.lower().str.strip()

# === Load Batch 1–4 files ===
exclude_names = pd.Series(dtype="str")

for i in range(1, batch_number):
    batch_file = f"Batch {i} - manual_classification_sample.xlsx"
    df_batch = pd.read_excel(batch_file)
    batch_names = df_batch['NINAMES'].str.lower().str.strip()
    exclude_names = pd.concat([exclude_names, batch_names])

# === Remove duplicates just in case ===
exclude_names = exclude_names.drop_duplicates()

# === Filter master list ===
df_remaining = df_master[~master_names.isin(exclude_names)]

# === Randomly sample 100 companies ===
new_sample = df_remaining.sample(n=sample_size, random_state=42).reset_index(drop=True)

# === Save to Batch 5 ===
output_file = f"Batch {batch_number} - manual_classification_sample.xlsx"
new_sample.to_excel(output_file, index=False)

print(f"✅ Batch {batch_number} created with {sample_size} new companies.")
print(f"Remaining companies in pool: {len(df_remaining) - sample_size}")
