import logging

from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from stp_database.models.STP import Employee
from stp_database.repo.Questions.requests import QuestionsRequestsRepo

from tgbot.filters.admin import AdminFilter

admin_router = Router()
admin_router.message.filter(AdminFilter())
admin_router.message.filter(F.chat.type == "private")
admin_router.callback_query.filter(F.message.chat.type == "private")

logger = logging.getLogger(__name__)


@admin_router.message(CommandStart())
async def admin_start(
    message: Message,
    state: FSMContext,
    user: Employee,
    questions_repo: QuestionsRequestsRepo,
) -> None: ...
