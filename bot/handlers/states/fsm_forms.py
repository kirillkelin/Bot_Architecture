from aiogram.fsm.state import StatesGroup, State

"""
здесь описываются возможные состояния
"""

class Auth(StatesGroup):
    email = State()
    password = State()