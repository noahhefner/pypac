# pypac

Arch Package Manager written in Python

## Repo Add

high level flow

- check repository exists
- verify repo extension, check for supported tar format
- get repo lock file
- check repo file
    - if empty repo, error

- for each package in arguments
    - add package to db

- re-zip the database

modules needed:

- tarfile (for decompressing repos, does not support .Z, but that seems to be a legacy format)
- pythopn-gnupg (for creating database signature)

Example usage:

```sh
repo-add path/to/database.db.tar.gz package1.pkg.tar.zst
```

Ideas:

ditch delta file support

maybe make repo a context?
```python
with Database("path/to/db") as db:
    db.add(packagename)
```