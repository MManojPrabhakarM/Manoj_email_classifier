import random
import pandas as pd
from pathlib import Path


def generate_dataset(n_samples=500):
    # Get project root (Manoj_email_classifier)
    BASE_DIR = Path(__file__).resolve().parent.parent
    DATA_DIR = BASE_DIR / "data"
    DATA_DIR.mkdir(exist_ok=True)

    OUTPUT_PATH = DATA_DIR / "email_access_data.csv"

    approved_templates = [
        "Your access request to {portal} has been approved.",
        "Access granted to {portal}.",
        "You can now login to {portal}.",
        "Permission approved for {portal}.",
        "Access successfully enabled for {portal}."
    ]

    rejected_templates = [
        "Your access request to {portal} has been rejected.",
        "Access denied due to missing approval.",
        "Request rejected for {portal}.",
        "Manager approval not received for {portal}.",
        "You are not authorized to access {portal}."
    ]

    manual_templates = [
        "Unable to process your request for {portal}.",
        "Please contact administrator.",
        "Manual review required for {portal}.",
        "Insufficient information provided.",
        "Request could not be understood."
    ]

    portals = ["HR Portal", "Finance Dashboard", "Analytics Server", "VPN", "CRM System"]

    data = []

    for _ in range(n_samples // 3):
        data.append((
            random.choice(approved_templates).format(portal=random.choice(portals)),
            "approved"
        ))

        data.append((
            random.choice(rejected_templates).format(portal=random.choice(portals)),
            "rejected"
        ))

        data.append((
            random.choice(manual_templates).format(portal=random.choice(portals)),
            "manual"
        ))

    random.shuffle(data)

    df = pd.DataFrame(data, columns=["text", "label"])
    df.to_csv(OUTPUT_PATH, index=False)

    print(f"Dataset saved to: {OUTPUT_PATH}")
    print("\nClass Distribution:")
    print(df["label"].value_counts())


if __name__ == "__main__":
    generate_dataset()