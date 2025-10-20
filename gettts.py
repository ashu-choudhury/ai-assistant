import asyncio
import edge_tts

# Default voice setting
selected_voice = "en-US-JennyNeural"  # Default to an American English Female Voice


async def main(text: str):
    """
    Generates speech from text using the selected Microsoft Neural TTS voice.

    Args:
        text (str): The input text to be converted to speech.

    The function saves the output as "tts.mp3".
    """
    tts = edge_tts.Communicate(text, selected_voice)
    await tts.save("tts.mp3")
    print(f"Audio saved as 'tts.mp3' using voice: {selected_voice}")


def change_voice(name: str):
    """
    Changes the selected voice for TTS.

    Args:
        name (str): The name of the Microsoft Neural voice to switch to.

    Available Voices:
    ----------------
    **English (All Accents) - Microsoft Neural Voices**

    - **American English (en-US)**
        - en-US-GuyNeural       → Male
        - en-US-JennyNeural     → Female
        - en-US-AriaNeural      → Female
        - en-US-DavisNeural     → Male
        - en-US-AmberNeural     → Female
        - en-US-ChristopherNeural → Male

    - **British English (en-GB)**
        - en-GB-RyanNeural      → Male
        - en-GB-LibbyNeural     → Female
        - en-GB-SoniaNeural     → Female
        - en-GB-ThomasNeural    → Male

    - **Indian English (en-IN)**
        - en-IN-PrabhatNeural   → Male
        - en-IN-NeerjaNeural    → Female
        - en-IN-RaviNeural      → Male

    - **Australian English (en-AU)**
        - en-AU-WilliamNeural   → Male
        - en-AU-NatashaNeural   → Female

    - **Canadian English (en-CA)**
        - en-CA-ClaraNeural     → Female
        - en-CA-LiamNeural      → Male

    - **Irish English (en-IE)**
        - en-IE-ConnorNeural    → Male
        - en-IE-EmilyNeural     → Female

    - **South African English (en-ZA)**
        - en-ZA-LeahNeural      → Female
        - en-ZA-LukeNeural      → Male

    - **New Zealand English (en-NZ)**
        - en-NZ-MitchellNeural  → Male
        - en-NZ-MollyNeural     → Female

    **Hindi (hi-IN) - Microsoft Neural Voices**
    - hi-IN-MadhurNeural    → Male
    - hi-IN-SwaraNeural     → Female

    **Other Popular Languages**
    - **Spanish (Spain)**
        - es-ES-AlvaroNeural    → Male
        - es-ES-ElviraNeural    → Female
    - **French (France)**
        - fr-FR-DeniseNeural    → Female
        - fr-FR-HenriNeural     → Male
    - **German (Germany)**
        - de-DE-KatjaNeural     → Female
        - de-DE-ConradNeural    → Male
    - **Japanese**
        - ja-JP-NanamiNeural    → Female
        - ja-JP-KeitaNeural     → Male
    - **Chinese (Mandarin)**
        - zh-CN-XiaoxiaoNeural  → Female
        - zh-CN-YunyangNeural   → Male
    """
    global selected_voice
    selected_voice = name
    print(f"Voice changed to: {selected_voice}")
    return {
        "status": "success",
        "current voice": name,
        "message": f"Voice changed to: {selected_voice}",
    }


def gettts(text: str):
    """
    Runs the TTS generation using the currently selected voice.

    Args:
        text (str): The text to be converted to speech.

    Example:
        gettts("Hello, how are you?")  # Generates speech from text
    """
    asyncio.run(main(text))


