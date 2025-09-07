import re
from aqt import gui_hooks
from aqt.editor import Editor

def on_button_click(editor: Editor):
    if editor.currentField is None:
        return
    field_index = editor.currentField
    text = editor.note.fields[field_index]
    new_text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    if new_text != text:
        editor.note.fields[field_index] = new_text
        editor.loadNoteKeepingFocus()


def add_my_button(buttons, editor: Editor):
    btn = editor.addButton(
        icon=None,
        cmd="my_button",
        func=on_button_click,
        tip="Wrap backticks in <code>",
        label="Code"
    )
    buttons.append(btn)
    return buttons

gui_hooks.editor_did_init_buttons.append(add_my_button)
