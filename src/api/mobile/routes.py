from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import null

from src.api.mobile.repository import get_all_hierarchy
from src.api.mobile.dto import CategoryHierarchyDTO
from src.core.database import get_db
from src.shared.dtos import ApiResponse

router = APIRouter(prefix="/mobile", tags=["mobile"])

# GetAll
@router.get("/products-hierarchy", response_model=ApiResponse[List[CategoryHierarchyDTO]])
def get_all(db: Session = Depends(get_db)):
  try:
    res = get_all_hierarchy(db) 
    
    return ApiResponse.success(data=res)
  except ValueError as e:
    return ApiResponse.bad_request(message=str(e))
  except Exception as e:
    return ApiResponse.server_error(message=str(e))