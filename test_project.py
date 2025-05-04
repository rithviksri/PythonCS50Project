import pytest
import json
from project import add_item, view_items, mark_complete, remove_item, save_to_file, load_from_file

def test_add_item():
    todo_list = []
    add_item(todo_list, "Test item")
    assert len(todo_list) == 1
    assert todo_list[0]["item"] == "Test item"
    assert not todo_list[0]["completed"]

def test_view_items(capfd):
    todo_list = [{"item": "Test item", "completed": False}]
    view_items(todo_list)
    out, _ = capfd.readouterr()
    assert "1. Test item [not done]" in out

def test_mark_complete():
    todo_list = [{"item": "Test item", "completed": False}]
    mark_complete(todo_list, "Test item")
    assert todo_list[0]["completed"]

def test_remove_item():
    todo_list = [{"item": "Test item", "completed": False}]
    remove_item(todo_list, "Test item")
    assert len(todo_list) == 0

def test_save_and_load():
    todo_list = [{"item": "Test item", "completed": False}]
    save_to_file(todo_list, "test_todo_list.json")
    loaded_list = load_from_file("test_todo_list.json")
    assert todo_list == loaded_list
