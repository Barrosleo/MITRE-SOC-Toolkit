# MITRE-SOC-Toolkit

## Purpose
The MITRE-SOC-Toolkit is an educational and practical tool designed for SOC Level 1 analysts. It integrates threat intelligence, maps observed indicators to MITRE ATT&CK techniques, visualizes incident data via an interactive dashboard, and provides incident analysis playbooks and automation tools to streamline response and reporting.

## Key Features
- **Threat Intelligence Integration:**  
  Python scripts and Jupyter Notebooks ingest threat data from public feeds and correlate indicators with MITRE ATT&CK techniques.
- **Interactive Dashboard:**  
  A Flask-based web dashboard visualizes incident data against the MITRE ATT&CK matrix.
- **Incident Analysis Playbook:**  
  Documented playbooks guide analysts through alert prioritization, root-cause analysis, and remediation strategies based on MITRE frameworks.
- **Automation & Reporting:**  
  Tools to automatically generate technical documentation and incident reports using defined MITRE tactics.
- **Educational Resources:**  
  Cheat sheets and markdown documents explain MITRE terminology (ATT&CK, D3FEND, MITRE Engage) with practical SOC exercise examples.

## Repository Structure
```
MITRE-SOC-Toolkit/
├── threat_intelligence/
│   ├── fetch_threat_data.py        # Python script to fetch/enrich threat data from public feeds
│   └── mapping_to_attack.ipynb     # Jupyter Notebook mapping indicators to MITRE ATT&CK techniques
├── dashboard/
│   ├── app.py                      # Flask app to serve the interactive dashboard
│   ├── templates/
│   │   └── index.html              # HTML template for the dashboard
│   └── static/
│       ├── css/
│       │   └── style.css           # Dashboard styling
│       └── js/
│           └── dashboard.js        # JavaScript (Chart.js) for visualizing incident data
├── playbooks/
│   └── incident_analysis_playbook.md  # Documented SOC incident analysis playbook anchored in MITRE frameworks
├── automation/
│   └── generate_report.py          # Script to generate automated incident reports based on MITRE tactics
├── docs/
│   ├── MITRE_Concepts_CheatSheet.md    # Cheat sheet explaining MITRE ATT&CK, D3FEND, and MITRE Engage
│   └── Project_Documentation.md    # Detailed project overview, setup, and usage guidelines
├── .gitignore                      # Ignore unnecessary files (e.g., virtual environments, caches)
└── README.md                       # Project overview, features, setup instructions, and usage
```

## Setup & Usage

### Prerequisites
- Python 3.7+
- pip
- (Optional) Jupyter Notebook for exploring the notebooks

### Quick Start

1. **Clone the repository:**

   ```
   git clone https://github.com/Barrosleo/MITRE-SOC-Toolkit.git
   cd MITRE-SOC-Toolkit
   ```
   
3.  **Setup the Backend:**
  
  ```
  cd dashboard
  python -m venv venv
  source venv/bin/activate    # On Windows: venv\Scripts\activate
  pip install -r ../threat_intelligence/requirements.txt  # Or install all dependencies manually as listed in docs/Project_Documentation.md
  pip install -r ../dashboard/requirements.txt
  python app.py
  ```

3.  **Explore the Notebooks & Documentation:**
- Open threat_intelligence/mapping_to_attack.ipynb in Jupyter Notebook.
- Review docs/MITRE_Concepts_CheatSheet.md and docs/Project_Documentation.md for detailed information.

## Future Enhancements
- Integrate real-time threat feeds (e.g., VirusTotal, MISP)

- Enhance the dashboard with additional interactive visualizations (using D3.js)

- Implement role-based access control for team environments

- Expand playbooks with more operational scenarios

## License

This project is licensed under the MIT License.
