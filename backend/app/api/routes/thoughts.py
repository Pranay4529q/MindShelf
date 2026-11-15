from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from uuid import UUID
from app.database import get_db
from app.core.auth import require_owner
from app.models.thought import Thought
from app.schemas.thought import ThoughtCreate, ThoughtRead

router = APIRouter(prefix="/api/thoughts", tags=["thoughts"], dependencies=[Depends(require_owner)])

@router.post("", response_model=ThoughtRead, status_code=201)
def create_thought(payload: ThoughtCreate, db: Session = Depends(get_db)):
    thought = Thought(**payload.model_dump())
    db.add(thought)
    db.commit()
    db.refresh(thought)
    return thought

@router.get("", response_model=list[ThoughtRead])
def list_thoughts(db: Session = Depends(get_db)):
    return db.scalars(select(Thought).order_by(Thought.created_at.desc())).all()

@router.delete("/{thought_id}", status_code=204)
def delete_thought(thought_id: UUID, db: Session = Depends(get_db)):
    thought = db.get(Thought, thought_id)
    if thought is None:
        raise HTTPException(404, "Thought not found")
    db.delete(thought)
    db.commit()

@router.put("/{thought_id}", response_model=ThoughtRead)
def update_thought(thought_id: UUID, payload: ThoughtCreate, db: Session = Depends(get_db)):
    thought = db.get(Thought, thought_id)
    if thought is None:
        raise HTTPException(404, "Thought not found")
    for key, value in payload.model_dump().items():
        setattr(thought, key, value)
    db.commit()
    db.refresh(thought)
    return thought
