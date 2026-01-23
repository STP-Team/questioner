from typing import Any

from aiogram_dialog import Dialog, DialogManager, Window
from aiogram_dialog.widgets.input import MessageInput, TextInput
from aiogram_dialog.widgets.kbd import Row, SwitchTo
from aiogram_dialog.widgets.text import Const

from tgbot.dialogs.events.user.q_create import (
    link_error,
    on_link_success,
    on_message_input,
    validate_link,
)
from tgbot.dialogs.states.user.main import QuestionSG
from tgbot.dialogs.widgets.buttons import HOME_BTN

question_text = Window(
    Const("""🤔 <b>Суть вопроса</b>

Отправь вопрос и вложения одним сообщением"""),
    MessageInput(on_message_input),
    HOME_BTN,
    state=QuestionSG.question_text,
)


question_link = Window(
    Const("""🗃️ <b>Регламент</b>

Прикрепи ссылку на регламент из клевера, по которому у тебя вопрос"""),
    TextInput(
        id="link",
        type_factory=validate_link,
        on_success=on_link_success,
        on_error=link_error,
    ),
    Row(
        SwitchTo(
            Const("↩️ Назад"),
            id="back",
            state=QuestionSG.question_text,
        ),
        HOME_BTN,
    ),
    state=QuestionSG.question_link,
)


async def on_start(_on_start: Any, _dialog_manager: DialogManager, **_kwargs):
    """Установка параметров диалога по умолчанию при запуске.

    Args:
        _on_start: Дополнительные параметры запуска диалога
        _dialog_manager: Менеджер диалога
    """


question_dialog = Dialog(question_text, question_link, on_start=on_start)
