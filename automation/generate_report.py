import json
import datetime

def generate_report(incidents):
    """
    Generate a simple text-based report summarizing the incidents.
    """
    report_lines = []
    report_lines.append("MITRE-SOC-Toolkit Incident Report")
    report_lines.append("Generated on: " + datetime.datetime.utcnow().isoformat() + "Z\n")
    component_summary = {}

    for incident in incidents:
        component = incident.get('component', 'Unknown')
        component_summary[component] = component_summary.get(component, 0) + 1

    report_lines.append("Incident Summary by Diamond Component:")
    for component, count in component_summary.items():
        report_lines.append(f" - {component}: {count} incidents")

    report_lines.append("\nDetailed Incidents:")
    for incident in incidents:
        report_lines.append(f"Timestamp: {incident['timestamp']}")
        report_lines.append(f"Description: {incident['description']}")
        report_lines.append(f"Classified as: {incident.get('component', 'Unknown')}\n")

    report_text = "\n".join(report_lines)
    with open('incident_report.txt', 'w') as f:
        f.write(report_text)
    return report_text

# For testing purposes
if __name__ == '__main__':
    with open('../data/sample_incidents.json', 'r') as f:
        incidents = json.load(f)
    report = generate_report(incidents)
    print(report)
