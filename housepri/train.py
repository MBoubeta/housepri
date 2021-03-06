import numpy as np
from sklearn.model_selection import train_test_split
from housepri.config.set_config import config
from housepri.pipeline.set_pipeline import price_pipe
from housepri.process.data_manager import load_dataset, save_pipeline


def train() -> None:

    """Train the model."""

    # read training data
    data = load_dataset(file_name=config.app_config.training_data_file)

    # divide train and test
    X_train, X_test, y_train, y_test = train_test_split(
        data[config.model_config.features],
        data[config.model_config.target],
        test_size=config.model_config.test_size,
        # we are setting the random seed here
        # for reproducibility
        random_state=config.model_config.random_state,
    )
    y_train = np.log(y_train)

    # fit model
    price_pipe.fit(X_train, y_train)

    # persist trained model
    save_pipeline(pipeline_to_persist=price_pipe)


if __name__ == "__main__":
    train()
