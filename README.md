# Traffic Vehicle Detector Demo Application

Web application allows to detect vehicles (trucks, cars, bikes, and so on) on the road. This task can be applied to the
road cameras to track/count vehicles to solve different problems, e.g. count daily traffic, apply payments on the paid
roads (bikes and moto usually are free, truck and small car fees differ), etc

Web application exposes simple UI that allows a user to Drag&Drop a phot image with each identified vehicle. 

Web application is built on top of Faster-RCNN and SSD300 models (UI enables a control for the selection).
Both models are available in Torch model ZOO.

## Plan of work

**Selected track:** **Product**

**Demo:** [**link**](https://drive.google.com/file/d/1p9G7cdG3xaGUjCKL-zyYq9AoX1w7RzxZ/view?usp=sharing)

|Stage | Status |
|:---|:---|
| Problem search and solution description | ✅ |
| Search for pretrained model and corresponding dataset | ✅ |
| Framework selection | ✅ |
| Development of MVP | ✅ |
| Testing demo | ✅ |
| Deployment | ✅ |


### 1. Problem search and solution description

1. Problem solved: **Vision-based vehicle detection** [1]. Identification of vehicles on the photo.
2. Target audience: **Road workers**, **Traffic Police**

### 2. Search for pretrained model and corresponding dataset

1. Selected model 1: [Faster-RCNN](https://pytorch.org/vision/main/models/faster_rcnn.html)
2. Selected model 2: [SSD-300 VGG](https://pytorch.org/vision/main/models/generated/torchvision.models.detection.ssd300_vgg16.html)
3. No need for a dataset, models are already pretrained

### 3. Framework selection

Solution is based on:

1. [Flask](https://flask.palletsprojects.com/en/2.3.x/) - framework for building web applications
   that expose REST API and serve static files
2. [React](https://react.dev/) - library for building SPA web applications
3. [React Material-UI](https://mui.com/) - Material UI, fully-loaded component library
4. [PyTorch](https://pytorch.org/) - framework for designing DL pipelines, training and inference
   of DL models
5. [Docker](https://www.docker.com/) - containerizing solution for web applications

### 4. Development of MVP

Code is located in [root](./) folder:

* [./frontend](./frontend) - UI for application
* [./app.py](./app.py) - server code with all REST API endpoint

### 5. Testing demo

**Proposed test scenario:**

1. Download [image](img/traffic.jpg).
2. Launch application with `docker-compose up -d --build`
3. Open Web application: [http://localhost:3000/](http://localhost:3000/)
4. Select this image:
   ![](img/traffic.jpg)
5. Click **Detect**
6. Inspect results:
   ![](img/res.png)


### 6. Deployment

Web application is available at localhost on Docker launch:

```commandline
docker-compose up -d --build
```

[1]: https://etrr.springeropen.com/articles/10.1186/s12544-019-0390-4