qdHome
======

Getting Started
---------------

- Change directory into your newly created project.

    cd qdhome

- Create a Python virtual environment.

    python3 -m venv env

- Upgrade packaging tools.

    pip install --upgrade pip setuptools

- Install the project in editable mode with its testing requirements.

    pip install -e ".[testing]"

- Initialize and upgrade the database using Alembic.

    - Generate your first revision.

        alembic -c development.ini revision --autogenerate -m "init"

    - Upgrade to that revision.

        alembic -c development.ini upgrade head

- Load default data into the database using a script.

    initialize_qdhome_db development.ini

- Run your project's tests.

    pytest

- Run your project.

    pserve development.ini


- Celery

    celery -A qdhome.services.s_home worker --loglevel=info
    celery -A qdhome.services.s_home worker --pool=solo --loglevel=info

