import ctypes

NVDA=ctypes.windll.LoadLibrary("./nvdaControllerClient.dll")
def speeck(text):
	NVDA.nvdaController_speakText(text)

