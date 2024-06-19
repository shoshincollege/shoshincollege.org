# shoshincollege.org

an experimental learning co-operative

## Development

This is a standard Django application.

Setup and run:

```sh
# setup venv
python3 -m venv .venv
source .venv/bin/activate

# setup env variables
cp .envrc.example .envrc
source .envrc

# install dependencies
pip install -r requirements.txt
```

Run development server:

```sh
python manage.py runserver
```

Format:

```sh
ruff format .
```

Lint:

```sh
ruff check --fix .
```

## Deploy

Every commit on branch `main` auto-deploys. To deploy manually:

```sh
cd ansible/
ansible-playbook playbook.yaml -v
```

## License

Copyright Shoshin College CIC

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU Affero General Public License as published by the Free
Software Foundation, version 3.
