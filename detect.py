from torchvision.transforms.functional import pil_to_tensor
from pycocotools.coco import COCO
from torchvision.utils import draw_bounding_boxes
from torchvision.transforms.functional import to_pil_image

ANN_FILE = 'annotations/instances_val2017.json'
COCO = COCO(ANN_FILE)


def run_detection(image, object_detection_model):
    image_tensor_int = pil_to_tensor(image)
    image_tensor_int = image_tensor_int.unsqueeze(dim=0)
    image_tensor_float = image_tensor_int / 255.0
    object_detection_model.eval()
    image_predictions = object_detection_model(image_tensor_float)
    image_predictions[0]["boxes"] = image_predictions[0]["boxes"][image_predictions[0]["scores"] > 0.8]
    image_predictions[0]["labels"] = image_predictions[0]["labels"][image_predictions[0]["scores"] > 0.8]
    image_predictions[0]["scores"] = image_predictions[0]["scores"][image_predictions[0]["scores"] > 0.8]
    image_labels = COCO.loadCats(image_predictions[0]["labels"].numpy())
    image_annot_labels = ["{}-{:.2f}".format(label["name"], prob) for label, prob in
                          zip(image_labels, image_predictions[0]["scores"].detach().numpy())]

    output = draw_bounding_boxes(image=image_tensor_int[0],
                                 boxes=image_predictions[0]["boxes"],
                                 labels=image_annot_labels,
                                 colors=["red" if label["name"] == "person" else "green" for label in
                                         image_labels],
                                 width=2,
                                 font_size=15
                                 )

    img = to_pil_image(output)
    return img
