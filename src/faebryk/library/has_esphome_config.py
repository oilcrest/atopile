# This file is part of the faebryk project
# SPDX-License-Identifier: MIT

from abc import abstractmethod

from faebryk.core.core import NodeTrait


class has_esphome_config(NodeTrait):
    @abstractmethod
    def get_config(self) -> dict: ...
