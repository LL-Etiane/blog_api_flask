# Api for demo demo block for the gdsc teachings on react
## To run;
- `pip install -r requirements.txt` to install requirements
- create the tables
    - Open flask shell `flask --app api shell`
    - Import the db and the models 
        - `from api import db`
        - `from api.models import Posts`
        - `db.create_all()`
- Run the sever,    `flask --app api --debug run`