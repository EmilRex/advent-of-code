import shutil
import subprocess
from datetime import datetime
from pathlib import Path

import typer


def bootstrap(name: str, year: int = datetime.now().year):
    """
    Bootstrap a new solution directory with template files.
    """
    path = Path("solutions") / str(year) / name

    typer.echo(f"Bootstrapping '{path}'...")

    # Create directory and files
    path.mkdir(parents=True, exist_ok=True)

    # Copy template.py to code.py
    shutil.copy("template.py", path / "code.py")

    # Create empty files
    (path / "example.txt").touch()
    (path / "input.txt").touch()

    subprocess.run(["cursor", str(path / "code.py")])

    typer.echo("Done\n")


if __name__ == "__main__":
    typer.run(bootstrap)
