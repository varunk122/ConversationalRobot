import keras.backend as K
def decoder( inputs , top_path = 1 , beam_width = 10):
  """
    inputs : ctc_model_input
    top_path : totol number of predicted strings
    beam_width : width of beam that ctc_decoder should maintain

    ** beam_width must be greater than top_paths
                          """
  predictions = model_ctc.m.predict(inputs)

  decoded_tensor , log_probabilites = K.ctc_decode(predictions , input_length =np.one(predictions.shape[0])*predictions.shape[1] , greedy = False , beam_width = beam_width , top_paths = top_paths)

  return k.eval(decoded_tensor) , k.eval(log_probabilites)

   
