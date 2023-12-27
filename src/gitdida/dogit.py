from datetime import datetime
from git import Repo, GitCommandError
from gitdida.log import get_logger
from gitdida.config import settings

logger = get_logger("GitDida.doGit")


def run(repo_path, work_branch, remote_name="origin") -> (bool, str):
    """Do git work."""
    if repo_path is None:
        repo_path = settings.repo_path
    if work_branch is None:
        work_branch = settings.work_branch
    logger.info(
        "Run() Parameter is repository=%s, work_branch=%s, remote_name=%s",
        repo_path,
        work_branch,
        remote_name,
    )
    print(
        f"Run() Parameter is repository={repo_path}, work_branch={work_branch}, remote_name={remote_name}"
    )
    try:
        repo = Repo(repo_path)
        repo.git.fetch()
        repo.git.checkout(work_branch)
        repo.git.pull()
        repo.git.add("--all")
        if not repo.is_dirty():
            logger.info("Succeed. But nothing to commit.")
            return True, f"Nothing to commit. | {datetime.now()}"
        repo.index.commit(f"Git with Python :{datetime.now()}")
        repo.remotes[remote_name].push()
    except GitCommandError as e:
        # 捕捉git命令错误
        logger.error("Info：%s", str(e))
        return False, f"Info：{str(e)} | {datetime.now()} "

    logger.info("Succeed.")
    return True, f"Git with Python. | {datetime.now()}"
