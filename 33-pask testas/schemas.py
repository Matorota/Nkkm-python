from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime


class UserCreate(BaseModel):
    email: str
    password: str


class UserSmallInfo(BaseModel):
    id: int
    email: str

    class Config:
        orm_mode = True


class CarSettingsCreate(BaseModel):
    is_active: bool


class CarCreate(BaseModel):
    years: int
    model: str
    price: int
    settings: CarSettingsCreate


class SettingsCarInfo(BaseModel):
    id: int
    mileage: int
    time: int
    is_active: bool


class SettingsUserInfo(BaseModel):
    id: int
    consumption_km: str
    consumption_mp: str
    mel_km: str
    mel_mp: str
    rida: int
    is_active: bool


class CarBrands(BaseModel):
    id: int
    model: str
    is_active: bool


class Car(BaseModel):
    years: int
    price: int
    body: Optional[str] = None

    owner_id: int
    owner: Optional[UserSmallInfo]

    setting_id_car: int
    setting: SettingsCarInfo

    setting_id_user: int
    setting: SettingsUserInfo

    setting_id_brand: int
    setting: CarBrands


class Config:
    orm_mode = True


class User(BaseModel):
    id: int
    email: str
    password: str
    userCars: List[Car] = []

    class Config:
        orm_mode = True