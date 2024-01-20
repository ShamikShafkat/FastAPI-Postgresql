from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE = "postgresql://<username_for_postgresql>:<password_for_postgresql>@<address_of_server_running_on_with_port>/<name_of_the_database>"

"""Creates a engine for database"""
engine = create_engine()

"""creates a local session with binding above created engine"""
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

"""creates a base for db"""
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        print(e)
    finally:
        db.close()