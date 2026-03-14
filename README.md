# JBA Ventures

A property management and listing platform built with Wagtail CMS. The application allows users to browse, search, and manage residential properties with detailed information, images, and tagging capabilities.

## Technologies Used

- **Wagtail 7.3.1** - CMS framework built on Django
- **Django 6.0** - Web framework
- **Python 3.13** - Programming language
- **UV** - Fast Python package manager
- **AWS S3 / boto3** - Cloud storage for media files
- **Gunicorn** - Production application server
- **Docker** - Containerization

**Key Dependencies:**

- `django-storages` - Cloud storage integration
- `dj-database-url` - Database configuration
- `psycopg2` - PostgreSQL adapter
- `whitenoise` - Static file serving
- `django-filter` - Search and filtering
- `taggit` - Tagging system

## Setup Instructions

### Prerequisites

- Python 3.13+
- UV (fast Python package manager)
- PostgreSQL (for production)
- SQLite (development)
- Virtual environment manager (venv)

### Local Development Setup

1. **Clone the repository:**

   ```bash

   git clone https://github.com/Juwonthefirst/JBA_ventures-wagtail
   cd JBA_ventures-wagtail
   ```

2. **Create and activate virtual environment:**

   ```bash

   python -m venv .venv
   source .venv/Scripts/activate  # On Windows
   # or
   source .venv/bin/activate      # On macOS/Linux
   ```

3. **Install dependencies:**

   ```bash

   uv sync
   ```

4. **Set up the database:**

   ```bash

    uv run scripts.py migrate
   ```

5. **Create a superuser:**

   ```bash

   uv run createsuperuser.py
   ```

6. **Collect static files:**

   ```bash

   uv run manage.py collectstatic

   ```

7. **Run development server:**

   ```bash

   uv run scripts.py dev
   ```

   Access the application at `http://localhost:8000` and admin panel at `http://localhost:8000/admin`

### Docker Setup

```bash
docker build -t jba-ventures .
docker run -p 8000:8000 jba-ventures
```

## Models

### HomePage

The main landing page of the website displaying featured properties.

- **Fields:**

  - `hero_image` - Featured image for the homepage
  - `hero_text` - Hero section text (max 120 characters)
- **Features:** Displays live property pages and integrates search functionality

### PropertyPage

Represents individual property listings with comprehensive details.

- **Fields:**
  - `address` - Property address (max 200 chars)
  - `country`, `state`, `district` - Location information
  - `description` - Rich text property description
  - `benefits` - List of property benefits
  - `type` - Property type (max 50 chars)
  - `offer` - Offer type: Rent, Sale, or Lease
  - `price` - Property price (BigInteger)
  - `bedrooms`, `bathrooms` - Room counts
  - `size` - Property size in square units
  - `tags` - Search tags via PropertyPageTag
- **Features:** Full-text search, image gallery, WhatsApp integration link

### PropertyImageGallery

Image gallery for property listings (one-to-many relationship).

- **Fields:**

  - `page` - Foreign key to PropertyPage
  - `image` - Associated image file

### PropertyPageTag

Tagging system for searchable property attributes.

- Enables properties to be discovered via multiple tags

## Project Structure

```
JBA_ventures/
├── home/              # Homepage app
├── property/          # Property listings app
├── search/            # Search functionality
├── JBA_ventures/      # Project settings & configs
├── media/             # User-uploaded files
└── static/            # CSS, JS, images
```
