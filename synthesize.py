import os
import sys
import argparse
import subprocess
import shlex
import shutil
import tempfile
import re
from huggingface_hub import hf_hub_download

script_file = os.path.abspath(__file__)
script_dir  = os.path.dirname(script_file)

def synthesize(text, language, model, output=None):
    use_tmp = False
    if output:
        if re.search(r"\.wav", output, re.IGNORECASE) is None:
            output += ".wav"
        out_path = output
    else:
        tmp = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
        out_path = tmp.name
        tmp.close()
        use_tmp = True

    quoted = shlex.quote(text)
    if(language=='eu'):
        script = f"echo {quoted} | iconv -f UTF-8 -t ISO-8859-1 | {script_dir}/ahotts/tts -Lang={language} -Method=Vits -HDic={script_dir}/ahotts/dicts/{language}/eu_dicc -voice_path={script_dir}/ahotts/voices/{language}/{model} {out_path}"
    elif(language=='gl'):
        script = f"echo {quoted} | {script_dir}/ahotts/tts -Lang={language} -Method=Vits -HDicDB={script_dir}/ahotts/dicts/{language}/cotovia -voice_path={script_dir}/ahotts/voices/{language}/{model} {out_path}"
    elif(language=='ca'):
        script = f"echo {quoted} | {script_dir}/ahotts/tts -Lang={language} -Method=Vits -HDic={script_dir}/ahotts/dicts/{language}/espeak-ng-data -voice_path={script_dir}/ahotts/voices/{language}/{model} {out_path}"
    elif(language=='es'):
        script = f"echo {quoted} | iconv -f UTF-8 -t ISO-8859-1 | {script_dir}/ahotts/tts -Lang={language} -Method=Vits -HDic={script_dir}/ahotts/dicts/{language}/es_dicc -voice_path={script_dir}/ahotts/voices/{language}/{model} {out_path}"

    subprocess.run(script, shell=True, stderr=subprocess.DEVNULL if use_tmp else None)

    if use_tmp:
        with open(out_path, 'rb') as f:
            sys.stdout.buffer.write(f.read())
        os.unlink(out_path)
    else:
        print(f"Synthesis completed. Output file: {out_path}", file=sys.stderr)

def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--text',     type=str, required = True, help='text to synthesize')
    parser.add_argument('-l', '--language', type=str,required = True,  choices=['eu', 'gl','ca','es'], help='language')
    parser.add_argument('-m', '--model',    type=str,required = True,  help='voice used for synthesis')
    parser.add_argument('-o', '--output',   type=str,                  help='output file name (omit to write to stdout)')
    args = parser.parse_args()
    return parser,args

if __name__ == "__main__":
    vocesCa = ["bet", "eli", "eva", "jan", "mar", "ona", "pau", "pep", "pol"]
    vocesEu = ["antton", "maider"]
    vocesEs = ["laura", "alejandro"]
    vocesGl = voces = ["brais", "celtia", "iago", "icia", "paulo", "sabela"]

    parser, args = getArgs()

    model_dir = f"{script_dir}/ahotts/voices/{args.language}/{args.model}"
    repo_id   = f"HiTZ/TTS-{args.language}_{args.model}"
    filename  = "vits.onnx"

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
        sys.exit(1)

    if os.path.isfile(model_dir + "/vits.onnx"):
        print("Model already downloaded", file=sys.stderr)
    else:
        print("Please wait while the model is downloaded (you will need internet connection)", file=sys.stderr)
        file_path = hf_hub_download(
            repo_id=repo_id,
            filename=filename,
        )
        os.makedirs(model_dir, exist_ok=True)
        dest_path = os.path.join(model_dir, "vits.onnx")
        shutil.copy2(file_path, dest_path)
    
    synthesize(args.text, args.language, args.model, output=args.output)
