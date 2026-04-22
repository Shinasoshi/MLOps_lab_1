import argparse
import os
import yaml
from pathlib import Path
from dotenv import load_dotenv
from settings import Settings


def export_envs(environment: str = "dev") -> None:
    env_path = Path("config") / f".env.{environment}"

    if not env_path.exists():
        raise FileNotFoundError(f"Environment file not found: {env_path}")

    load_dotenv(dotenv_path=env_path, override=True)


def export_secrets(secrets_file: str = "secrets.yaml") -> None:
    secrets_path = Path(secrets_file)

    if not secrets_path.exists():
        raise FileNotFoundError(f"Secrets file not found: {secrets_path}")

    with secrets_path.open("r", encoding="utf-8") as file:
        secrets = yaml.safe_load(file)

    if not isinstance(secrets, dict):
        raise ValueError("Secrets file must contain key-value pairs")

    for key, value in secrets.items():
        os.environ[key] = str(value)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from specified .env file."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="The environment to load (dev, test, prod)",
    )
    args = parser.parse_args()

    export_envs(args.environment)
    export_secrets("secrets.yaml")

    settings = Settings()

    print("APP_NAME:", settings.APP_NAME)
    print("ENVIRONMENT:", settings.ENVIRONMENT)
    print("API_KEY:", settings.API_KEY)
