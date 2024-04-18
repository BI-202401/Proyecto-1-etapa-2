from ..predictor import predict, tokenize, clean_process, clean_vectorize, TextProcessor
import __main__

__main__.tokenize = tokenize
__main__.TextProcessor = TextProcessor
__main__.clean_process = clean_process
__main__.clean_vectorize = clean_vectorize
__main__.predict = predict
