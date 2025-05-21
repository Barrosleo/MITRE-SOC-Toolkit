# MITRE-SOC-Toolkit Project Documentation

## Overview
MITRE-SOC-Toolkit encompasses tools to integrate threat intelligence data, classify indicators according to MITRE ATT&CK, visualize incident relationships, and document incident analysis procedures.

## Components
1. **Threat Intelligence Integration:**  
   - **fetch_threat_data.py:** Retrieves public threat data.
   - **mapping_to_attack.ipynb:** Demonstrates mapping indicators to ATT&CK techniques.

2. **Interactive Dashboard:**  
   - A Flask app (`dashboard/app.py`) serves a dynamic interface showing charts and network diagrams based on incident data.

3. **Incident Analysis Playbook:**  
   - Detailed playbooks in `playbooks/incident_analysis_playbook.md` guide SOC analysts through incident response steps.

4. **Automation & Reporting:**  
   - Scripts in the `automation/` folder automatically generate incident reports.

## Setup Instructions
Refer to the README.md for full setup and configuration details.

## Contribution Guidelines
- Fork the repository.
- Follow PEP8 for Python code.
- Update documentation when adding new features.
- Submit pull requests for review.

This project aims to be a living resource. Contributions from the community are welcome!
