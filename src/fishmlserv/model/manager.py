def get_model_path():
    import os

    path = __file__

    # 현재 파일의 디렉토리 경로를 얻음
    my_path = os.path.dirname(path)

    # model.pkl 파일의 절대 경로를 생성
    model_path = os.path.join(my_path, "model.pkl")
    return model_path

