from typing import List, Optional

from sqlalchemy import func
from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends, HTTPException, Response, status

from .. import models, oauth2, schemas
from ..database import get_db

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)


# @router.get("/", response_model=List[schemas.Post])
@router.get("/", response_model=List[schemas.PostOut])
def get_all_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user),
                  limit: int = 100, skip: int = 0, search: Optional[str] = ""):
    # cursor.execute("""SELECT * FROM posts""")
    # posts = cursor.fetchall()

    # It retrieves all posts of all users: Public behaviour of our API
    # posts = db.query(models.Post).all()

    # posts = db.query(models.Post).filter(
    #    models.Post.owner_id == current_user.id).all() # It only retrieves all of my posts: Private behaviour of our API

    # posts = db.query(models.Post).filter(
    #    models.Post.title.contains(search)).limit(limit).offset(skip).all()

    posts = db.query(models.Post, func.count(models.Vote.post_id).label(
        "votes")).join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()

    return posts


@ router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_a_post(post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute(
    #    """INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *""", (post.title, post.content, post.published))
    # new_post = cursor.fetchone()
    # conn.commit()

    # print(current_user.id)
    # print(current_user.email)
    new_post = models.Post(owner_id=current_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post


# @router.get("/{id}", response_model=schemas.Post)
@router.get("/{id}", response_model=schemas.PostOut)
def get_post_by_id(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute("""SELECT * FROM posts WHERE id = %s""", (id,))
    # post = cursor.fetchone()

    # post = db.query(models.Post).filter(models.Post.id == id).first()
    post = db.query(models.Post, func.count(models.Vote.post_id).label(
        "votes")).join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with {id = } was not found"
        )

    return post


@ router.put("/{id}", response_model=schemas.Post)
def update_post_by_id(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute(
    #     """UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""",
    #     (post.title, post.content, post.published, str(id)))
    # updated_post = cursor.fetchone()
    # conn.commit()

    post_query = db.query(models.Post).filter(models.Post.id == id)

    post = post_query.first()

    if post == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with {id = } does not exist"
        )

    if post.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Not authorized to perform requested action"
        )

    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()

    return post_query.first()


@ router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post_by_id(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", (id,))
    # deleted_post = cursor.fetchone()
    # conn.commit()

    post_query = db.query(models.Post).filter(models.Post.id == id)

    post = post_query.first()

    if post == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with {id = } does not exist"
        )

    if post.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Not authorized to perform requested action"
        )

    post_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
