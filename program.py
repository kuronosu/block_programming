from typing import Any, Optional

from blocks.arithmetic import SumBlock
from blocks.base import BaseBlock, Context, Reference, Response
from blocks.operation import OperationBLock
from blocks.assignment import AssignBlock
from blocks.utility import InputBlock, ParseBlock, PrintBlock


class Program:
    def __init__(self) -> None:
        self.context = Context()
        self.blocks: list[BaseBlock] = []

    def run(self) -> list:
        return [block._execute(self.context) for block in self.blocks]

    def add_block(self, block: BaseBlock) -> None:
        self.blocks.append(block)


program = Program()
program.add_block(AssignBlock("a", ParseBlock(int, '1')))
program.add_block(AssignBlock("b", 2))
program.add_block(AssignBlock("c", 3))
program.add_block(AssignBlock("d", SumBlock(Reference("a"), Reference("b"))))
program.add_block(PrintBlock(
    SumBlock(Reference("a"), SumBlock(Reference("b"), Reference("c")))))
program.add_block(PrintBlock(Reference("d")))
program.add_block(PrintBlock(InputBlock("Enter name: ")))
program.run()
