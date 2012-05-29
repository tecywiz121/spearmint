spearmint
=========

An entry for the MintChip competition.

Installation
------------

Clone the repository locally, set the permissions on the media folder so that
the server can write to it.  Optionally you may create a virtual environment
using the python virtualenv package.  Creating a virtual environment is
recommended.  Next, install the following packages and versions.

> Django==1.4
>
> South==0.7.5
>
> django-registration==0.8

For production or testing environments, install:

> psycopg2==2.4.5

For development, sqlite3 should be sufficient.

Any settings specific to development machines should be kept in
local_settings.py.
