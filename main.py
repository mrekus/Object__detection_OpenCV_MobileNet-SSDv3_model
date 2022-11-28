import cv2
import matplotlib.pyplot as plt

config_file = "model_config/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
frozen_model = "ssd_mobilenet_v3_large_coco_2020_01_14/frozen_inference_graph.pb"
model = cv2.dnn_DetectionModel(frozen_model, config_file)
