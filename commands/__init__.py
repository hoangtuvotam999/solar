import os
import importlib
import logging

logger = logging.getLogger("solar")


def load_command_modules():
    modules = []

    current_dir = os.path.dirname(__file__)

    for filename in os.listdir(current_dir):
        if not filename.endswith(".py") or filename == "__init__.py":
            continue

        module_name = filename[:-3]
        module_path = f"commands.{module_name}"

        try:
            module = importlib.import_module(module_path)
        except Exception as e:
            logger.error("err import module %s: %s", module_name, e)
            continue

        if not hasattr(module, "NAME") or not hasattr(module, "handle"):
            logger.info(
                "module %s (doesnt have NAME or handle)", module_name
            )
            continue

        modules.append(module)
        logger.info("Loaded module: %s (NAME=%s)", module_name, module.NAME)

        # Debug: module have on_message 
        if hasattr(module, "on_message"):
            logger.info("Module %s have on_message hook", module_name)

    return modules
