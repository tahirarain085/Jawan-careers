import sqlalchemy
from sqlalchemy import create_engine,text

db_connection_string ="mysql+pymysql://rh3hme2qj7izbsiiait3:pscale_pw_kkERo8jWfWuv4JCKwZpzeUeWm66UVNWTr2GWzgWmxXg@aws.connect.psdb.cloud:3306/jawancareeres"


engine = create_engine(
    db_connection_string,
    connect_args = {
        'ssl':
        {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    }
    )




def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        jobs = []
        for row in result.all():
            jobs.append(row)
        return jobs
        print(type(jobs))