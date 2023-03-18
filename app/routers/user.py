from typing import List

from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends, HTTPException, status

from .. import models, schemas, utils
from ..database import get_db

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_a_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    query = db.query(models.User).filter(models.User.email == user.email)
    if query.first() != None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f"Email {user.email} has already been used to create an user")

    user.password = utils.hash(user.password)

    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get("/", response_model=List[schemas.UserAllOut])
def get_all_users(db: Session = Depends(get_db)):

    users = db.query(models.User).all()

    if not users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No users available"
        )

    return users


@router.get("/{id}", response_model=schemas.UserOut)
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with {id = } does not exist"
        )

    return user
