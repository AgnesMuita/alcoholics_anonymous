from api.auth.schemas import LoginSchema
from db.db import db_session
from db.models.auth import LoginUser
from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class AuthService:
    def __init__(self, session: AsyncSession = Depends(db_session)):
        self.session = session

    async def get_all_users(self) -> list[LoginUser]:
        users = await self.session.execute(select(LoginUser))

        return users.scalars().fetchall()

    async def create_user(self, data: LoginSchema) -> LoginUser:
        user = LoginUser(**data.dict())
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)

        return user
  



