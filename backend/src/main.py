import uvicorn
from fastapi import Query, Depends, FastAPI, HTTPException
from fastapi.responses import ORJSONResponse
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from db import get_session
from models import Student, StudentCreate, StudentRead


app = FastAPI(
    title='Boilerplate',
    description='Fastapi React boilerplate',
    version='0.1',
    openapi_url='/docs/openapi.json',
    default_response_class=ORJSONResponse,
    docs_url='/docs',
    redoc_url=None,
)


@app.get('/api/v1/modeus', response_model=dict[str, str])
async def example() -> dict[str, str]:
    return {'sas': 'sus'}


@app.patch('/api/v1/student/{student_id}', response_model=StudentRead)
async def year_student(student_id: int, year: int, session: AsyncSession = Depends(get_session)) -> StudentRead:
    student = await session.get(Student, student_id)
    if not student:
        raise HTTPException(status_code=404, detail='Student not found')
    student.year = year
    await session.commit()
    print(student)
    return student


@app.get('/api/v1/student/{student_id}', response_model=StudentRead)
async def get_student(student_id: int, session: AsyncSession = Depends(get_session)) -> StudentRead:
    student = await session.get(Student, student_id)
    if not student:
        raise HTTPException(status_code=404, detail='Student not found')
    return student


@app.get('/api/v1/students', response_model=list[StudentRead])
async def get_students(
        offset: int = 0, limit: int = Query(default=100, lte=100),
        session: AsyncSession = Depends(get_session)) -> list[StudentRead]:
    result = await session.exec(select(Student).offset(offset).limit(limit))
    return result.all()


@app.post('/api/v1/student', response_model=StudentRead)
async def add_student(student: StudentCreate, session: AsyncSession = Depends(get_session)) -> StudentRead:
    student = Student(**student.dict())
    session.add(student)
    await session.commit()
    # Seems, that refreshing is not necessary
    # await session.refresh(student)
    return student


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', reload=True)  # , log_level='critical')
