import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "JBA_ventures.settings.dev")
import django

django.setup()

from property.models import PropertyPage
from home.models import HomePage
import json

# Load the fixture data
with open("property/fixtures/initial_data.json", "r") as f:
    data = json.load(f)

# Get the HomePage as parent
home_page = HomePage.objects.first()
if not home_page:
    print("Error: No HomePage found. Create a HomePage first.")
    exit(1)

# Create PropertyPage objects
for item in data:
    fields = item["fields"]
    home_page.add_child(
        instance=PropertyPage(
            live=True,
            title=fields["title"],
            slug=fields["slug"],
            address=fields["address"],
            country=fields["country"],
            state=fields["state"],
            district=fields["district"],
            description=fields["description"],
            benefits=fields["benefits"],
            type=fields["type"],
            offer=fields["offer"],
            price=fields["price"],
            bedrooms=fields.get("bedrooms"),
            bathrooms=fields.get("bathrooms"),
            size=fields["size"],
        )
    )

print(f"Created {len(data)} properties successfully!")
