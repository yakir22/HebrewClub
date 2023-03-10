from google.cloud import texttospeech
import boto3
import hashlib
import os
import shutil
import re
import pdb
# create data dir if not exist
os.makedirs('data', exist_ok=True)
os.makedirs('data/test', exist_ok=True)


def text_from_google(text):
    client = texttospeech.TextToSpeechClient()
    synthesis_input = texttospeech.SynthesisInput(text="Hello, World!")
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    with open("output.mp3", "wb") as out:
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')


def is_hebrew_char(char):
    # codepoint = ord(char)
    return '\u05D0' <= char <= '\u05EA'


def hebrew_text_from_google(input_string):
    # remove single character words from the string
    input_string_for_tts = ' '.join([word for word in input_string.split() if len(
        word) > 1 or not is_hebrew_char(word[0])])
    input_string_dummy = ' '.join(
        [word for word in input_string.split() if True])
    md5_hash = hashlib.md5(input_string.encode()).hexdigest()
    output_filename = f"{md5_hash}.mp3"
    final_filename = 'data/' + output_filename
    if os.path.exists(final_filename) and input_string_dummy == input_string_for_tts:
        return
    client = texttospeech.TextToSpeechClient()
    synthesis_input = texttospeech.SynthesisInput(text=input_string_for_tts)
    voice = texttospeech.VoiceSelectionParams(
        language_code='he-IL',
        name='he-IL-Wavenet-A',
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=synthesis_input,
        voice=voice,
        audio_config=audio_config
    )

    with open(final_filename, "wb") as out:
        out.write(response.audio_content)
    copy_file_to_test_folder(final_filename, input_string + '.mp3')
        # copy file using string as name


def copy_file_to_test_folder(source, destination):
    # Remove illegal characters from the destination filename
    destination = re.sub(r'[<>:"/\\|?*]', '_', destination)
    print('destination: ' + destination)
    # Copy the file to the destination
    shutil.copy2(source, 'data/test/' + destination)


def russian_text_to_speech(text):
    # pdb.set_trace()
    polly = boto3.client('polly')
    response = polly.synthesize_speech(
        Text=text, VoiceId='Maxim', OutputFormat='mp3', LanguageCode='ru-RU')
    with open('data/output.mp3', 'wb') as f:
        f.write(response['AudioStream'].read())

    print('Text has been converted to speech and saved to output.mp3')


# def hebrew_text_to_speech(text):
#     polly = boto3.client('polly')
#     response = polly.synthesize_speech(
#         Text=text, VoiceId='Carmit', OutputFormat='mp3', LanguageCode='he-IL')
#     with open('output.mp3', 'wb') as f:
#         f.write(response['AudioStream'].read())
#     print('Hebrew text has been converted to speech and saved to output.mp3')


# russian_text_to_speech("????????????! ?????? ?????????")
# hebrew_text_to_speech("???? ???????? ??????????")

