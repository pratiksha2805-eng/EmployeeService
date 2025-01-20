import json
import matplotlib.pyplot as plt
from collections import Counter

# Load JSON data
def load_json(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

# Process data to count alerts by severity
def process_data(data):
    severity_counts = Counter(alert.get("rule", {}).get("severity", "unknown") for alert in data)
    return severity_counts

# Generate a bar chart
def create_graph(severity_counts):
    # Extract data for plotting
    severities = list(severity_counts.keys())
    counts = list(severity_counts.values())
    
    # Create the bar chart
    plt.figure(figsize=(8, 5))
    plt.bar(severities, counts, color=["red", "orange", "blue", "gray"])
    plt.xlabel("Severity")
    plt.ylabel("Number of Alerts")
    plt.title("GitHub Code Scanning Alerts by Severity")
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    # Save or display the graph
    plt.savefig("github_alerts_graph.png")
    plt.show()

# Main function
def main():
    # Load the JSON report
    file_path = "security_report.json"  # Replace with the path to your JSON report
    data = load_json(file_path)

    # Process data
    severity_counts = process_data(data)

    # Generate graph
    create_graph(severity_counts)

# Run the script
if __name__ == "__main__":
    main()
