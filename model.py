from deeppavlov import build_model


def infer(model, query):
    answer = model([query])[0][0]
    if answer != 'Cellular respiration is the set of the metabolic reactions and processes that take place in the cells of organisms to convert biochemical energy from nutrients into adenosine triphosphate (ATP), and then release waste products.':
        return answer
    else:
        return 'Sorry, cannot answer your question. Please, ask again.'


def load(config_path='model_config.json'):
    return build_model(config_path)
