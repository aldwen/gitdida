from datetime import datetime
from git import Repo, GitCommandError
from gitdida.log import get_logger

logger = get_logger(__name__)


def run(repository, work_branch, remote_name="origin"):
    """Do git work."""
    logger.info(
        "Run dogit.py parameter is repository:{repository}, work_branch:{work_branch},remote_name:{remote_name}"
    )
    try:
        repo = Repo(repository)
        repo.git.fetch()
        repo.git.checkout(work_branch)
        repo.git.pull()
        repo.git.add("--all")
        repo.index.commit(f"Git with Python :{datetime.now()}")
        repo.remotes[remote_name].push()
        logger.info("Success.")
        return True, f"Git with Python. | {datetime.now()}"

    except GitCommandError as e:
        # 捕捉git命令错误
        logger.warning("Error!")
        return False, f"Info：{str(e)} | {datetime.now()} "
