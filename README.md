# Contains the Code and AirSim simulation environment dependencies for simulation

#### Algorithm 
Twin Delayed Deep Deterministic Policy Gradient

#### Maps 
[Easy](https://drive.google.com/file/d/1LigXGvDj0XZvgkffqBwe8XRWRmzMR93P/view?usp=sharing), [Normal](https://drive.google.com/file/d/1KtiHr_qpw37qq3PPiAKzLN9THm2aQZOU/view?usp=sharing), [Hard](https://drive.google.com/file/d/110mekUMdnYr5wNaEGVbsSZpwty12knzX/view?usp=sharing)

#### Instructions 
Run the "td3_per.py" inorder to start the training.

#### Note 
The trained model's stats will be stored in the "save_stat" folder and model will be updated in the "save_model" folder.

#### Requirements
|Module|Version|
|------|-------|
|AirSim|1.5.0|
|TensorFlow-gpu|1.15|
|OpenCV-Python|4.5.4.60|
|Cuda Toolkit|11.0|
|CuDNN|8 (from conda repo)|
|h5py|2.10.0|
|Protobuf|3.20.1|
|Keras|2.2.4|
|msgpack-rpc-python|supporting 1.5.0 (for RPC support in AirSim)|
