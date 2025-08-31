from pydantic import BaseModel
from typing import List,Optional
from enum import IntEnum, StrEnum

class CellValue(IntEnum):
    """Enum for valid cell values in THE BOARD"""
    EMPTY = 0
    X = -1 
    O = 1 
    
    
class CurrentPlayer(StrEnum):
    X="X"
    O="O"

class GameStateEnum(StrEnum):
    win="win"
    draw="draw"
    ongoing="ongoing"


class GamePlayResponse(BaseModel):
    """Response model for game status"""
    is_game_over: bool
    board:  Optional[List[List[int]]] = None
    winner: Optional[str] = None
    is_draw: bool
    state: GameStateEnum
    next_move: str

class GameStatusResponse(BaseModel):
    """Response model for game status"""
    is_game_over: bool
    board:  Optional[List[List[int]]] = None
    winner: Optional[str] = None
    is_draw: bool
    state: GameStateEnum
    
class BoardStateModel(BaseModel):
    state: List[List[CellValue]]
    current_player: CurrentPlayer

class BoardStateCheckModel(BaseModel):
    state: List[List[CellValue]]
     
    