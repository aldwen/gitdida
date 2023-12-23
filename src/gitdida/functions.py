def RunGitandDida() -> (bool, str):
    return False, "Need a git repository."


# ---
# import sys
# from datetime import datetime
# from config import settings
# from autogit import run
# from src.wenutils.log import get_logger

# sys.path.append('src/didaapi')
# from didaapi.api import dida365

# logger = get_logger('main')


# def add_poor_task(dida:dida365, title:str):
#     old_task_dict =dict()
#     template_task = Task(old_task_dict)
#     new_task_dict = copy.deepcopy(template_task.task_dict)
#     new_task_dict[Task.TITLE] = title
#     dida.post_task(Task.gen_add_date_payload(new_task_dict))

# if __name__ == '__main__':
#     logger.info(f"Working in :{settings.repo_path}")
#     print(f"Working in :{settings.repo_path}")
#     success, message = run.commit_and_push(settings.repo_path,settings.work_branch,'gitee')

#     dida = dida365.Dida365()
#     if success:
#         logger.info(f"Successed at {datetime.now()}")
#         print("Success:",message)
#     else:
#         logger.warning(f"Error:{message}")
#         print(f"Error:{message}")
#         add_poor_task(dida, message)
