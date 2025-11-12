# U.S. Fintech Company Classification: IPO Analysis & Manual Verification
Python automation for fintech IPO classification - Suffolk University Research and Conference Assistant 

## Project Overview

This repository contains Python scripts and methodologies developed during my research assistantship at Suffolk University (May–July 2025) to systematically identify and classify fintech companies from a comprehensive dataset of U.S. Initial Public Offerings (IPOs). The project combines automated data extraction, text analysis, and manual verification to create a robust classification system for financial technology companies.

## Research Context

### Background
Financial technology (fintech) has transformed the financial services industry, yet accurately identifying which companies qualify as "fintech" remains challenging. This project addresses that challenge by developing a reproducible methodology to classify companies based on their business models, SEC filings, and operational characteristics.

### Objectives
- Systematically identify fintech companies from a master dataset of 1,900+ U.S. IPO companies (1994-2023)
- Develop automated classification tools using Python to scale the analysis
- Manually verify classifications through rigorous research methodology
- Create a three-tiered classification system: **Core Fintech**, **Supporting Fintech**, and **Non-Fintech**

### Research Questions
1. Which companies from the U.S. IPO dataset between 1994-2023 can be classified as fintech?
2. What distinguishes core fintech providers from supporting fintech enablers?
3. How can SEC Form S-1 filings be leveraged to identify fintech characteristics?

## Methodology

### Data Sources
- **Primary Dataset**: `usipo_to_check_fintech_1994-2023.xlsx` - Comprehensive list of U.S. IPO companies with CIK (Central Index Key) numbers
- **SEC EDGAR Database**: Form S-1 IPO prospectuses for detailed company descriptions
- **Statista Fintech Report**: External validation source for known fintech companies
- **Company Tickers Exchange**: `company_tickers_exchange.json` from SEC for CIK mapping

### Three-Tier Classification System

#### 1. Core Fintech
Companies whose **primary** products or services center on financial technology innovation:
- Digital/mobile banking platforms
- Payment processing systems
- Peer-to-peer lending platforms
- Cryptocurrency and blockchain services
- Robo-advisory and automated investment platforms
- InsurTech (digital insurance solutions)
- RegTech (regulatory compliance technology)

#### 2. Supporting Fintech
Companies that **enable or enhance** fintech ecosystems but don't provide fintech as their core service:
- Cybersecurity providers serving financial institutions
- Cloud infrastructure platforms for fintech clients
- Data analytics and business intelligence tools for financial services
- Identity verification and KYC (Know Your Customer) services

#### 3. Non-Fintech
Companies with no direct or peripheral involvement in financial technology operations.

## Project Workflow

### Phase 1: Data Collection & Preparation
1. **CIK Database Setup**: Downloaded and processed SEC's company tickers exchange database
2. **Missing CIK Resolution**: Manually searched for missing Central Index Keys using Perplexity AI and SEC EDGAR
3. **Form S-1 Acquisition**: Bulk downloaded IPO prospectuses using Python scripts

### Phase 2: Automated Classification
1. **Keyword Extraction**: Analyzed academic literature (Buchak et al., 2018; Steenbergen, 2017) to establish fintech classification criteria
2. **Python-Based Filtering**: Developed scripts to scan Form S-1 documents for fintech keywords and indicators
3. **Statista Cross-Reference**: Matched companies against known fintech firms from industry reports

### Phase 3: Manual Verification
1. **Random Sampling**: Generated 10 batches of 100 randomly-selected companies (1,000 total reviews)
2. **Multi-Source Research**: Used Microsoft Copilot, Google Gemini, and Perplexity AI to gather company information from:
   - SEC filings (site:sec.gov constraint)
   - Official company websites
   - Press releases and news articles
3. **Evidence-Based Classification**: Recorded verdicts with brief justifications for each company
4. **Quality Review**: Conducted consistency checks across all classifications

### Phase 4: Consolidation & Validation
1. **Batch Compilation**: Merged all 10 manually-reviewed batches into a master file
2. **Standardization**: Ensured consistent use of "Yes", "Supporting Fintech", and "No" classifications
3. **Documentation**: Preserved detailed justifications for audit trail and research reproducibility

## Repository Structure

### Python Scripts

**Random Sampling & Batch Management:**
- `Batch 1 - Sample Selection Python Script.py` - Initial random sampling of 100 companies
- `Batch 2 - Sample Selection Python Script.py` - Second batch random sampling
- `Batch 5 - Sample Selection Python Script.py` - Updated sampling script with duplicate prevention

