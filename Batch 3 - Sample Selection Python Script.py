#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  2 09:45:19 2025

@author: benedictsantoso
"""

import pandas as pd
import random

# Load the master file containing all IPO companies
master_file_path = "USIPO_processed-w_CIK_20250610_with_Fintech.xlsx"
df_master = pd.read_excel(master_file_path)

# Load the previously selected batch (Batch 1) # Add more as Batch Progress
batch1_file_path = "Batch 1 - manual_classification_sample.xlsx"
df_batch1 = pd.read_excel(batch1_file_path)

batch2_file_path = "Batch 2 - manual_classification_sample.xlsx"
df_batch2 = pd.read_excel(batch2_file_path)

# Standardize company names for comparison (lowercase, stripped) 
master_names = df_master['NINAMES'].str.lower().str.strip()
batch1_names = df_batch1['NINAMES'].str.lower().str.strip()  #Add more as Batch Progress
batch2_names = df_batch2['NINAMES'].str.lower().str.strip()

# Filter out companies already in Batch 1, and 2
exclude_names = pd.concat([batch1_names, batch2_names]) #Add more as Batch Progress
df_remaining = df_master[~master_names.isin(exclude_names)]

# Randomly sample 100 new companies from the remaining set
new_sample = df_remaining.sample(n=100, random_state=42).reset_index(drop=True)

# Save the new sample to a file
new_sample.to_excel("Batch 3 - manual_classification_sample.xlsx", index=False)

print("✅ New batch of 100 companies selected and saved to 'Batch 3 - manual_classification_sample.xlsx'")

