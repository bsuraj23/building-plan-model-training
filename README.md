# Building Plan Model Training

Training pipeline for asset/symbol detection from building plans (PDFs and AutoCAD PNGs) using YOLOv8

## Overview

This project provides a complete end-to-end pipeline for training a YOLOv8 object detection model to identify and detect assets/symbols in building plans. It supports processing both PDF files and AutoCAD PNG exports.

## Features

- ✅ PDF to PNG conversion utility
- ✅ YOLOv8 training pipeline
- ✅ Customizable dataset configuration
- ✅ Inference and prediction scripts
- ✅ Support for multiple asset/symbol classes
- ✅ Batch processing capabilities

## Project Structure

```
building-plan-model-training/
│
├── data/                # Raw PDFs and source files
├── images/              # Extracted PNG images from PDFs
├── annotations/         # Annotation files (YOLO format)
├── dataset/            # Organized dataset for training
│   ├── images/
│   │   ├── train/
│   │   └── val/
│   └── labels/
│       ├── train/
│       └── val/
├── training/            # Training scripts and configs
├── models/              # Saved model checkpoints
├── notebooks/           # Jupyter notebooks for exploration
├── utils/               # Utility scripts
│   └── pdf_to_png.py   # PDF conversion script
├── data.yaml            # YOLOv8 dataset configuration
├── requirements.txt     # Project dependencies
└── README.md
```

## Installation

### Prerequisites

- Python 3.8 or higher
- pip
- poppler-utils (for PDF processing)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/bsuraj23/building-plan-model-training.git
cd building-plan-model-training
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Install poppler-utils:

**Ubuntu/Debian:**
```bash
sudo apt-get install poppler-utils
```

**macOS:**
```bash
brew install poppler
```

**Windows:**
Download from: https://github.com/oschwartz10612/poppler-windows/releases

## Quick Start

### 1. Convert PDFs to Images

```bash
python utils/pdf_to_png.py data/ images/ --dpi 300
```

### 2. Annotate Images

Use annotation tools like:
- [LabelImg](https://github.com/tzutalin/labelImg)
- [makesense.ai](https://www.makesense.ai/)
- [Roboflow](https://roboflow.com/)
- [CVAT](https://github.com/opencv/cvat)

Export annotations in YOLO format.

### 3. Organize Dataset

Organize your images and labels into the dataset structure:
```
dataset/
  images/
    train/   # 80% of your images
    val/     # 20% of your images
  labels/
    train/   # Corresponding annotations
    val/     # Corresponding annotations
```

### 4. Configure Dataset

Edit `data.yaml` to match your classes:
```yaml
path: dataset
train: images/train
val: images/val
nc: 5  # Number of classes
names:
  0: switch
  1: lamp
  2: pipe
  3: vent
  4: duct
```

### 5. Train Model

```bash
yolo task=detect mode=train model=yolov8n.pt data=data.yaml epochs=50 imgsz=640
```

### 6. Run Inference

```bash
yolo task=detect mode=predict model=runs/detect/train/weights/best.pt source=images/test_image.png
```

## Training Options

### Basic Training
```bash
yolo detect train data=data.yaml model=yolov8n.pt epochs=50 imgsz=640
```

### Advanced Training
```bash
yolo detect train \
  data=data.yaml \
  model=yolov8m.pt \
  epochs=100 \
  imgsz=640 \
  batch=16 \
  patience=20 \
  save=True \
  project=building-plan-models \
  name=exp1
```

### Model Variants

- `yolov8n.pt` - Nano (fastest, least accurate)
- `yolov8s.pt` - Small
- `yolov8m.pt` - Medium (recommended)
- `yolov8l.pt` - Large
- `yolov8x.pt` - Extra Large (slowest, most accurate)

## Usage Examples

### Convert Single PDF
```bash
python utils/pdf_to_png.py plan1.pdf output/ --dpi 300
```

### Batch Convert PDFs
```bash
python utils/pdf_to_png.py data/ images/ --dpi 300
```

### Predict on Image
```bash
yolo detect predict model=models/best.pt source=test.png
```

### Predict on Folder
```bash
yolo detect predict model=models/best.pt source=images/test/
```

## Configuration

### data.yaml

The `data.yaml` file configures your dataset:

- `path`: Root directory of dataset
- `train`: Path to training images
- `val`: Path to validation images
- `nc`: Number of classes
- `names`: Dictionary mapping class IDs to names

### Training Parameters

- `epochs`: Number of training epochs (default: 100)
- `imgsz`: Input image size (default: 640)
- `batch`: Batch size (default: 16)
- `patience`: Early stopping patience (default: 50)
- `lr0`: Initial learning rate (default: 0.01)

## Common Issues

### PDF Conversion Errors

**Error:** `PDFInfoNotInstalledError`
**Solution:** Install poppler-utils

### CUDA Out of Memory

**Solution:** Reduce batch size:
```bash
yolo detect train data=data.yaml batch=8
```

### Low Model Accuracy

**Solutions:**
- Increase training epochs
- Use a larger model (e.g., yolov8m or yolov8l)
- Augment your dataset
- Improve annotation quality
- Increase dataset size

## Citation

If you use this project, please cite:

```bibtex
@software{building_plan_model_training,
  author = {Suraj Kumar Yadav},
  title = {Building Plan Model Training},
  year = {2025},
  url = {https://github.com/bsuraj23/building-plan-model-training}
}
```

## License

MIT License - See LICENSE file for details

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Contact

- GitHub: [@bsuraj23](https://github.com/bsuraj23)
- Email: [your-email@example.com]

## Acknowledgments

- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- [pdf2image](https://github.com/Belval/pdf2image)
- Building plan datasets and annotation tools

---

**Note:** Update the class names in `data.yaml` to match your specific building plan symbols before training.
