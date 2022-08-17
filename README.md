# Simple Calculator 
## How to run server
### In dev environment
To run in dev environment You need to use `docker-compose-dev.yml` file.
This command will bring up all services:
```shell
docker-compose -f docker-compose-dev.yml up 
```
If You're runnin UNIX-like system (MacOS or Linux, for example) you may create 
a link to compose file like this:
```shell
ln -s docker-compose-dev.yml docker-compose.yml
```
In this case You will be able to run shorter command:
```shell
docker-compose up
```

### In prod environment
To run in dev environment You need to use `docker-compose-prod.yml` file.
This command will bring up all services:
```shell
docker-compose -f docker-compose-prod.yml
```
## Utils
Consider, that all utils' commands should run inside container environment.
So run shell inside container like this:
```shell
docker-compose -f docker-compose-dev.yml run --rm calc bash
```
Or wrap utils' commands like this
```shell
docker-compose -f docker-compose-dev.yml run --rm calc <your_command_goes_here>
```
## Code Style check
`Flake8` is used to check code style. You can this command to check it:
```shell
flake8
```
If output is empty then code style is OK.
## Test
To run tests You can use this command:
```shell
pytest
```
## Test coverage
To calculate percentage of code covered by test you may run this command:
```shell
bash -c "coverage run -m pytest && coverage report"
```
## Migrations
Alembic is used to manage migrations of the database schema in the project.
To create new revision (migration step) you can run next command:
```shell
alembic revision -m "<your migration message goes here>"
```
Then new file should appear in `migration/versions/` directory.
Edit `upgrade` and `downgrade` functions to create migration.</br>
To apply all migrations use this command:
```shell
alembic upgrade head
```
To apply 1 migration use this command:
```shell
alembic upgrade 1
```
To downgrade 1 migration use this command:
```shell
alembic downgrade -1
```
