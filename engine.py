# -*- encoding: utf-8 -*-
from __future__ import annotations
from process import handle, input, render
from utils import graphic, colors
from abc import abstractmethod

class GameLoop:
    def __init__(
        self,
        FPS: int,
        screen_width: int,
        screen_height: int,
    ) -> None:
        self.FPS = FPS
        self.screen = graphic.Screen(screen_width, screen_height)

    @abstractmethod
    def process(self):
        pass