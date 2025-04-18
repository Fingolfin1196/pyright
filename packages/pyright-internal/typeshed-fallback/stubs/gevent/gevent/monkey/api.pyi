from types import ModuleType
from typing import Any

def get_original(mod_name: str, item_name: str) -> Any: ...
def patch_item(module: ModuleType, attr: str, newitem: object) -> None: ...
def remove_item(module: ModuleType, attr: str) -> None: ...
def patch_module(target_module: ModuleType, source_module: ModuleType, items: list[str] | None = None) -> bool: ...
