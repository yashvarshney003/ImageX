# ImageX
An Open Source image processing desktop app (under development). It provides some image processing features like super resolution, object detection*, image compression, and image fusion (multifocus). 

## Tech Stack and libraries 
- Tensorflow
- Keras
- PyQt5
- Python3 or above
- sciPy
- Pillow
- numPy and matplotlib

## Resources 
- **Dataset -** Here I used ImageCeleb dataset but this can be trained by other datasets too like VGG, etc.
- **Research paper -** Implemented this research [paper](https://arxiv.org/abs/1609.04802)   

## How to build
For builidng this you need to run `python3 ImageX_desktopApp.py`. This will open a desktop app which will provide you to select various features and then ask you to insert the image in which it will work on. Make sure you installed all the required libraries.

## Screenshot

<table>
    <tr>
          <td><img height="250" src="https://raw.githubusercontent.com/robustTechie/ImageX/main/screenshot/Screenshot%20from%202020-12-01%2001-58-13.png" /><br /><center><b>Desktop app</b></center></td>
    </tr>
</table>


<table>

<tr>
    <td><img height="250" src="https://github.com/robustTechie/ImageX/blob/main/screenshot/Screenshot%20from%202020-12-01%2002-14-21.png?raw=true"  /><br /><center><b>Low resolution Image</b></center>
    <td><img height="250" src="https://github.com/robustTechie/ImageX/blob/main/screenshot/Screenshot%20from%202020-12-01%2002-14-26.png?raw=true" /><br /><center><b>LR 2 image</b></center></td><td><img height="250" src="https://github.com/robustTechie/ImageX/blob/main/screenshot/Screenshot%20from%202020-12-01%2002-14-16.png?raw=true" /><br /><center><b>HR  generated Image</b></center></td> <td><img height="250" src="https://github.com/robustTechie/ImageX/blob/main/screenshot/Screenshot%20from%202020-12-01%2002-13-59.png?raw=true" /><br /><center><b>Original HR Image</b></center></td>
    </td>
    </tr>
    <tr>
    <td><img height="250" src="https://github.com/robustTechie/ImageX/blob/main/screenshot/Screenshot%20from%202020-12-01%2002-15-02.png?raw=true"  /><br /><center><b>Low resolution Image</b></center>
    <td><img height="250" src="https://github.com/robustTechie/ImageX/blob/main/screenshot/Screenshot%20from%202020-12-01%2002-15-09.png?raw=true" /><br /><center><b>LR 2 image</b></center></td><td><img height="250" src="https://github.com/robustTechie/ImageX/blob/main/screenshot/Screenshot%20from%202020-12-01%2002-14-55.png?raw=true" /><br /><center><b>HR  generated Image</b></center></td> <td><img height="250" src="https://github.com/robustTechie/ImageX/blob/main/screenshot/Screenshot%20from%202020-12-01%2002-15-31.png?raw=true" /><br /><center><b>Original HR Image</b></center></td>
    </tr>

</table>

### Todo
- Add object detection feature
- Image compression
- Image fusion
- Save/Load model

** Repo under development
