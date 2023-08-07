from sqlmodel import create_engine, select, Session

from .models import Department, Application, JobSeeker, Position

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)

# # === Seeder ===

# department_1 = Department(name="Technology", description="Technology department")
# department_2 = Department(name="Operation", description="Operation department")
# department_3 = Department(name="Marketing", description="Marketing department")
# department_count = 0

# with Session(engine) as session:
#     statement = select(Department)
#     results = session.exec(statement)
#     for department in results:
#         # print(department)
#         department_count += 1
#         break

# if department_count == 0:
#     with Session(engine) as session:
#         session.add(department_1)
#         session.add(department_2)
#         session.add(department_3)
#         session.commit()
