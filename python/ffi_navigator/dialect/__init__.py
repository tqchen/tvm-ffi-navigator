"""Namespace for FFI export dialects"""
import os
from .tvm import TVMProvider
from .mxnet import MXNetProvider
from .torch import TorchProvider


def autodetect_dialects(root_path, resolver, logger):
    """Auto-detects which providers to use based on the root path.

    Parameters
    ----------
    root_path: str
        The root path for the project provided by a user or detected by
        a LSP client

    resolver : PyImportResolver
        Resolver for orginial definition.

    logger : Logger object

    Returns
    -------
    dialects: list of provider
    """
    dialects = []
    if os.path.exists(os.path.join(root_path, "python", "tvm")):
        dialects.append(TVMProvider(resolver, logger))
    elif os.path.exists(os.path.join(root_path, "python", "mxnet")):
        dialects.append(MXNetProvider(resolver, logger))
    elif os.path.exists(os.path.join(root_path, "python", "torch")):
        dialects.append(TorchProvider(resolver, logger))
    return dialects