sentences = [
  "???????????? ?????????? ( ???? ) ",
  "???????????? ?????? ?? ",
  "?????? ???????? ?????????? ?????? ???? ?????????? ???? ??????????? ?????? ???? \\ ?????",
  "?????????? ?? ",
  "?????????? ???????????? \\ ???????????? ",
  "???? ?????? ?????????? \"?????????? ?????? ??????\"?",
  "???? ?????????? /?????? ???????? ???????????? ?????????? ???????? ?????? ?????? ?????? ?????????? ????????? ?????? ????/?????",
  "?????? ?????? ???? /?????? ???????? ??????????????? ?????????? ?????????? \\ ???????????????????",
  "?????? ?????????? ???? ?????? ???????? ??????????? ???????",
  "???????? ???? ???? ???????? ???????????? ",
  "???????? ?????????? ?????????????? ",
  "???????????? ?????????? ",
  "?????? ???????? ",
  "?????? ?????????? ???????????? ?????????? ?????????? ???? ???????????? ?????????",
  "?????? ???????? ?????????? ???? ???????? ???????? ???? ??????????? ??????? ????  ?????????? ?????????? ?????????????",
  "???????? ???????? ",
  "?????????? ???????????? ",
  "?????????? ?????????? ",
  "?????????? ???? ?????? ",
  "???????????? ",
  "?????? ?????????? ?????????????? ???????? ???? ???????????? ???? ???????????",
  "?????? ???? ???????? ???????????? ???????? ?????????? ?????????????",
  "?????????? ?????????????? ",
  "?????????? ?????????? ",
  "?????????? ?????????? ?????????????? ",
  "?????????????? ???????????????????? ????????????... ",
  "???????? ?????????? ",
  "???????? ???????????? ",
  "?????????????? ?????????? ",
  "?????????? ???????? ",
  "?????????? ???????????? ",
  "???????????? ",
  "???????????? ?????? ???????????? ?????????? ?????????????? ",
  "?????????? ???????????????? ",
  "???????????? ???????????????? ",
  "?????????? ???????????? ???????????? ",
  "?????????? ???????????? ",
  "???????? ??????????  ",
  "???? ???????????????? ?????????????????? ???? ?????????? ???????????????",
  "???? ?????? ???? ???????? ???????? ?????????? ??????????????, ???? ???????? ?????? ???????",
  "???????????? ?????? ?????????????? ",
  "(????) ???????? ?????????? ???????? ",
  "?????????? ???????????? ?????????? ",
  "?????????? ???????????? ",
  "???????????? ???????? ",
  "?????? ???????? ?????????????? ???????? ???????? ??????????\\?????????? ???? ???? ?????? ?????????? ?????????????????",
  "?????? ???? \\ ?????",
  "?????????? ?????????? ",
  "?????????? ?????? ?????????? ",
  "?????????? ?????????????? (?????????? ) ",
  "???????? ???????????? ",
  "???????? ???????????? ???? ",
  "?????? ???????? ???????????? ?????? ?????? ?????????????",
  "?????? ?????? ?????????? ???????????? ???? ?????? ???????? ?????????",
  "?????? ???????? ?????????? ???? ?????",
  "???????????? ?????? ?????? ",
  " ???????????? ?????? ??????",
  "???????? ???????????? ?? ",
  "?????????? ???????????????? ",
  "???????? ???????? ",
  "?????? ???????? ???????? ???????? ???? ???????? ???????????????? (??????????, ??????????, ????????????, ???????????????? )?",
  "???????? ???? ???????? ",
  "???????? ?????????? ????????????  ",
  "???????????? ?????????? \\ ?????????? ",
  "???????????? ???????????? ",
  " ?????????? ???????????? ",
  "???????????? ?? ",
  "?????? ?????????? ?????????? ??????????????? ?????? ????\\????? ???? ???????? ?????? ???????? ?????????? ???????????????",
  "?????????? ( ??????????\\??????????\\?????????? ) ",
  "?????????? ",
  "???????????? ?????????? ",
  "?????????? ???????? ",
  "?????????? ???? ???????????? ",
  "?????????? ?????????????? ",
  "?????????? ???????????? ",
  "???? ???????????????? ?????????????????? ???? ?????????? ???????????????",
  "???????????? ?????????????? ",
  "?????????? ?????????? ",
  "?????????? ???? ???????? ",
  "???????????? ???????? ",
  "?????????? ???????????? ???????????? ",
  "?????? ???????????? ???????????? ???????? ?????????? ???????? ??????? ?????? ???? \\ ?????",
  "?????????? ?????????????? ",
  "???????????? ???????????????? ",
  "?????? ?????????? ",
  "?????????? ?????????? ",
  "???????? ???????? ",
  "?????? ?????????? ",
  "???? ?????? ?????????? ?????????????",
  "???? ?????????????? ?????? ?????? ?????????????? ???????",
  "?????????? ???????????? ",
  "?????????? ?????????? ",
  "?????? ?????????? ",
  "?????????? ?????????? ",
  "?????????? ?? ",
  "?????? ???????????? ???????????? ???? ?????????? ?????????????? ?????????",
  "?????? ???????????? ?????? ???????????? ?????????",
  " ?????????? ???????? ",
  "???? ?????? ???????? ?????? ??? ?? ???. ",
  "???????????? ?????????????? \\ ???????????????? ",
  "?????????? ?????? ",
  "???????? ???????? ",
  "?????? ???????????? ???? ???????????? ???????? ???????? ?????????????? ???????",
  " ?????????????? ?? ",
  "???????? ???????? ????????? ?????",
  "???????? ???????? \\ ???????? ???????? ",
  "???????????? ??????????\\???????? ",
  "???????? ???????????? ",
  "???? ?????? ????????: ?????????? ?????? ???? ?????????? ???? ?????? ????????? ???????",
  "???????????? ?????? ???????? ????? ????????? ",
  " ???????????? ?????????? ",
  "???????? ?????????? ",
  "?????????? ",
  "?????????? ???????????? \\ ???????? ?????????? ",
  "?????? ?????????????? ?????????? ???? ???? ???????? ?????????? ???????? ???????",
  "?????????? ?????????? ???????????? ?????????",
  "???????????? ?????????? ",
  "???????? ???? ???????? ??????????????  ",
  "???????? ",
  "???????? ???? ???????? ????? ",
  "???????? ???????? ",
  "?????? ???? ?????? ???????? ?????????? ???????????",
  "?????? ?????????? ?????????? ?????????? ?????? ???????? ?????????? ???? ?????",
  "?????? ???????????? ????? ????????? ",
  "?????????? ???????????? ",
  "?????????? ???????? ",
  "???? ???? ?????????? ???? ???. ?????? ",
  "?????????? ?????????? ",
  "???? ?????? ?????????? ???????? ?????????? ?????????",
  "???? ?????? ?????????? ?????? ????????? ",
  "?????? ???????????? ???????? ???????? ???????????",
  "?????????? ?????? ",
  "???????? ",
  "????????\\?? ???????????? ",
  " ???????????? ???? ???????? ",
  "?????? ?????????????? ?????????? ?????????? ???????? ???? ?????????? ??????????????????? ???????",
  "???? ?????? ???????? ???????? ?????? ???????????? ???????????? ?????? ??????? ?????? ???? \\ ?????",
  "?????????? ?????????????????? ",
  " ?????????? ?????????? ???????? ",
  "?????????? ???????? ",
  "?????????? ???????????? ",
  "??????\"?? = ???????? ???????????? ",
  "???? ?????? ?????????? ???????????? \\ ?????????? \\ ?????????",
  "?????? ?????????????? ?????????? ?????????? ???? ?????????? ??????????? ???????",
  "?????????? ?????????? ",
  "?????????? ",
  "?????????? ?????????? ",
  "???????????? ?????? ?? ",
  "???????? ???????? ",
  "???? ?????? ?????????? ???????????? \\ ?????????? \\ ?????????",
  "?????? ?????????????? ?????????? ?????????? ???? ?????????? ??????????? ???????",
  "?????????? ?????????? ",
  "?????????? ",
  "?????????? ?????????? ",
  "???????????? ?????? ?? ",
  "???????? ???????? ",
  "???????? ?????????? ?????? ?????????? ????????? ???????",
  "???? ?????? ??????? ???????",
  "???? ?????????? ???????????????? ???????",
  "???????? ?????????? ",
  " ???????????? ?? ",
  "???????????? (????) ???????????? ",
  "?????????????? ???????????? ",
  "???????????? ?? ",
  "???? ???????? ?????????? ?????? ?????????? ????????? ",
  "( ???????????? ???????????? ???? ???????????????? )",
  "?????????? ?????????? ",
  "???????????? ?????????? ?????????? ",
  "?????? ???????? ?????????? ",
  "???????????? ?????????? ",
  "?????????? ?????????????? ",
  "?????? ???????????? ?????????? ???????? ??????????? ?????? ???? \\ ?????",
  "?????? ???????????? ???????? ???????????? ???????????? ???? ???????????? ?????? ???????????? ???????? ??????????? ?????? ????\\?????",
  "?????????? ?????????? ",
  "?????????? ???? ???????????? ",
  " ?????????? ?????????? ",
  "???????????? ???? ????????????  ",
  "?????? ?????? ",
  "???? ???? ???????? ???????? ???????? \\ ???? ?????????",
  "?????? ?????????? ?????????? ???? ???????? ???????? ????????? ???????",
  "?????? ?????????? ?????????? ?????? ???????? ???????? ???????? ?????????",
  "?????????? ???????? ???????? ???????? ",
  "???????????? ???????????? ",
  "?????????? ???????????? ",
  "???????? ?????? ???????? ",
  "???????????? ???????????? ",
  "?????????? ???????????? ",
  "???? ?????? ?????????? ???????????",
  "???? ?????? ???????????? ???????? ??????? ",
  "???? ?????? ???????????? ???? ????????????? ???????????? ?????????? ?????????? ???? ???????????",
  "?????????? ???? ?????????? ???????????? ",
  "???????? ???????? ",
  "?????????? ???? ?????????? ?????????? \\ ?????? \\ ??? ",
  "???????????? ???? ?????????? ?????????? \\ ?????? \\ ??? ",
  " ???????????? ?? ",
  "???? ?????? ???????? ??????????? ?????? ???? ???????? ???????????????",
  "???? ???????? ???????? ???? ?????????? ???????????",
  "???? ???????? ?????????? ?????? ?????????? ???????",
  " ???????????? ???? ?????????? ?????????? ",
  "?????????? ?????????? ???????? ",
  "???????? ???????? ???????? ?????????? ",
  "???????????? ?? ",
  "???????? ???? ?????????? ?????????? ",
  "???? ???????? ?????? ?????? ?????????? ???????? ?????????",
  "?????? ?????? ?????????? ???? ?????????????? ?????????",
  "???? ???????? ?????????? ?????????? ?????????????? ???? ???????",
  "?????? ?????????? ",
  "???????? ?? ",
  "???????????? ???? ???????????? ????? ",
  "????????  ",
  " ???????? ?????????? ?? ",
  "?????????? ???????????? ",
  "???? ???????? ?????? ?????????????? ???? ???????????? ???????",
  "?????? ???????? ?????????? ???????????? ?????????",
  "?????? ?????? ???????????? ?????????? ???? ???????? ?????????",
  "???????? ?????????? ",
  "???????? ?????????? ",
  "?????? ???????????? ",
  "?????????? ???? ???????? ",
  "???????????? ",
  "?????? ???????????? ????????? ?????? ???? \\ ?????",
  "???????? ???? ???????????? ???? ????????\\????????  ???????? ???????????? \\ ???????????? ??????????.",
  "?????? ???????????? ",
  "???????? ?????? \\ ???????????? ???????? ",
  "(????) ???? ???? ???????? ",
  "?????????????? ?????????????? ",
  "?????????????? ?????????? ",
  "?????? ?????????????? ?????????? ???????? ???? ???????? ????????????? ???????",
  "???? ???????????????? ?????????????????? ???? ???????????? ???????? \\ ?????????????",
  "???? ???????????? ???????????? ?????????????",
  "????",
  "?????????? ?????? ?????? ",
  " ?????????????? ?????????????? ",
  "???????????? ?????????????? ",
  "?????? ?????????????? ???? ?????????? \"?????? ???? ???? ???????? ????????\"?",
  "?????? ?????? ???????????? ???? ?????????? ??????? ",
  "???? ???????? ?????? ???????? ???????? ?????? ?????? \\ ???????????? ?????????????",
  "?????????? ?????????? ",
  "???? ???????????? ?????????????? ?????? ",
  "?????????? ?????????? ",
  "?????????? ?????????????? ",
  "???? ???? \"???????? ????\"?",
  "???? ???? ???????????? ?????????",
  "???????? ???????????? ????\\?? ???????? ??????????? ???????",
  "?????????? ???????????????? ",
  "?????????? ???????????? ",
  "?????????? ???????????? ",
  "?????????? ?????????????? ?? ",
  "?????????? ???????????? ( ?????????? ) ",
  "?????? ???????? ???????????? ?????????????? ?????????",
  "?????????? ???????????? ?????????? ???????????? ????????? ???????",
  "?????? ???????? ",
  "???????????? ???????????? ",
  "???????????? ???? ",
  "???????????? ?????????? ",
  "???????? ???????? ???????????? ",
  "?????? ???????? ???????? ???????????? ???????????",
  "???????? ???????????? ?????????? ?????? ???? ????? ?????? ???? ???????????? ???? ???????????",
  " ???????? ???????????? ?????????? ",
  "?????????? ???????????? ?????????? ",
  " ?????????? ???????? ",
  "???????????? ",
  "???? ???? ?????????? ???????????",
  "?????? ???? ?????????????? ???? ?????????? ?????????",
  "???????? ???????????????? ",
  "???????? ?????????? ",
  "???????????? ?????????????????? ",
  "???????????? ",
  "?????????? ???????? ???????????? ",
  "?????? ???????????? ?????????? ?????????? \\ ???????????",
  "?????? ?????? ???????????? ?????? ?????????? ??????? ?????? ????\\?????",
  "???? ???? ?????? ?????? \\ ???????? ?????????",
  "?????????? ?????????????? ",
  "???????? ?????????? ???? ",
  " ?????????? ???????? ",
  "???????? (????) ???????? ",
  "???????????? (????) ???????????????? ",
  "???? ???????? ?????????? ?????????????",
  "???????? ???? ???????? ????????????????.",
  "?????? ?????????? ???? ?????????",
  "???????????? ???????????? ????? ",
  " ?????????? ????????????  ",
  "???????? ???????? ???? ???????????? ??????? ",
  "?????? ???????? ",
  "???????? ?????????? ???? ???????????? ???????????? ??????? ",
  "?????? ?????????? ?????? ?????????? ???????????? ??????? ???????? ???????????",
  "???? ?????? ???????? ???????????? ???????????????? ?????? Netflix ? ?????? ???????? ?????????? ?????? ?????????? ???????????",
  "?????? ?????????? ???????? ?????????? ???????? 20 ???????",
  "?????????? ???????????????? ",
  "?????????? ???????? ???? ?????????? ",
  "?????????? ???????????? ?????????? ",
  "?????????? ?????????? ",
  "???? ???????? ??????: ?????????? ?????? ???? ?????????? ???????",
  "?????? ?????????? ?????????? ?????? ???????? ?????????? ???????????????",
  "?????? ???????? ",
  "?????????? ???????? ",
  "???????? ?????????? ???????????? ",
  "???????????? ???????? ?????????? ",
  "?????? ???????????? ???????????? ???????? ???????????? ???????? ???? ???????? ?????????? 20 ???????",
  "???? ?????????? ???????????? ???????????? ??20 ???????? ?????????????????",
  "?????????? ???????????? ",
  "?????????? ?????????? ???????????? ?????????? ?????? ",
  "?????????? ?????????????? ?????????? ",
  " ???????????? ?????????????? ",
  "?????????? ???????????? ?????????? ",
  "?????? ???????????? ???????????",
  "?????? ?????? ???????????? ???????? ?????? ???????????",
  "???? ???????? ???????????? ???????? ???????????( ????????, ????????????, ?????????? )",
  "?????????? ?????????? ???????? ",
  "?????????? ?????????????? ",
  "?????????? ?????????? ",
  "?????????? ???????? ",
  "???? ???????????????? ?????????????????? ???? ?????????? ??????????????????\\??????????????\\?????????????",
  "???????? ?????????? ?????? ??????????????? ???????",
  "???????????? ?????????? ",
  "???????????? ???????????? ?????? ?????????? ",
  " ?????????? ?????? ",
  "???????????? ?????????? ",
  "?????? ?????????? ???????? ???????? ?????????? ?????????? ?????????? ???????? ??????????? ???????",
  "?????? ???? ?????????? ?????? ?????? ???????? ?????????? ?????????? ?????? ???????",
  "???????? ?????????? ???? ",
  " ???????????? ?????????????? ",
  "?????????????????? ???????????? ",
  "?????????????? ?????????? ???????????? ",
  " ???????? ?????????? ???????? ",
  "?????? ???????????? ?????????? ?????????????",
  "???????? ???????????? ?????? ???????????? ???????? ???????",
  "?????? ???????? ???????????????? ???????? ?????????? ??10 ???????? ?????????????????",
  "???????????? ?????????????????? ",
  "?????? ",
  "???????? \\ ???????? ?????????????? ",
  "???????? ???????????? ",
  "?????????? ?????????????? ",
  "?????????? ???????? ",
  "?????? ?????? ?????????????? ???????? ?????????? ?????? ???????? ???? ?????????? ???? ???? ???????",
  "?????? ???? ?????? ?????? \"???????????? ???? ????????\" ???? ?????? ???? ?????????? ???? ???????",
  " ?????? ???????? ",
  " ?????????? ???????? ???? ?????????????? ",
  "???????????? ?????????????? ",
  "?????????? ???? ?????? ",
  "???????????? ?????????????? ",
  "?????? ???????????? ?????????? ???????????? ???? ?????? ???????? ????????? ???????",
  "?????? ?????????? ???????????? ?????????????? ???????? ???? ???????? ?????????? ???????????? ?????????",
  "?????????? ???????????? ???? ?????????????? ",
  "???????????? \\ ?????? ",
  "?????????? ?????????? ",
  " ?????????????? ?????? ?????? ",
  "???????? ?????? ",
  "?????? ???????????? ?????????? ???? ???????????????? ??????????????? ???? ?????? ???????????? ???? ???????????? ?????????????",
  "?????? ???????????? ???? ?????? ???????? ???????????? ????????? ?????? ???????????? ?????????? ??????????????? ",
  " ?????????? ???????????? ",
  "???????????? ???? ?????? ",
  "???????????? ?????????????? ",
  "?????? ( ???? ) ??????????.?? ?????????????? ?????????????? ",
  "???????? ???? ???????? ",
  "???????? ?????????? ?????????? ?????? ?????? ???????? ???????",
  "???????? ?????????? ???????? ?????????? ???????? ?????? ?????? ???????????? ?????? ???????? ?????? ???? ???????????? ?????????????",
  "???????? ?????????? ???????????? ?????? ???????????? ???????????? ?????????????",
  " ???????????? ?? \\ ????????.?? ?? ",
  " ???????????? \\ ????????.?? ",
  "?????????????? ???? ?????? ???????? ",
  "?????????? ????????.?? ????? ",
  "?????????? ???? ?????????? ???????? \\ ???????? ",
  "???? ?????????????? ?????????",
  "???????? ???????????? ?????????? ???????? ?????????? ?????? ?????????????? ???? ?????????? ???????????? ?????????",
  "?????????? ",
  "?????????? ?????? ?????? ",
  "?????? ?????????? ",
  "?????????????? ?????????????? ",
  "???????? ???????? ",
  "?????????? ???????? ???????????? ",
  "???? ?????? ???????????? ?????????? ?????? ?????????? ???????????? ?????????? ???????????? ?????? ???????? ???????? ???????",
  "???????? ?????????? ?????? ?????????? ?????? ???????????? ???????? ???????????????? ???????????? ???????????",
  "???????????? ?????????????? ",
  "?????????? ???????? ",
  "?????????? ?? ",
  "???????????? ?????????? ",
  "?????????? ?????????? ",
  "???? ?????? ?????????????? ???????????????? ???????? ?????????????? ???????????",
  "???????? ???????????? ?????????? ???????????? ????????????? ?????? ?????????? ???? ?????",
  "???????? ???????????? ?????????? ???? ????????????? ???????",
  "???????????? ???????? ",
  "?????????? ???????????? ",
  "?????????? ??",
  "?????????? ??",
  "???? ???????????? ???????? ???????? ??????.. ",
  "???? ?????? ???????????? ???? ?????????? ???????????? ??????????? ???? ?????",
  "?????? ?????? ?????????? ???? ?????",
  "???? ???????? ?????????? ?????? ???????????? ???? ?????????????? ???????? ???????????? ?????????????",
  "?????????? ?????????? ",
  "?????????? ",
  "?????????? ?????????? ",
  "?????????? ?????????? ",
  "????  ?????????? ?????????? ",
  "???? ???????????????? ???????? ??????????? ?????? ???? ?????????????? ???? ?????????????? ?????????????? ?????????",
  "?????? ???????????????? ???????? ?????????? ???? ????????? ?????? ???? \\ ?????",
  "?????????????? ",
  "?????????? ???????????? ",
  "?????????????? ???????????? ",
  "???????????? ??????????? ",
  "???????? ?????????? ",
  "???? ???? ?????? ??????????????? ???? ?????????? ?????? ??????????? ???????",
  "???????? ?????????????? ???? ???????????? ????????? ???????? ????????????, ?????????? ???????????????",
  "???? ?????? ?????? ?????????? ???? ???? ?????? ?????????? ???? ???????????? ???? ?????????????? ????????? ",
  " ?????????? ?????????? ",
  "???????? ?????????? ",
  "?????? ???????? ",
  "???????? ???? ???????? ????? ",
  "?????????? ",
  "?????? ???????????????????",
  "?????? ?????? ?????????? ???????? ?????????? ???????????",
  "?????? ?????? ?????????? ?????????????????? ???????? ???????",
  "???????? ?????????? ",
  "???????????????? ",
  "???????? ?????????? \\ ????????  ",
  "?????????? ??????? ",
  " ?????? ?????????????? ",
  "???? ?????? ???????????? ???????????",
  "?????? ???? ?????? ?????????? ???? ???????????",
  "?????? ???????? ",
  "???????? ?????????? ????? ",
  "???????????? ",
  "?????? ?????????? ",
  "?????????? ?????????????????? ?????????????? ",
  "???? ?????? ???????????? ???????????",
  "?????? ???? ?????? ?????????? ???? ???????????",
  "?????? ???????? ",
  "???????? ?????????? ????? ",
  "???????????? ",
  "?????? ?????????? ",
  "?????????? ?????????????????? ?????????????? ",
  "???? ?????? ???????????? ???????",
  "???? ???? ?????????????? ?????????",
  "???????? ?????????? ?????? ???????????? ?????????? ???????????",
  " ( ????????, ??????????????, ???????????? ?? ?????? )",
  " ?????????? ?????????????? ",
  "???? ??????????.?? ?????????? ",
  "???????? ???????? ?????????????? ",
  "???????? ",
  " ???????? ???????????? ???????? ???? ",
  "?????? ?????????",
  "???????? ?????????? ?????? ???????????? ???????? ???????",
  "?????? ?????????? ???????????? ???????????",
  "?????? ???? ?????????????? ???????????",
  "???????? ???????? ",
  "?????????? ???????????? ?? ",
  " ?????????? ???? ???????? ",
  "?????????? ???????? ",
  " ?????????? ???????????? ",
  "???? ???? ?????????????? ?????????? ???????? ???????????????? ?????????? ???????????",
  "?????? ???????????? ?????????? ?????????????? ?????????? ?????????",
  "???????? ???? ???????? ",
  "?????????? ?????????? ",
  "?????????? ?????????? ???????? ?????????? ???????? ",
  "???????? ",
  " ???????????? ?????????? ?????????? ",
  "?????? ???????? ?????????? ???? ?????????? ?????????????? ?????????",
  "?????? ???????? ???????? ????????????? ???????",
  "???????? ?????????? ?????????? ???? ??????? ???????",
  " ???????? ???? ?????????????? ",
  "?????????????? ???????? ",
  "???????????? ???? ???????? ???????? ",
  "???????????? ?????? ??",
  " ?????????? ???????????? ",
  "???? ?????? \"??????????\"?",
  "?????? ???????????? ??????????? ?????? ???? \\ ?????",
  "?????????? ???? ?????????? ???????? ",
  "?????????? ?????????? ",
  "?????????? ?????????????? ",
  "?????????? ?????????????? ",
  "?????????? ???????????? ",
  "?????????? ?????? ???????? ???????? ?????????????????????????",
  "???? ?????? ???????????? ???? ?????????? ???????????? ???????????? ?????????",
  "?????????? ???????????? ",
  "?????????? ?????????? ",
  " ?????? ???? ?????????? ?????????? ",
  " ?????????????? ?????? ?????????? ???????????? ",
  "???????? ?????????? ",
  "?????? ???????????? ?????????? ???????? ???? ???????????? ???????? ??????????? ???????",
  "?????????? ???? ???????? ",
  "???????????? ?????????? ",
  "???????????? ?????????????? ",
  "?????????????? ?????????? ???????????? ",
  "???????? ???????????? ?????????? ",
  "???? ?????? ???????????????????????",
  "???? ?????? ???? ?????? ?????????????????????",
  "???? ?????? ???? ???????? ?????? ???????????????????? ???????? ?????????????",
  "?????????? ???????????????? ",
  "???????????? ?????????? ",
  "?????????? ?????????????? ",
  "???? ?????????? ??",
  "???????? ?????????????????????? ?????????? ",
  "?????? ???? ?????? ???????????????????? ???????? ???????? ?????? ???????? ???? ?????????? ???????? ?????? ??????????? ",
  "???? ?????? ??????????????:  ???????? ?????? ???????? ???? ?????????? ???????? ?????? ???????????",
  "?????? ?????????? ?????? ???????? ??????????????????????? ???????",
  "???????????? ?????? ?????????????? ",
  "?????????? ?????????? ",
  "?????? ???????? ",
  "?????????? ?????????? ",
  "?????????? ?????????? ???????????? ",
  "?????? ?????????????????????? ?????? ?????????? ?????????? ???? ???????????",
  "?????? ???????? ???????? ???????????????????????",
  " ???????????? ???? ???????????????????????? ???????? ",
  "?????????? ?????????????? ",
  "??????????.?? ?????????????? ",
  " ???????? \"???????? ??????\" ",
  "???????? ???? ???????????????????????? ????????????????? ",
  "?????? ???? ?????? ?????? ?????????????????????? ???????? ?????????? ???? ???? ???????",
  "?????? ?????????? ?????????????????????? ???? ???????? ???????????? ???????? ???????????????",
  "?????????? ?????? ",
  "?????????? (????) ???????????? ???? ???????? ???????????????? ",
  "?????? ?????????????? ?????? ...?? ",
  "???????? ?????????? ",
  "?????? ??..., ???????",
  "?????? ?????????????????????? ???????????",
  "?????? ?????? ?????????? ?????? ???????????",
  "?????????? ?????????????? ?? ",
  "?????????? ?????????? ",
  "???????? ???? ???????????? ???????? ",
  "?????????? ???????? ???????????? ",
  "?????????? ?????????? ",
  "?????? ?????????????????????? ?????????? ?????? ?????????? ???????????????",
  "?????? ???????? ???????? ?????????",
  "???????? ???????????? ",
  " ?????????? ?????????? ",
  "?????????? ???????? ?? ",
  "???????? ?????????? ?????????????? ???????? ???????? ",
  "( ???? ) ???? ?????? ?????????? ???????? ",
  "???????? ?????????? ???????????? ",
  "?????? ???????????? ?????????? ???????????",
  "?????? ?????? ???????????? ?????????? ???????????? ?????????",
  "?????????? ?????????? ????/?????? ??????????? ???????",
  "?????????? ?????????? ",
  "?????????? ???????????? ",
  "??????????.?? ????????????.?? ",
  " ???????????? ??????...????? ",
  "?????? ???? ?????????? ?????????????? ???????????? ??????????????? ???? ?????",
  "?????? ???????? ???????????? ???????????? ?????????????? ??????????? ",
  "?????????? ?????????????? ",
  "?????????? ?????????????? ",
  " ???????????? ???????????? ",
  " ?????????? ?????????????? ",
  "?????????? ( ???? ) ?????????? ",
  "???? ???? ???????",
  "???? ???????? ?????? ???????????",
  "?????? ???? ???????? ?????? ??????????? ?????? ?????????????? ???? ???????????",
  " ?????????? ?????????? ",
  "???????? ???????? \"??????????\" ",
  " ???????? ?????????? ?? ",
  "?????????? ?????????? ",
  "?????????????? ?????????????? ",
  "???? ???? ???????????",
  "???? ???????? ?????? ???????????????",
  "?????? ???? ?????????????? ?????????????",
  "???? ???????? ?????? ?????????? ???????????????????",
  "?????? ???????????? ",
  "?????????? ???????? ???????? ",
  "???????? ???????????? ",
  "?????? ?????????? ???????? ",
  "?????????????? ",
  "???? ???? ???????? ???????????",
  "?????? ?????????? ?????????????? ???????? ???????????",
  "???? ???? ?????????? ?????????? ???????????",
  "( ????) ?????????????? ?????????? ???????? ?????????? ",
  "?????????????????? ???????????? ",
  "?????????????? ?????????? ",
  " ???????????? ?????????????? ??/ ??????????...",
  "???? ?????? ???????????",
  "?????? ?????? ?????????",
  "?????? ?????????? ?????????????? ???? ???????? ?????????",
  "?????? ???????? ?????????? ?????? ?????????????? ???? ?????????? ??????? ",
  " ?????????? ???????? ?????????? ",
  "???????? ?????????? ???? ???????????? ",
  " ?????????? ?????? ?????????????? ",
  "???????????? ",
  "???????? ?????????? ?? ",
  "???? ?????? ???????????",
  "?????? ?????? ?????????????? ?????????? ?????????????",
  "?????? ???????? ?????????? ???????????? ???? ?????????",
  " ?????????? ?????????? ",
  "???????? ???????????? ???????????? ",
  " ???????????? ???????????? ????????????...????????????/?????????? ",
  " ???????????? ?????? ?? ",
  "???? ?????? ???????????????",
  "?????????? ???? ?????????? ???????????? ???????????????",
  "?????? ???????? ???????? ???? ???????????? ?????????",
  "???????? ???????????? ???? ?????? ?????? ",
  "???????????? ?????????? ",
  "???????????? ?????????????????? ???????? ",
  "???????????? ???????????? ",
  "???????????? ???????????? ???? ?????????? ",
  "???? ???? FOMO?",
  "?????? ?????? ???????????? ??FOMO? ???????",
  "?????? ?????????? ?????????????? ???????????? ???????????? ?????????? ???????? ???????? ?????????????",
  "?????? ???????????? ",
  "?????????? ?????????? ???????? ",
  "???????? ?????????? ",
  "???????? ",
  "?????????? ?????????? ",
  "?????? FOMO ?????????? ???? ?????????? ???????????????? ?????????",
  "?????????? ???? ???????????? ???????????? ",
  "???????? ???????????? ???????? ",
  "?????????????? ???????? ???????? ",
  "?????????? ?????????? ???? ",
  "?????? ???? ???????? ???????? ?????? ???????????? ??????????? ???????",
  "?????? ???? ???????? ?????? ???????",
  " ???????????? ?????? ?? ",
  "???????????? ???? ???????????? ",
  "?????? ?????????? ???????? ",
  "???????? ?????????? ?? ",
  "?????? ???????? ???????????? ???? ?????? ???????????? ??????????? ???????",
  " ?????????? ???? ???????????????? ?????????? ",
  "???????? ???????????? ",
  "?????????? ???????????? ?????????????? ",
  "?????????? ",
  "???? ?????? ????????????????? ",
  "?????? ?????????? ????????????????? ???????? ?????",
  " ?????????? ???????? ???????????????? ",
  " ?????????????? ?????? ???????? ",
  "?????? ?????????? ???????? ",
  "???????????????? ?????????? ",
  "?????? ?????????? ?????????? ?????????? ???????????????????",
  "?????????? ???????????? ???????? ",
  "???????????? ???? ?????????????? ???????????? ",
  " ?????????? ?????????????????? ",
  "?????????? ???????? ?????????? ?????????? ?????????? ",
  "?????? ???????????????? ???? ?????? ?????????? ???? ???????????",
  "?????? ???????????????? ?????????? ?????????? ?????????????",
  "?????? ???????????? ???????",
  "???????? ?????????? ?? ",
  "???????? ?????????? ?????????? ???? ?????????? ",
  "?????????? ???????????? ",
  "???? ???????????? ?????????? ",
  "???? ???????????????? ???? ?????????????????",
  "???????? ???????????????? ???????????? ?????? ???????????? ???????",
  "?????????? ?????????? ",
  " ???????????????? ???? ?????????? ",
  "?????????????? ?????????????? ???? ???????????? ",
  " ???????????? ???????????? ?????????????? ",
  "?????? ?????? ???????????? ?????????????",
  "?????? ???????????? ???? ???? ???????????????? ???? ???????????? ???? ?????????? ???????",
  "?????????? ???? ???? ????????????????  ",
  "???????? ?????????? ???????????? ",
  "?????????????? ?????????? ?????????? ",
  "?????????? ?????? ",
  "?????????? ???????????? ",
  "?????? ?????? ?????? ?????? ???????? ?????????????? ???? ???????? ??????? ",
  "???????? ?????????? ???????????? ",
  "???????? ?????????? ???????????????? ",
  "???????????? ?????????????? ",
  "???????? ???????????? ?????????? ",
  "???????? ?????????? ",
  "?????? ?????? ?????? ???????? ????????????? ?????? ?????????????? ???? ?????????????? ???????? ????????? ",
  "???? ???????? ?????????? ?????? ???????? ?????????????",
  "?????????????? ???? ???????????? ",
  "?????????? ???????????? ?????? ?????????????????? ",
  "???????????? ???????????? ",
  "???? ?????????? ???????? ???????????? ",
  "?????? ???????? ?????????? ???????? ????????????????????",
  "???????????? ???????? ???????? ",
  "?????????? ???? ???????????? ?????????? ",
  "?????????? ???????????? ?????????? ",
  " ???????????? ???????? ???? ???? ?????????? ???????????? ",
  "???? ?????? ?????????????????",
  "???? ?????? ?????????? ???????????????",
  "?????? ???????????????? ?????????? ?????????? ?????? ???????????",
  "???????????????? ",
  "?????????? ?????????????? ",
  " ???????? ?????? ",
  "?????????? ???????????? ",
  "?????????? ?????? ???????? ",
  "???? ?????? ???????? ???????????????",
  "?????? ?????? ?????????????????",
  "?????????????? ?????????? ",
  "?????????? ?????????? ?????????? ",
  "?????????? ",
  "?????????? ?????? ",
  "?????? ???????????????? ?????? ?????????? ?????????? ???? ???????????",
  "?????? ?????? ???????????????",
  " ?????????? ?????????? ",
  " ?????????? ?????????? ",
  "?????????????? ",
  "?????????? ?????????? ",
  "?????? ???????? ???????? ?????????? ?????????? ??????????????? ???????",
  " ???????? ",
  "?????????? ???????????? ",
  "?????????????????? ",
  "?????????? ???????????? ",
  "???? ???? ?????????????",
  "?????? ???? ?????? ???????? ???? ?????? ?????? ???????? ???????? ?????????????",
  "?????????? ?????????? ",
  "???????? ???????? ???????? ??????????  ",
  "?????????? ???????? ?? ",
  "?????????? ?????????????? ",
  " ?????????? ?? ",
  "?????? ?????? ???????????????",
  "?????? ???? ?????? ?????????? ???????????",
  "???????????? ?????????? ",
  "?????????????? ",
  "?????????? ?????????? ?? ",
  "??????????  ???????? ",
  " ???????????? ?????????? ?????????? ",
  "?????? ???????? ?????????? ???????????? ?????? ?????????????",
  "?????? ?????? ?????? ???????????? ???????? ???????????????",
  "?????????????? ",
  " ?????????? ?????????? ",
  "???????? ???????????? ",
  "?????????? ?????????? ???????????? ",
  "?????? ???????????? ???????????? ???? ?????????? ",
  "?????? ???????? ???????? ???????????? ?????? ???????? ??????????? ?????? ???? /?????",
  "???????? ???????????? ?????????? ?????????? ?????????",
  "?????????? ???? ???????? ???????????? ",
  "???????????? ???????????? ",
  "?????????? ",
  "?????????? ?????????? ",
  "???????????? ???????? ???????",
  "???? ?????? ???????????",
  "???? ?????? ???? ?????? ???????????",
  "?????? ?????? ",
  " ?????????? ?????????? ???????????? ",
  "???????? ???????? ",
  "?????????? ?????????????? ???????????? ",
  " ?????????? ?????????? ",
  "???? ???????? ?????? ?????? ???????? ????????????? ( ???????????? ???????? ?????????????? )",
  "?????? ???? ???????? ?????????????? ???? ?????????? ???????? ????????????? ",
  "???????? ?????????? ?????????? ?? ",
  "???????????? ???????????? ?????????? ",
  "?????????? ???? ???????? ",

  "???????????? ",
  "?????? ?????????? ???????? ?????????? ???????? ?????????",
  "?????? ???? / ?????",
  "?????????? ???????????? ",
  " ?????????? ???????? ",
  " ?????????? ?????? ( ???????? ) ",
  "?????????? ",
  "???????? ?????????? ",
  "???? ???????? ???????????? ???????????? ???????????",
  "???? ???? ????????????? ",
  "?????? ???????????????? ",
  "???????? ???????? ",
  " ?????????? ?????????? ",
  "???????????? ?????????? "
]


# print(sentences[0][1])
# print(str(is_hebrew_char(sentences[0][0])))
# iterate over the list of sentences and call the function hebrew_text_from_google
for i in sentences:
	hebrew_text_from_google(i)
