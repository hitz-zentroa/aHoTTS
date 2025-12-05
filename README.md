# Aholab TTS Synthesis models
## Description
This repository contains a collection of text-to-speech (TTS) models and the necessary tools to synthesize speech for Basque (eu), Galician (gl), Catalan (ca) and Spanish (es). All voices are based on the VITS architecture proposed by [Kim et al. (2021)](https://arxiv.org/abs/2106.06103).   
*** The TTS models are not uploaded to this Github repository, they are uploaded to a HuggingFace repo. The download is done automatically when the synthesize.py script is runned. ***

* Basque [eu]:  
    - antton   
    - maider  
* Galician [gl]:  
    - [brais](https://huggingface.co/HiTZ/TTS-gl_sabela)  
    - celtia  
    - iago  
    - icia  
    - paulo  
    - [sabela](https://huggingface.co/HiTZ/TTS-gl_sabela)   
* Catalan [ca]:  
    - pau  
    - ona  
    - bet  
    - eli  
    - eva  
    - jan  
    - mar  
    - pep  
    - pol  
* Spanish [es]:
    - laura
    - alejandro  

## Uses  
This models are intented to be used for speech synthesis in Basque, Galician, Catalan and Spanish.  
## Installation  
You will need to install huggingface_hub package with the following command.  
```pip install huggingface_hub```
## How to use
### Python
Use the synthesize.py script to generate speech. All available models are listed in the sections above. Before running the script, navigate to the repository directory:  
```cd Ahotts```

For help:  
```python3 synthesize.py -h```    
Example commands:  
```bash
python3 synthesize.py -t "Antton naiz, zer moduz zaude." -l eu -m antton -o audio_name  
python3 synthesize.py -t "Soy Laura, qué tal estás?" -l es -m laura -o audio_name  
python3 synthesize.py -t "Sóc Ona, com estàs." -l ca -m ona -o audio_name
python3 synthesize.py -t "Son Brais, como estás." -l gl -m brais -o audio_name
```  

The synthesized audio is saved as a .wav file inside the **output/** directory.  
Use ```--output``` / ```-o``` to specify the filename.    

## Additional information
### Voice Resource Licenses and references
* Galician  
  - Celtia  
    Public Creative Commond Attribution 4.0 International License  
    [Vázquez Abuín, M., García Díaz, N., Vladu, A. I., Magariños, C., Vidal Miguéns, A., & Fernández Rei, E. (2023). Nos_Celtia-GL: Galician TTS corpus (1.0.0.) [Data set]. Zenodo.](https://doi.org/10.5281/zenodo.7716958)  
  - Brais  
    Public Creative Commond Attribution 4.0 International License  
    [Vladu, A. I., García Díaz, N., Regueira Fernández, X. L., Magariños, C., Moscoso Sánchez, A., Fernández López, D., Fernández Rei, E., & Dubert-García, F. (2025). Nos_Brais-GL: Galician TTS corpus [Data set]. Zenodo](https://doi.org/10.5281/zenodo.14265241)  
  - Sabela/Icia/Iago/Paulo   
    Public Creative Commond Attribution 4.0 International License  
    [Centro Ramón Piñeiro para a Investigación en Humanidades (CRPIH), & Multimedia Technology Group (GTM) – atlanTTic Research Center for Telecommunication Technologies. (2023). CRPIH_UVigo-GL-Voices: Galician TTS dataset (1.0.0.) [Data set]. Zenodo.](https://doi.org/10.5281/zenodo.8027725)  
* Catalan  
    - Creative Commons Attribution-ShareAlike 4.0 International Public License [festcat_trimmed_denoised](https://huggingface.co/datasets/projecte-aina/festcat_trimmed_denoised)
* Basque
    - Maider, Antton: developed by HiTZ with funding from Project ILENIA. Public Creative Commond Attribution 4.0
* Spanish
    - Alejandro: Developed in HiTZ from [openSLR dataset.](https://openslr.org/39/)
    - Laura: Acquired in [ELRA ID: ELRA-S0309](https://catalog.elra.info/en-us/repository/browse/ELRA-S0309/)
### Authors
HiTZ Basque Center for Language Technology - Aholab Signal Processing Laboratory, University of the Basque Country EHU.  
### Contact information
Ibon Saratxaga: ibon.saratxaga@ehu.eus
### Licensing Information
[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)
### Funding
Catalan and Galician have been funded by the project with reference numbers 2022/TL22/00215337, 2022/TL22/00215336, 2022/TL22/00215335, and 2022/TL22/00215334 is funded by the Ministry of Digital Transformation and by the Recovery, Transformation and Resilience Plan – Funded by the European Union – NextGenerationEU.
### Citation information  
Hernaez, I., Navas, E., Murugarren, J.L., Etxebarria, B. (2001) Description of the AhoTTS system for the Basque language. Proc. 4th ISCA ITRW on Speech Synthesis (SSW 4), paper 202