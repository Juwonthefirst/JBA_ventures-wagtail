import subprocess, sys


def run_development_server():
    subprocess.run(["uv", "run", "manage.py", "runserver", "0.0.0.0:8000"])


def run_production_server():
    subprocess.run(["python", "manage.py", "makemigrations"])
    subprocess.run(["python", "manage.py", "migrate"])
    subprocess.run(["python", "createsuperuser.py"])
    subprocess.run(["python", "manage.py", "collectstatic"])
    subprocess.run(["gunicorn", "JBA_ventures.wsgi:application"])


def make_migrations_and_migrate():
    subprocess.run(["uv", "run", "manage.py", "makemigrations"])
    subprocess.run(["uv", "run", "manage.py", "migrate"])


def run_tests():
    subprocess.run(["uv", "run", "manage.py", "test", "v1"])


def load_initial_data():
    subprocess.run(["uv", "run", "load_properties.py"])


if __name__ == "__main__":
    if len(sys.argv) > 1:
        match (sys.argv[1]):
            case "dev":
                run_development_server()
            case "prod":
                run_production_server()
            case "migrate":
                make_migrations_and_migrate()
            case "test":
                run_tests()
            case "load_initial_data":
                load_initial_data()
