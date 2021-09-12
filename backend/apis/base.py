from fastapi import APIRouter

from apis.version1 import route_users, route_jobs, route_login


api_router = APIRouter()

"""
- tags: swagger docs에서 API 나누는 기준이 된다.
- prefix: 도메인뒤에 오는 문자열
"""

# v1
api_router.include_router(route_users.router, prefix="/users", tags=["users"])
api_router.include_router(route_jobs.router, prefix="/jobs", tags=["jobs"])
api_router.include_router(route_login.router, prefix="/login", tags=["Authenticate"])

# v2
