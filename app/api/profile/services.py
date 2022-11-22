from api.profile.schemas import UserCreateSchema
from db.db import db_session
from db.models.profile import User
from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class ProfileService:
    def __init__(self, session: AsyncSession = Depends(db_session)):
        self.session = session

    async def get_all_users(self) -> list[User]:
        users = await self.session.execute(select(User))

        return users.scalars().fetchall()

    async def create_user(self, data: UserCreateSchema) -> User:
        user = User(**data.dict())
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)

        return user
    async def edit_user(self, data: UserCreateSchema) -> User:
        user = User(**data.dict())
        self.session.edit(user)
        await self.session.commit()
        await self.session.refresh(user)

        return user

    async def delete_user(self, data: UserCreateSchema) -> User:
        user = User(**data.dict())
        self.session.delete(user)
        await self.session.commit()
        await self.session.refresh(user)

        return user


