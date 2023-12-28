from gitdida.log import get_logger
from gitdida.config import settings
from dida365api.api import dida365
from dida365api.models.task import Task
import copy

logger = get_logger("GitDida.doDida")

# sys.path.append('src/dida365api')


def add_poor_task(dida: dida365, title: str):
    newdict = {
        # "id": "某个唯一标识符",
        # "project_id": "所属项目的ID",
        "title": "2023-12-28",
        # "start_date": "开始日期",
        # "modified_time": "最后修改时间",
        # "created_time": "创建时间",
        # "due_date": "截止日期",
        # "repeat_flag": "重复标志",
        # "repeat_first_date": "首次重复日期",
        # "kind": "任务类型",
        # "completed_time": "完成时间",
        # "status": "任务状态",
    }
    # template_task = Task(dict())
    # new_task_dict = copy.deepcopy(template_task.task_dict)
    # new_task_dict[Task.TITLE] = title
    dida.post_task(Task.gen_add_date_payload(newdict))


# save a copy here
# def add_poor_task(dida: dida365, title: str):
#     # old_task_dict = dict()

#     template_task = Task(dict())
#     new_task_dict = copy.deepcopy(template_task.task_dict)
#     new_task_dict[Task.TITLE] = title
#     dida.post_task(Task.gen_add_date_payload(new_task_dict))

# def another_task(dida: dida365):
#     adict = dict()
#     adict[Task.TITLE] = "another"
#     adict[Task.DUE_DATE] = "2023-12-29"
#     dida.post_task(Task.gen_add_date_payload(adict))


def run(git_succeed, message):
    """Simulate the dodida function."""
    logger.debug("parameter git_succeed=%s, message=%s", git_succeed, message)
    dida = dida365.Dida365()
    add_poor_task(dida, message)
    logger.info("Succeed.")
    return True, "Succeed."
