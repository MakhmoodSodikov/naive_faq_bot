from deeppavlov import configs, train_model
from deeppavlov.core.common.file import read_json
import json
import os


def train(data='wiki_train.csv', save_path='model_config.json'):
    os.environ["CUDA_VISIBLE_DEVICES"] = "3"
    model_config = read_json(configs.faq.tfidf_logreg_en_faq)
    model_config['dataset_reader']['data_path'] = data
    model_config['dataset_reader']['data_url'] = None

    model = train_model(model_config)
    save(model_config, save_path)


def save(model_config, save_path):
    with open(save_path, 'w') as outfile:
        json.dump(model_config, outfile)