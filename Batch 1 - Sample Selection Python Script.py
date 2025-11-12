#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 22 14:55:12 2025

@author: benedictsantoso
"""

# Sample Selection Python Script - Randomly Select 100 Companies for Manual Fintech Classification

import pandas as pd
import random

# === Step 1: Load the full company list ===
input_file = "USIPO_processed-w_CIK_20250610_with_Fintech.xlsx"
df = pd.read_excel(input_file)

# === Step 2: Drop duplicates (if any) and shuffle ===
df_sample = df.drop_duplicates().sample(n=100, random_state=42)

# === Step 3: Create new columns for manual classification ===
df_sample["Manual_Fintech_Classification"] = ""
df_sample["Brief_Justification"] = ""

# === Step 4: Save the sample to a new Excel file ===
output_file = "manual_classification_sample.xlsx"
df_sample.to_excel(output_file, index=False)

print(f"\n 100 companies sampled and saved to '{output_file}'")
