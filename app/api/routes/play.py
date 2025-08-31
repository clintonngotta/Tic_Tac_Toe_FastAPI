from fastapi import APIRouter,HTTPException
from fastapi.responses import JSONResponse
from app.api.schemas import GameStatusResponse, BoardStateCheckModel, BoardStateModel, GameStateEnum

from app.engine.engine import play_game,get_game_status, reset_game

router = APIRouter(tags=["play"])

@router.post("/play", response_model=GameStatusResponse)
def play(state: BoardStateModel):           
    try: 
        status =  play_game(state.current_player,state.state) 
        status['status'] = get_game_state(status)
        return JSONResponse(status_code=200, content= status) 
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@router.post("/game_status")
def play(state: BoardStateCheckModel):   
    
    try:
        status =  get_game_status(state.state)       
        status['status'] = get_game_state(status)
        return JSONResponse(status_code=200, content=status)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")



@router.post("/reset_game")
def play():   
    try:
        status =  reset_game()
        return JSONResponse(status_code=200, content=status)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

def get_game_state(status:GameStatusResponse):    
    state_of_game =""
    if status['is_game_over']:
        state_of_game=GameStateEnum.draw if status['is_draw'] else GameStateEnum.win
    elif status['is_draw']:
        state_of_game=GameStateEnum.draw
    else:
        state_of_game=GameStateEnum.ongoing
    return state_of_game