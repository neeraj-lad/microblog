#!/home/student/virtualenvs/microblog/bin/python
from migrate.versioning import api
from cfg import SQLALCHEMY_DATABASE_URI
from cfg import SQLALCHEMY_MIGRATE_REPO
api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
print('Current database version: ' + str(v))