**Classification & Matching:**
- `IS Fintech Company Matching.py` - Original automated fintech classification based on reference datasets
- `Modified IS Fintech Company Matching.py` - Updated version with improved output formatting

**IPO Analysis:**
- `IPO Prospectus Pattern.py` - Keyword detection and pattern analysis across S-1 filings
- `Tone Analysis (S-1 Forms).py` - Sentiment analysis using Loughran-McDonald dictionaries

### Jupyter Notebooks

**Data Processing:**
- `SEC CIK JSON to CSV format.ipynb` - Converts SEC company tickers JSON to CSV format
- `Bulk Download Form S-1 Filings from SEC EDGAR.ipynb` - Automated S-1 prospectus downloader
- `Fintech Prospectus (pt1) IPO PDF to CSV.ipynb` - Extracts text from PDF prospectuses
- `Fintech Classification (pt 2) (CSV -> Analysis).ipynb` - Classification analysis pipeline

### Documentation
- `README.md` - This file


## Key Python Scripts

### 1. Batch Sample Selection Scripts
**Purpose**: Generate random samples of 100 companies for manual classification while preventing duplicates across batches

**Key Features**:
- Random sampling without replacement
- Tracks previously sampled companies across batches
- Exports manageable Excel files for classification teams

**Files**: `Batch 1 - Sample Selection Python Script.py`, `Batch 2 - Sample Selection Python Script.py`, `Batch 5 - Sample Selection Python Script.py`

### 2. IS Fintech Company Matching
**Purpose**: Automatically flag companies as fintech based on reference datasets (e.g., Statista Report)

**Methodology**:
- Cross-references company CIK numbers with known fintech databases
- Outputs binary classification (1 for fintech, 0 for non-fintech)
- Modified version uses blank cells instead of "0" for more flexible analysis

**Files**: `IS Fintech Company Matching.py`, `Modified IS Fintech Company Matching.py`

**Limitations**: Only identifies companies present in reference datasets; may miss emerging fintech firms

### 3. IPO Prospectus Pattern Analysis
**Purpose**: Detect keyword usage and categorize companies based on S-1 form content

**Output**: `fintech_ipo_Pattern_analysis.xlsx`

**Analysis Includes**:
- Keyword frequency detection
- Company categorization based on financial services
- Pattern trend identification across IPO cohorts

### 4. Tone Analysis (S-1 Forms)
**Purpose**: Apply Loughran & McDonald financial tone dictionaries to IPO prospectuses

**Metrics Generated**:
- Uncertainty score (hedge words, ambiguous language)
- Negativity score (risk factors, challenges)
- Speculative language indicators

**Output**: `fintech_ipo_tone_analysis_simple.xlsx`

**Research Application**: Helps identify companies with technology-forward or innovation-focused business descriptions

### 5. SEC Data Processing
**Purpose**: Convert SEC's JSON format company tickers into analyzable CSV format

**File**: `SEC CIK JSON to CSV format.ipynb`

**Use Case**: Enables mapping between company names, ticker symbols, and CIK numbers for bulk downloads

### 6. Bulk S-1 Download Script
**Purpose**: Automatically download Form S-1 filings from SEC EDGAR based on CIK list

**File**: `Bulk Download Form S-1 Filings from SEC EDGAR.ipynb`

**Technical Notes**:
- Handles multiple S-1 versions (original, amendments, updates)
- Error handling for companies with Form S-4 (merger-related) instead of S-1
- Respects SEC rate limits

## Manual Classification Process

### Step-by-Step Workflow

1. **Batch Preparation**: Python script randomly selects 100 companies from master list
2. **Research Phase**: For each company, research using the following prompt template:

Using information from SEC filings (site:sec.gov) or the company's website,
summarize whether [Company Name] (CIK: XXXX) offers any services related to
financial technology. If possible, identify if they are involved in: digital
payments, mobile banking, online lending, cryptocurrency, blockchain,
robo-advisors, or any digital financial platforms. Please list key financial
or tech features mentioned in filings or descriptions.


3. **Information Gathering**:
   - Search SEC filings via `site:sec.gov` constraint
   - Review company's official website
   - Consult press releases and credible news sources
   - Document all findings in Word document for evidence trail

4. **Classification Decision**:
   - Compare findings against fintech classification criteria
   - Assign verdict: "Yes" (Core Fintech), "Supporting Fintech", or "No"
   - Write brief justification explaining the decision

5. **Quality Assurance**:
   - Review batch for internal consistency
   - Check for ambiguous cases requiring additional research
   - Validate against external fintech databases when available

