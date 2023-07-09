"""main execution"""

import itertools
import logging
from pathlib import Path
from typing import Tuple

import yaml

from src.script import Script, find_script

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    # filename="wrangler.log",
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def load_scripts_from_yamls(_paths: list[Path]) -> list[Script]:
    """instantiates Script instances from yaml files"""
    results = []
    for _path in _paths:
        logger.info("extracting scripts from %s", _path)
        with open(_path, "r", encoding="utf-8") as _file:
            results.extend(
                (Script(name, data) for (name, data) in yaml.safe_load(_file).items())
            )
    return results


def get_bookend_scripts_content(scripts: list[Script]) -> Tuple[list[str], ...]:
    """returns the prepend and postpend scripts if thy exist"""
    _prepend_script = find_script("^pre", scripts)
    _postpend_script = find_script("^post", scripts)
    return (get_content(_prepend_script), get_content(_postpend_script))


def get_content(_script: Script) -> list[str]:
    """returns the main content of a Script as Lua

    The content excludes anything not in the list below as they need to be
    treated differently with respect to parsing and ordering.

    * modulepaths
    * modules
    * environment
    """
    return list(
        itertools.chain(
            *[_script.get_as_lua(x) for x in ("modulepaths", "modules", "environment")]
        )
    )


def write_scripts_to_lua(output_path: Path, scripts: list[Script]) -> None:
    """outputs lua scripts from Script instances to output_path"""
    prepend_script, postpend_script = get_bookend_scripts_content(scripts)
    for script in [x for x in scripts if "^" not in x.name]:
        write_script_to_lua(output_path, prepend_script, postpend_script, script)


def write_script_to_lua(
    output_path: Path,
    prepend_script: list[str],
    postpend_script: list[str],
    script: Script,
):
    """writes the script to file with bookend script contents
    
    This method is responsible for preserving the necessary order in which
    each YAML file is parsed, converted to Lua, and written to disk and is 
    done so explicitly.
    """
    with open(
        Path(output_path / f"{script.name}.lua"), "w", encoding="utf-8"
    ) as _output:
        _output.writelines(script.get_as_lua("help"))
        _output.writelines(prepend_script)
        _output.writelines(script.get_as_lua("modulepaths"))
        _output.writelines(script.get_as_lua("modules"))
        _output.writelines(script.get_as_lua("environment"))
        _output.writelines(script.get_as_lua("^extra"))
        _output.writelines(postpend_script)
        _output.writelines(script.get_as_lua("whatis"))


def main():
    """main execution"""
    # data = get_cli_data()
    # _input = data["queue"]
    _input = Path("./tests/fixtures/test3.yaml")
    output_path = Path("./temp")
    output_path.mkdir(parents=True, exist_ok=True)
    write_scripts_to_lua(output_path, load_scripts_from_yamls([_input]))


if __name__ == "__main__":
    main()
