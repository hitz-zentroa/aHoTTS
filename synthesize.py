import argparse
import subprocess
import os
import shutil
from huggingface_hub import hf_hub_download

def synthesize(text, language, model,output):
    if(language=='eu'):
        script = f"""
        echo "{text}" | iconv -f UTF-8 -t ISO-8859-1 | ./ahotts/tts -Lang={language} -Method=Vits -HDic=./ahotts/dicts/{language}/eu_dicc -voice_path=./ahotts/voices/{language}/{model} ./output/{output}.wav
        """
    elif(language=='gl'):
        script = f"""
        echo "{text}" | ./ahotts/tts -Lang={language} -Method=Vits -HDicDB=./ahotts/dicts/{language}/cotovia -voice_path=./ahotts/voices/{language}/{model} ./output/{output}.wav
        """
    elif(language=='ca'):
        script = f"""
        echo "{text}" | ./ahotts/tts -Lang={language} -Method=Vits -HDic=./ahotts/dicts/{language}/espeak-ng-data -voice_path=./ahotts/voices/{language}/{model} ./output/{output}.wav
        """
    elif(language=='es'):   
        script = f"""
        echo "{text}" | iconv -f UTF-8 -t ISO-8859-1 | ./ahotts/tts -Lang={language} -Method=Vits -HDic=./ahotts/dicts/{language}/es_dicc -voice_path=./ahotts/voices/{language}/{model} ./output/{output}.wav
        """
    subprocess.run(script, shell=True)
    print("Synthesis completed. Output file:", "./output/" + output + ".wav")



if __name__ == "__main__":
    vocesCa = ["bet", "eli", "eva", "jan", "mar", "ona", "pau", "pep", "pol"]
    vocesEu = ["antton", "maider"]
    vocesEs = ["laura", "alejandro"]
    vocesGl = voces = ["brais", "celtia", "iago", "icia", "paulo", "sabela"]
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--text', type=str, required = True, help='text to synthesize')
    parser.add_argument('-l', '--language', type=str,required = True, choices=['eu', 'gl','ca','es'], help='language')
    parser.add_argument('-m', '--model', type=str,required = True, help='voice used for synthesis')
    parser.add_argument('-o', '--output', type=str,required = True, help='output file name')
    args = parser.parse_args()
    model_dir = "./ahotts/voices/" + args.language + "/" + args.model + ""
    repo_id = "HiTZ/TTS-" + args.language + "_" + args.model + ""
    filename = "vits.onnx"
    if args.language == 'ca':
        modelos_validos = vocesCa
    elif args.language == 'eu':
        modelos_validos = vocesEu
    elif args.language == 'gl':
        modelos_validos = vocesGl
    elif args.language == 'es':
        modelos_validos = vocesEs
        
    if args.model not in modelos_validos:
        parser.error(f"The selected voice is not valid for this language: {args.language}. Please, select a voice from the following list: {modelos_validos}")
    if os.path.isfile(model_dir + "/vits.onnx"):
        print("Model already downloaded")
    else:
        print("Please wait while the model is downloaded (you will need internet connection)")
        file_path = hf_hub_download(
            repo_id=repo_id,
            filename=filename,
        )
        os.makedirs(model_dir, exist_ok=True)
        dest_path = os.path.join(model_dir, "vits.onnx")
        shutil.copy2(file_path, dest_path)
    
    synthesize(args.text, args.language, args.model,args.output)


