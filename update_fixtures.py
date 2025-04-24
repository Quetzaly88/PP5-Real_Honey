import json

# Define the path to the original fixture file
fixture_path = "products/fixtures/all_products_backup.json"

# Load the fixture data
with open(fixture_path, "r", encoding="utf-8") as file:
    products = json.load(file)

# Function to generate a short description


def generate_short_description(product_name):
    return f"{product_name} is a premium honey product, offering rich flavor and natural sweetness. Perfect for your daily needs."[:150]


# Update missing descriptions
for product in products:
    if not product["fields"].get("description") or len(product["fields"].get("description", "")) < 10:
        product["fields"]["description"] = generate_short_description(product["fields"]["name"])

# Save the updated fixture
updated_fixture_path = "products/fixtures/all_products_backup_updated.json"
with open(updated_fixture_path, "w", encoding="utf-8") as file:
    json.dump(products, file, indent=2, ensure_ascii=False)

print(f"✅ Updated fixture saved to {updated_fixture_path}.")
print("🔄 Next step: Load the updated fixture into the database.")
