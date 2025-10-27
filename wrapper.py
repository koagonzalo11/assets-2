import functools
import importlib.machinery
import importlib.util
import os


def WrapperDir():
    return os.path.dirname(__file__)


def WrapperPath():
    return os.path.join(WrapperDir(), "repo")


@functools.lru_cache(maxsize=None)
def Wrapper():
    modname = "wrapper"
    loader = importlib.machinery.SourceFileLoader(modname, WrapperPath())
    spec = importlib.util.spec_from_loader(modname, loader)
    module = importlib.util.module_from_spec(spec)
    loader.exec_module(module)
    return module
