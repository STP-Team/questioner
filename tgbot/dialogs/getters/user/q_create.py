from aiogram_dialog import DialogManager
from stp_database.models.STP import Employee
from stp_database.repo.Questions.requests import QuestionsRequestsRepo

from tgbot.misc.helpers import get_target_forum


async def confirmation_getter(
    user: Employee,
    questions_repo: QuestionsRequestsRepo,
    dialog_manager: DialogManager,
    **_kwargs,
):
    """Получение данных для подтверждения."""
    user_message = dialog_manager.dialog_data.get("user_message", {})
    link = dialog_manager.dialog_data.get("link", "")

    # Получаем настройки группы для проверки ask_clever_link
    target_forum_id = await get_target_forum(user)
    group_settings = await questions_repo.settings.get_settings_by_group_id(
        group_id=target_forum_id
    )

    ask_clever_link = group_settings.get_setting("ask_clever_link")

    result = {
        "user_text": user_message.get("text", "Без текста"),
        "has_attachments": "photo" in user_message or "document" in user_message,
        "link": link,
        "ask_clever_link": ask_clever_link,
    }

    return result
