import sqlite3
from flask_sqlalchemy import SQLAlchemy

def main():
    # Database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///person_data.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)

    connection = sqlite3.connect("company.db")
    print(connection)
    connection.close()


if __name__ == "__main__":
    main()