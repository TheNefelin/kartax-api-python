from typing import List
from fastapi import APIRouter, Depends, File, Form, UploadFile, status
from sqlalchemy.orm import Session

from src.core.database import get_db
from src.shared.dtos import ApiResponse
from . import repository, dto, service

router = APIRouter(prefix="/categories", tags=["categories"])

# GET ALL
@router.get("/", response_model=ApiResponse[List[dto.CategoryDTO]], status_code=status.HTTP_200_OK)
def get_all(db: Session = Depends(get_db)):
  try:
    items = repository.get_all(db)
    return ApiResponse.success(data=items)
  except Exception as e:
    return ApiResponse.server_error(str(e))

# GET BY ID
@router.get("/{id}", response_model=ApiResponse[dto.CategoryDTO], status_code=status.HTTP_200_OK)
def get_by_id(id: int, db: Session = Depends(get_db)):
  try:
    item = repository.get_by_id(id, db)

    if not item:
      return ApiResponse.not_found()

    return ApiResponse.success(data=item)
  except Exception as e:
    return ApiResponse.server_error(str(e))

# CREATE
@router.post("/", response_model=ApiResponse[dto.CategoryDTO], status_code=status.HTTP_201_CREATED)
def create(
  name: str = Form(...),
  file: UploadFile = File(...),
  db: Session = Depends(get_db)
):
  if not file.content_type.startswith("image/"):
    return ApiResponse.bad_request("El archivo debe ser una imagen")

  try:
    result = service.create_with_images(
      name=name,
      file=file,
      db=db
    )
      
    return ApiResponse.created(result)
  except ValueError as e:
    return ApiResponse.bad_request(str(e))
  except Exception as e:
    return ApiResponse.server_error(str(e))

# DELETE
@router.delete("/{id}", response_model=ApiResponse[object], status_code=status.HTTP_202_ACCEPTED)
def delete(id: int, db: Session = Depends(get_db)):
  try:
    result = service.delete_with_images(id, db)

    return ApiResponse.deleted(result)
  except ValueError as e:
    return ApiResponse.bad_request(str(e))
  except Exception as e:
    return ApiResponse.server_error(str(e))
