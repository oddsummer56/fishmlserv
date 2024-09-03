import os
import pickle

def get_model_path():
    
    path = __file__

    # 현재 파일의 디렉토리 경로를 얻음
    my_path = os.path.dirname(path)

    # model.pkl 파일의 절대 경로를 생성
    model_path = os.path.join(my_path, "model.pkl")
    return model_path

def run_prediction(l:float, w:float):
    
    model_path = get_model_path()

    with open(model_path, "rb") as f:
        fish_model = pickle.load(f)

    p = fish_model.predict([[l, w]])

    if p[0] == 1:
        fish = '도미'
    else:
        fish = '빙어'
    
    print(fish)

    return fish
