import logging
from pathlib import Path
from typing import Any

from torch.utils.tensorboard import SummaryWriter

logger = logging.getLogger(__name__)

class LightGBMTensorBoardCallback:
    """
    Custom callback for plotting validation metrics in TensorBoard during
    LightGBM training.
    """
    def __init__(self, logdir: Path, activate: bool = True):
        self.activate = activate
        self.writer = None
        if self.activate:
            self.writer = SummaryWriter(f"{str(logdir)}/tensorboard")

    def __call__(self, env: Any) -> None:
        """
        Callback function executed at each iteration.
        """
        if not self.activate or not self.writer:
            return
            
        if not env.evaluation_result_list:
            return

        # evaluation_result_list contains tuples:
        # (data_name, eval_name, result, is_higher_better)
        for data_name, eval_name, result, _ in env.evaluation_result_list:
            # Match the XGBoost tag format e.g. "validation-rmse" or "train-rmse"
            # LightGBM typically outputs data_name like "training" or "valid_1"
            self.writer.add_scalar(f"{data_name}-{eval_name}", result, env.iteration)

    def close(self):
        """
        Close the writer to flush the logs to disk.
        """
        if self.activate and self.writer:
            self.writer.flush()
            self.writer.close()
