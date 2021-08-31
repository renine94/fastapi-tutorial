from typing import Optional
from pydantic import BaseModel, Field
from datetime import date, datetime


class JobBase(BaseModel):
    title: Optional[str] = Field(None, title="공고명")
    company: Optional[str] = Field(None, title="회사이름")
    company_url: Optional[str] = Field(None, title="회사 홈페이지")
    location: Optional[str] = Field("Remote", title="위치")
    description: Optional[str] = Field(None, title="설명")
    date_posted: Optional[date] = Field(datetime.now().date(), title="생성일")


class JobCreate(JobBase):
    title: str = Field(title="공고명")
    company: str = Field(title="회사이름")
    location: str = Field(title="위치")
    description: str = Field(title="설명")


class ShowJob(JobBase):
    title: str
    company: str
    company_url: Optional[str]
    location: str
    date_posted: date
    description: Optional[str]

    class Config:
        orm_mode = True
