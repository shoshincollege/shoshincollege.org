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

```sh
cd ansible/
ansible-playbook playbook.yaml -v
```
