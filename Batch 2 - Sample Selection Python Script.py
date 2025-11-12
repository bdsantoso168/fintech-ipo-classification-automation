#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 30 10:01:51 2025

@author: benedictsantoso
"""

import pandas as pd
import random

# Load the master file containing all IPO companies
master_file_path = "USIPO_processed-w_CIK_20250610_with_Fintech.xlsx"
df_master = pd.read_excel(master_file_path)

# Load the previously selected batch (Batch 1)
batch1_file_path = "Batch 1 - manual_classification_sample.xlsx"
df_batch1 = pd.read_excel(batch1_file_path)

# Standardize company names for comparison (lowercase, stripped)
master_names = df_master['NINAMES'].str.lower().str.strip()
batch1_names = df_batch1['NINAMES'].str.lower().str.strip()

# Filter out companies already in Batch 1
df_remaining = df_master[~master_names.isin(batch1_names)]

# Randomly sample 100 new companies from the remaining set
new_sample = df_remaining.sample(n=100, random_state=42).reset_index(drop=True)

# Save the new sample to a file
new_sample.to_excel("Batch 2 - manual_classification_sample.xlsx", index=False)

print("✅ New batch of 100 companies selected and saved to 'Batch 2 - manual_classification_sample.xlsx'")
