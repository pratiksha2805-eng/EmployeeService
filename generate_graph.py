import json
import matplotlib.pyplot as plt
from collections import Counter

# Load JSON data

with open(file_path, "r") as file:
    raw_data = file.read()
    print(f"Raw JSON content: {raw_data}")

def load_json(file_path):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            if isinstance(data, dict) and "alerts" in data:  # Adjust for nested structure
                return data["alerts"]
            elif isinstance(data, list):
                return data
            else:
                raise ValueError("Expected a list of alerts or a dictionary with an 'alerts' key.")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return []
    except Exception as e:
        print(f"Error loading JSON: {e}")
        return []

# Process data to count alerts by severity
def process_data(data):
    # Safeguard against invalid data
    valid_alerts = [alert for alert in data if isinstance(alert, dict) and "rule" in alert]
    severity_counts = Counter(alert.get("rule", {}).get("severity", "unknown") for alert in valid_alerts)
    return severity_counts

# Generate a bar chart
def create_graph(severity_counts):
    if not severity_counts:
        print("No valid data to plot.")
        return

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

    # Debug: Print loaded data structure
    print(f"Loaded data: {data[:2]}")  # Print first two entries for debugging

    # Process data
    severity_counts = process_data(data)

    # Debug: Print severity counts
    print(f"Severity counts: {severity_counts}")

    # Generate graph
    create_graph(severity_counts)

# Run the script
if __name__ == "__main__":
    main()
