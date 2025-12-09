"""
@author: AudioscavengeR
@title: Save WebP
@nickname: Save WebP
@description: Custom node to save your images in WebP.
"""


from .save_webp import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

WEB_DIRECTORY = "./web"

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS', "WEB_DIRECTORY"]

from aiohttp import web
from server import PromptServer
from pathlib import Path

if hasattr(PromptServer, "instance"):
  # NOTE: we add an extra static path to avoid comfy mechanism
  # that loads every script in web.
  PromptServer.instance.app.add_routes(
      [web.static("/save_webp", (Path(__file__).parent.absolute() / "assets").as_posix())]
  )

