## Python

### How to run:
Create .env file with the following variables as shown in .env.example
```
HOST=0.0.0.0
PORT=8000
SECRET_KEY=09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=600 // in seconds
```

```
pip install -r requirements.txt
uvicorn app.main:app --reload
```
### Scenarios covered:
- CRUD operations for a user model
- Protected endpoints with JWT authentication

>> After starting the server, you can see 10 generated users at console. 
    You can use any of them to login and test the protected endpoints.