6. **Documentation**: Record classification and justification in Excel spreadsheet

### Recommended AI Tools for Manual Research

- **Microsoft Copilot**: Real-time internet integration, free tier sufficient
- **Google Gemini**: Strong web search capabilities, reliable for quick company lookups
- **ChatGPT**: Best for detailed analysis and clarification after initial research
- **Perplexity AI**: Excellent for academic and SEC filing searches

**Average Processing Time**: ~6 hours 50 minutes per 100-company batch (1 researcher)

## Results & Outputs

### Consolidated Dataset
`USIPO_Fintech_Batch1-10_Compiled.xlsx`
- 1,000 manually classified companies
- Standardized "Verdict" column (Yes / Supporting Fintech / No)
- "Brief Justification" column with research evidence
- "Batch Origin" column tracking classification batch (1-10)
- Excel filter functionality for easy analysis

### Analysis Reports
- **Pattern Analysis**: Trends in fintech IPO characteristics over time
- **Tone Analysis**: Sentiment and speculative language in fintech vs. non-fintech prospectuses
- **Classification Metrics**: Distribution of Core Fintech vs. Supporting Fintech companies

## Technologies Used

- **Python 3.x**: Core scripting language
- **pandas**: Data manipulation and analysis
- **requests / urllib**: SEC EDGAR API interactions
- **openpyxl / xlsxwriter**: Excel file generation
- **PyPDF2 / pdfplumber**: PDF text extraction from S-1 forms
- **NLTK / spaCy**: Natural language processing for keyword detection
- **Loughran-McDonald Dictionary**: Financial sentiment analysis

## Key Challenges & Solutions

### Challenge 1: Missing CIK Numbers
**Problem**: Many companies lacked Central Index Keys required for SEC API access  
**Solution**: Manual search using Perplexity AI + validation through official SEC filings

### Challenge 2: Classification Ambiguity
**Problem**: Some companies use fintech as supporting technology, not core business  
**Solution**: Created three-tier system distinguishing Core vs. Supporting Fintech

### Challenge 3: Batch Overlap Errors
**Problem**: Early Python code allowed duplicate sampling across batches  
**Solution**: Implemented exclusion tracking in `Batch 5 - Sample Selection Python Script.py` to prevent re-sampling

### Challenge 4: Form S-1 Variations
**Problem**: SEC filings contain multiple S-1 versions (original, amendments, updates)  
**Solution**: Bulk download script filters for "final" or most comprehensive versions

## Academic References

This classification methodology draws on:

1. **Buchak, G., Matvos, G., Piskorski, T., & Seru, A. (2018)**  
   "Fintech, regulatory arbitrage, and the rise of shadow banks"  
   *Journal of Financial Economics*, 453-483

2. **Steenbergen, T.M. (2017)**  
   "The IPO Performance of FinTech Companies"  
   Master's Thesis

3. **Loughran, T., & McDonald, B. (2011)**  
   "When Is a Liability Not a Liability? Textual Analysis, Dictionaries, and 10-Ks"  
   *Journal of Finance*, 66(1), 35-65

## Future Improvements

- [ ] Integrate machine learning classification models (Random Forest, XGBoost)
- [ ] Expand training dataset beyond Statista reference list
- [ ] Automate text extraction from Form S-1 with better OCR
- [ ] Develop NLP pipeline for semantic understanding of business descriptions
- [ ] Create real-time classification tool for new IPO filings
- [ ] Validate classifications against post-IPO company performance data

## Author & Acknowledgments

**Research Assistant**: Benedict Daxell Santoso  
**Institution**: Suffolk University, Sawyer Business School  
**Supervising Professor**: Prof. Lin Guo  
**Research Period**: May 2025 - July 2025  
**Additional Contributors**: Ella (Manual Classification), Ruben (Batch Review)

**Special Thanks**:
- Suffolk University MRS International Risk Conference team
- MIT AI and Climate Forum organizers
- Kimberly (Conference logistics support)

## License

This project was developed as part of academic research at Suffolk University. The methodology and code are shared for educational and research purposes. Please cite appropriately if using this work in your research.

## Contact

For questions about this methodology or collaboration opportunities:
- **LinkedIn**: https://www.linkedin.com/in/benedictdaxellsantoso/ 
- **GitHub**: https://github.com/bdsantoso168 

---

**Note**: This research was conducted as part of broader studies on fintech IPO performance, financial innovation patterns, and regulatory implications of technology-driven financial services.
