from fishmlserv.model.manager import get_model_path, run_prediction
import typer

def prediction():
    typer.run(run_prediction)
