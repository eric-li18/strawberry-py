from typing import List
from fastapi import APIRouter, Depends, HTTPException, Path, Body, Query
from sqlalchemy.orm import Session
from backend import crud, schemas
from .util import get_db


def get_item(
    item_id: int = Path(..., title="ID of item to get", ge=1),
):
    item = crud.item.get(db, item_id)
    if not item:
        raise HTTPException(
            status_code=404, detail=f"Item with id: {item_id} not found."
        )
    return item


def get_items():
    db = get_db()
    limit = 3
    items = crud.item.get_multi(db, limit)
    if not items:
        raise HTTPException(status_code=404, detail=f"Database is empty.")
    return items


def create_item(
    db: Session = Depends(get_db),
    item: schemas.ItemCreate = Body(..., title="Item to be created."),
):
    created_item = crud.item.create(db, item)
    return created_item


def remove_item(
    db: Session = Depends(get_db),
    item_id: int = Path(..., title="ID of item to delete."),
):
    item = crud.item.get(db, item_id)
    if not item:
        raise HTTPException(
            status_code=404, detail=f"Item with id: {item_id} not found."
        )
    crud.item.remove(db, item_id)
    return item


def update_item(
    db: Session = Depends(get_db),
    item: schemas.ItemUpdate = Body(..., title="Item fields to update."),
):
    updated_item = crud.item.update(db, item)
    if not updated_item:
        raise HTTPException(status_code=404, detail=f"Item not found.")
    return updated_item
