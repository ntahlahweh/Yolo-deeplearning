from darkflow.net.build import TFNet

option = {
    "model": "cfg/tiny-yolo-voc-3c.cfg",
    "load": "bin/tiny-yolo-voc.weights",
    "batch": 8,
    "epoch": 100,
    "train": True,
    "annotation": "./hippocampal/annotation",
    "dataset": "./hippocampal/",
    "gpu": 1.0
}

tfnet = TFNet(option)
tfnet.train()