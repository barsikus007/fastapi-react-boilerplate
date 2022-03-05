import uvicorn
from fastapi import Depends, FastAPI
from fastapi.responses import ORJSONResponse
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_session
from models import Student, StudentCreate


app = FastAPI(
    title='MODEUS',
    description='Yet Another Modeus Realisation',
    version='2.0',
    openapi_url='/docs/openapi.json',
    default_response_class=ORJSONResponse,
    docs_url='/docs',
    redoc_url=None,
)


@app.get('/api/v1/modeus')
async def example() -> dict:
    return {'sas': 'sus'}


@app.get('/api/v1/student', response_model=list[Student])
async def get_students(session: AsyncSession = Depends(get_session)) -> list[Student]:
    result = await session.execute(select(Student))
    students = result.scalars().all()
    return [Student(name=student.name, major=student.major, year=student.year, id=student.id) for student in students]


@app.post('/api/v1/student')
async def add_students(student: StudentCreate, session: AsyncSession = Depends(get_session)) -> Student:
    student = Student(name=student.name, major=student.major, year=student.year)
    session.add(student)
    await session.commit()
    await session.refresh(student)
    return student


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', reload=True)  # , log_level='critical')
