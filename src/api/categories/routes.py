from typing import List
from fastapi import APIRouter, Depends, File, Form, UploadFile, status
from sqlalchemy.orm import Session

from src.api.categories.service import create_with_images
from src.api.categories import repository
from src.api.categories.dto import CategoryDTO
from src.core.database import get_db
from src.shared.dtos import ApiResponse

router = APIRouter(prefix="/categories", tags=["categories"])

# GetAll
@router.get(
  "/",
  response_model=ApiResponse[List[CategoryDTO]],
  status_code=status.HTTP_200_OK
)
def get_all(db: Session = Depends(get_db)):
  try:
    items = repository.get_all(db)
    return ApiResponse.success(data=items)
  except Exception as e:
    return ApiResponse.server_error(str(e))

# Create
@router.post(
  "/",
  response_model=ApiResponse[CategoryDTO],
  status_code=status.HTTP_201_CREATED
)
def create(
  name: str = Form(...),
  file: UploadFile = File(...),
  db: Session = Depends(get_db)
):
  if not file.content_type.startswith("image/"):
    return ApiResponse.bad_request("El archivo debe ser una imagen")

  try:
    result = create_with_images(
      name=name,
      file=file,
      db=db
    )
      
    return ApiResponse.created(result)
  except ValueError as e:
    return ApiResponse.bad_request(str(e))
  except Exception as e:
    return ApiResponse.server_error(str(e))
