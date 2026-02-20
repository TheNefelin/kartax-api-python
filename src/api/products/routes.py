from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.api.products import repository
from src.api.products.dto import ProductDTO
from src.core.database import get_db
from src.shared.dtos import ApiResponse

router = APIRouter(prefix="/products", tags=["products"])

# GetAll
@router.get("/", response_model=ApiResponse[List[ProductDTO]])
def get_all(db: Session = Depends(get_db)):
  try:
    items = repository.get_all(db)
    return ApiResponse.success(data=items)
  except ValueError as e:
    return ApiResponse.bad_request(message=str(e))
  except Exception as e:
    return ApiResponse.server_error(message=str(e))

# GET BY ID
@router.get("/{id}", response_model=ApiResponse[ProductDTO])
def get_by_id(id: int, db: Session = Depends(get_db)):
  try:
    item = repository.get_by_id(id, db)

    if not item:
      return ApiResponse.not_found(message="Product not found")
    
    return ApiResponse.success(data=item)
  except ValueError as e:
    return ApiResponse.bad_request(message=str(e))
  except Exception as e:
    return ApiResponse.server_error(message=str(e))

# GET BY ID GROUP
@router.get("/group/{id}", response_model=ApiResponse[List[ProductDTO]])
def get_by_id_group(id: int, db: Session = Depends(get_db)):
  try:
    items = repository.get_by_id_group(id, db)

    if not items:
      return ApiResponse.not_found(message="Products not found for the given group")
    
    return ApiResponse.success(data=items)
  except ValueError as e:
    return ApiResponse.bad_request(message=str(e))
  except Exception as e:
    return ApiResponse.server_error(message=str(e))
