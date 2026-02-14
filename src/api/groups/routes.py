from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.api.groups import repository
from src.api.groups.dto import GroupDTO
from src.core.database import get_db
from src.shared.dtos import ApiResponse

router = APIRouter(prefix="/groups", tags=["groups"])

# GetAll
@router.get("/", response_model=ApiResponse[List[GroupDTO]])
def get_all(db: Session = Depends(get_db)):
  try:
    res = repository.get_all(db)
    
    return ApiResponse.success(data=res)
  except ValueError as e:
    return ApiResponse.bad_request(message=str(e))
  except Exception as e:
    return ApiResponse.server_error(message=str(e))