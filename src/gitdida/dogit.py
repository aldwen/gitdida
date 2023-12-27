"""
DoGit.

"""
from git import Repo, GitError, NoSuchPathError, InvalidGitRepositoryError
from gitdida.log import get_logger
from gitdida.config import settings

logger = get_logger("GitDida.doGit")


def run(repo_path, work_branch, remote_name) -> (bool, str):
    """Do git work."""
    if repo_path is None:
        if "repo_path" not in settings:
            logger.error(
                "'repo_path' was not defined in settings.toml, or no paramter gave."
            )
            return (
                False,
                "'repo_path' was not defined in settings.toml, or no paramter gave.",
            )
        repo_path = settings.repo_path
    if work_branch is None:
        if "work_branch" not in settings:
            logger.error(
                "'work_branch' was not defined in settings.toml, or no paramter gave."
            )
            return (
                False,
                "'work_branch' was not defined in settings.toml, or no paramter gave.",
            )
        work_branch = settings.work_branch
    if remote_name is None:
        print("remote_name is None")
        remote_name = getattr(settings, "remote_name", "origin")

    logger.info(
        "Run()'s Parameter is repository=%s, work_branch=%s, remote_name=%s",
        repo_path,
        work_branch,
        remote_name,
    )
    try:
        repo = Repo(repo_path)
        repo.git.fetch()
        repo.git.checkout(work_branch)
        repo.git.pull()
        repo.git.add("--all")
        if not repo.is_dirty():
            logger.info("Succeed. But nothing to commit.")
            return True, "Nothing to commit. "
        repo.index.commit("Auto commit by GitDida.")
        repo.remotes[remote_name].push()
    except NoSuchPathError as e:
        logger.error("指定的仓库路径不存在：%s", str(e))
        return False, f"指定的仓库路径不存在：{str(e)}"
    except InvalidGitRepositoryError as e:
        logger.error("无效的 Git 仓库：%s", str(e))
        return False, f"无效的 Git 仓库：{str(e)}"
    except GitError as e:
        logger.error("发生了一个 Git 错误：%s", str(e))
        return False, f"发生了一个 Git 错误：{str(e)}"

    logger.info("Succeed.")
    return True, "Do Git finished."
