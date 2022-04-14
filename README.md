# fastAPI_using_PostgreSQL

# Step 1: Installation
pip install pipenv
pipenv shell
pipenv install fastapi fastapi-sqlalchemy pydantic alembic psycopg2 uvicorn python-dotenv


# Step 2:
alembic init alembic

# Step 3: 
Always do this when you perform any change in the code to see changes in the database:
alembic upgrade head
alembic revision --autogenerate -m "New Migration"

# Step 4:
uvicorn main:app --reload
