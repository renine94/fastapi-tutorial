from fastapi import APIRouter, Depends, HTTPException, status

from db.models.jobs import Job
from db.repository.jobs import create_new_job, retreive_job
from db.session import get_db
from schemas.jobs import JobCreate, ShowJob
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/create-job", response_model=ShowJob)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    owner_id = 1
    job = create_new_job(job=job, db=db, owner_id=owner_id)
    return job


@router.get(
    "/get/{id}",
    response_model=ShowJob,
    name="Job 조회",
    description="job_id 로 특정job을 조회한다.",
)
def retreive_job_by_id(id: int, db: Session = Depends(get_db)):
    job = retreive_job(id=id, db=db)
    if not job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Job with id {id} does not exist",
        )
    return job
