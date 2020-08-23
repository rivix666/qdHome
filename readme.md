===============================================================================
Documentation: https://docs.pylonsproject.org/projects/pyramid/en/latest/
Tutorials:     https://docs.pylonsproject.org/projects/pyramid_tutorials/en/latest/
Twitter:       https://twitter.com/PylonsProject
Mailing List:  https://groups.google.com/forum/#!forum/pylons-discuss
Welcome to Pyramid.  Sorry for the convenience.
===============================================================================

Change directory into your newly created project.
    cd qdhome

Upgrade packaging tools.
    env\Scripts\pip install --upgrade pip setuptools

Install the project in editable mode with its testing requirements.
    env\Scripts\pip install -e ".[testing]"

Initialize and upgrade the database using Alembic.
    # Generate your first revision.
    env\Scripts\alembic -c development.ini revision --autogenerate -m "init"
    # Upgrade to that revision.
    env\Scripts\alembic -c development.ini upgrade head

Load default data into the database using a script.
    env\Scripts\initialize_qdhome_db development.ini

Run your project's tests.
    env\Scripts\pytest

Run your project.
    env\Scripts\pserve development.ini
