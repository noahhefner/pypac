#!/usr/bin/env python3

from tarfile import TarFile
import sys
from pathlib import Path
from argparse import Namespace
import argparse
import tempfile
import tarfile

def prepare_repo_db():

    """
    acquire file lock on lock file
      - use retry logic

    if db exists
        if db is empty
            error out
        verify signature
        extract db to temp dir

    """

    pass

def add(db: Path):

    try:
        tar: TarFile = tarfile.open(db)
        tar.extract(".PKGINFO")
    except tarfile.ReadError as e:
        # TODO: Cleanup files?
        print(f"Failed to read database archive: {e}")
        sys.exit(1)
    except Exception as e:
        # TODO: Cleanup files?
        print(f"Unexpected error: {e}")
        sys.exit(1)

def main():

    # parse program arguments
    parser = argparse.ArgumentParser(
        prog='pypac',
        description='Arch package manager, written in Python'
    )
    parser.add_argument("db_path")
    parser.add_argument("package_name")
    args: Namespace = parser.parse_args()

    # create Path object for database archive
    db = Path(args.db_path)

    # check that the database archive exists
    if not db.exists():
        print(f"{str(db)} does not exist.")
        exit(1)

    # create a temp dir for database building
    tmp_dir = Path(tempfile.mkdtemp(prefix="repo-tools."))
    db_dir: Path = tmp_dir / "db"
    files_dir: Path = tmp_dir / "files"
    db_dir.mkdir()
    files_dir.mkdir()

    # TODO: Verify PGP signature

    # TODO: Prep database

    # add()
    
if __name__ == "__main__":
    main()
