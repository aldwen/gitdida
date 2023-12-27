from gitdida.log import get_logger
from gitdida.config import settings
from dida365api.api import dida365
from dida365api.models.task import Task
import copy

logger = get_logger("GitDida.doDida")

# sys.path.append('src/dida365api')


def add_poor_task(dida: dida365, title: str):
    old_task_dict = dict()
    template_task = Task(old_task_dict)
    new_task_dict = copy.deepcopy(template_task.task_dict)
    new_task_dict[Task.TITLE] = title
    dida.post_task(Task.gen_add_date_payload(new_task_dict))


def run(git_succeed, message):
    """Simulate the dodida function."""
    logger.debug("parameter git_succeed=%s, message=%s", git_succeed, message)
    dida = dida365.Dida365()
    add_poor_task(dida, message)
    logger.info("Succeed.")
    return True, "Succeed."
