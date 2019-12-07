# PAD
OutbreakPAD (Outbreak Predictor And Detector) is a Python 3 library. This library functions to detect and predict hospital acquired infectious outbreak events.

# Download and install
##  in linux
  ```bash
  git clone https://github.com/pandafengye/OutbreakPAD.git    
  cd OutbreakPAD  
  python setup.py install 
  ```  
# Example
  ```python
  from OutbreakPAD import *
  #    Forecasting with ARIMA-GRNN (recommended)
  OutbreakPAD.PAD(example,p=2,d=0,q=1,a="ARIMA-GRNN",pvalue_cusum_k=1.5) 
  
  ```
# OutbreakPAD input file
The input file is a time series (Column 1, date; Column 2, case number), as follows:
```python
  2014-01-01     3
  2014-01-02     1
  2014-01-03     3
  2014-01-04     1
  ……
  2014-08-15    30
  2014-08-16    26
  2014-08-17    30
  2014-08-18    26
```
# OutbreakPAD output file

The output of OutbreakPAD is a folder labelled “Outbreak_result”, which contains the subdirectories. The folder, “History_record”, contains the detected outbreak events that had already taken place within the time series. The folder, “Prediction”, contains the results predicting whether an outbreak would occur at the end of the time series.
# Note:
It is strongly recommended that the folder, “Outbreak_result”, be immediately renamed subsequent to running the program; if this is not done, the resulting folder produced following the program’s last operation would be overwritten.

