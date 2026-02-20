from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.core.database import get_db
from src.shared.dtos import ApiResponse
from . import repository, dto

router = APIRouter(prefix="/groups", tags=["groups"])

# GET ALL
@router.get("/", response_model=ApiResponse[List[dto.GroupDTO]])
def get_all(db: Session = Depends(get_db)):
  try:
    items = repository.get_all(db)
    return ApiResponse.success(data=items)
  except ValueError as e:
    return ApiResponse.bad_request(message=str(e))
  except Exception as e:
    return ApiResponse.server_error(message=str(e))

# GET BY ID
@router.get("/{id}", response_model=ApiResponse[dto.GroupDTO])
def get_by_id(id: int, db: Session = Depends(get_db)):
  try:
    item = repository.get_by_id(id, db)

    if not item:
      return ApiResponse.not_found(message="Group not found")
    
    return ApiResponse.success(data=item)
  except ValueError as e:
    return ApiResponse.bad_request(message=str(e))
  except Exception as e:
    return ApiResponse.server_error(message=str(e))
  
# GET BY ID CATEGORY
@router.get("/category/{id}", response_model=ApiResponse[List[dto.GroupDTO]])
def get_by_id_category(id: int, db: Session = Depends(get_db)):
  try:
    items = repository.get_by_id_category(id, db)

    if not items:
      return ApiResponse.not_found(message="Groups not found for the given category")
    
    return ApiResponse.success(data=items)
  except ValueError as e:
    return ApiResponse.bad_request(message=str(e))
  except Exception as e:
    return ApiResponse.server_error(message=str(e))