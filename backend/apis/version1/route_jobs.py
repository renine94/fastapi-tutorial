from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from db.models.jobs import Job
from db.repository.jobs import create_new_job, retreive_job, list_jobs, update_job_by_id, delete_job_by_id
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
    description="job_id 로 특정 job을 조회한다.",
)
def retreive_job_by_id(id: int, db: Session = Depends(get_db)):
    job = retreive_job(id=id, db=db)
    if not job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Job with id {id} does not exist",
        )
    return job


@router.get(
    "/all",
    response_model=List[ShowJob],
    name="All Jobs 조회",
)
def retreive_all_jobs(db: Session = Depends(get_db)):
    jobs = list_jobs(db)
    return jobs


@router.put("/update/{id}")
def update_job(id: int, job: JobCreate, db: Session = Depends(get_db)):
    owner_id = 1  # TODO 추후 인증기능 구현후에 동적으로 넣어줘야 한다.
    is_success = update_job_by_id(id=id, job=job, db=db, owner_id=owner_id)
    if not is_success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Job with id {id} does not exist")
    return {"detail": "Successfully updated data."}


@router.delete("/delete/{id}")
def delete_job(id: int, db: Session = Depends(get_db)):
    owner_id = 1
    is_success = delete_job_by_id(id=id, db=db, owner_id=owner_id)
    if not is_success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Job with id {id} does not exist")
    return {"detail": "Successfully deleted the job"}
