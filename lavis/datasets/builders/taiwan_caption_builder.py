from lavis.datasets.builders.base_dataset_builder import BaseDatasetBuilder
from lavis.datasets.datasets.taiwan_caption_datasets import TaiwanCaptionDatasets

from lavis.common.registry import registry

@registry.register_builder("taiwan_captions")
class TaiwanCaptionBuilder(BaseDatasetBuilder):
    train_dataset_cls = TaiwanCaptionDatasets
    eval_dataset_cls = TaiwanCaptionDatasets

    DATASET_CONFIG_DICT = {
        "default":"configs/datasets/taiwan_cap/defaults.yaml"
    }