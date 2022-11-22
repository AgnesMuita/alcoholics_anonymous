from api.profile.schemas import UserCreateSchema, UserSchema, UserInDBSchema
from api.profile.services import ProfileService
from db.db import db_session
from db.models.profile import User
from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession

router = APIRouter()


@router.get("/", response_model=list[UserSchema])
async def get_user(
    session: AsyncSession = Depends(db_session),
) -> list[User]:
    profile_service = ProfileService(session=session)
    return await profile_service.get_all_users()


@router.post("/", response_model=UserSchema)
async def create_user(
    data: UserCreateSchema,
    session: AsyncSession = Depends(db_session),
) -> User:
    profile_service = ProfileService(session=session)
    auth = await profile_service.create_user(data)
    return auth

@router.put("/", response_model=UserSchema)
async def edit_user(
    data: UserSchema, 
    session:AsyncSession=Depends(db_session),
)->User:
    profile_service=ProfileService(session=session)
    auth=await profile_service.edit_user(data)
    return auth

@router.delete("/", response_model=UserSchema)
async def delete_user(
    data: UserSchema, 
    session:AsyncSession=Depends(db_session),
)->User:
    profile_service=ProfileService(session=session)
    auth=await profile_service.delete_user(data)
    return auth



