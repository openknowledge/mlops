#!/usr/bin/env python3

import argparse
import logging
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import sys
sys.path.append('../lib')
# print(sys.path)

from TrainableInsuranceModel import TrainableInsuranceModel
from data import InsuranceData
from model import create_model, create_normalizer


def setup_logger() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.StreamHandler()
        ]
    )

def main(data_path: str, model_path: str) -> None:
    logging.info("Generate model for dataset %s", data_path)
    data_path = os.path.abspath(data_path)
    model_path = os.path.abspath(model_path)
    
    data = InsuranceData(data_path)
    X_train, _, _, _ = data.get_split()
    normalizer = create_normalizer(X_train)
    model = create_model(num_features=X_train.shape[1], num_categories=3, normalizer=normalizer)

    logging.info("Train model")

    trainableModel = TrainableInsuranceModel(model, data)
    trainableModel.train()
    ((_, train_metric), (_, test_metric)) = trainableModel.evaluate()
    logging.info(f"Model trained to train / test accuracy: {train_metric} / {test_metric}")

    logging.info("Save model to %s", model_path)
    trainableModel.save(model_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Training Script"
    )
    parser.add_argument(
        "-d",
        "--data-path",
        type=str,
        help="Path for training data.",
        required=True
    )
    parser.add_argument(
        "-m",
        "--model-path",
        type=str,
        help="Path for saving training model.",
        required=True
    )

    args = parser.parse_args()
    setup_logger()
    main(args.data_path, args.model_path)
