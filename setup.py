import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
packages = ["PyQt5", "matplotlib", "numpy", "statistics", "os", "glob", "pandas", "multiprocessing.pool", "warnings", "operator", "pickle", "math", "seaborn", "fpdf", "sys", "PIL",
"wittgenstein", "re", "sklearn", "xgboost", "scipy.sparse.csgraph._validation", "scipy.spatial.ckdtree", "joblib", "time"]

path = "D:\OVGU\Project\KMD\KMD_Final\model"

includefiles = [r'commons/', r'data/', r'img/', r'models/', r'help.txt', r'INSTALL.txt', r'preprocessing.py']

build_exe_options = {"packages": packages, "include_files": includefiles, "excludes": [],}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "G-MARC.py",
        version = "1.0",
        description = "GUI for Model-Agnostic model explanations for Rupture status Classification",
        options = {"build_exe": build_exe_options},
        executables = [Executable("G-MARC.py", base=base)]
        )

#includefiles = [(path,'aneur.csv'), (path,'ice_plot_feat_ei.jpg'), (path, 'load.gif'), (path,'model_details.jpg'), (path,'oops.gif'), (path,'Transformed_dataset.csv'),
# (path,'Transformed_dataset_orig.csv'), (path, 'Transformed_dataset_with_prediction.csv'), (path, 'img/'), (path, 'models/')]


 
#includefiles = [r'counter_factuals.py', r'create_pdf.py', 'generate_ice.py', r'model_info.py', r'model_reliance.py', r'param_range.py', r'preprocessing_final.py', r'aneur.csv', r'commons/',
#r'data/', r'img/', r'models/']

#r'C:\Users\Sachin Nandakumar\Anaconda3\Lib\site-packages\scipy\sparse\csgraph\_validation.py', r'C:\Users\Sachin Nandakumar\Anaconda3\Lib\site-packages\scipy\spatial\ckdtree.cp37-win_amd64.pyd', 
#r'C:\Users\Sachin Nandakumar\Anaconda3\Lib\site-packages\joblib\pool.py'

#, ('C:/Users/Sachin Nandakumar/Anaconda3/Lib/site-packages/scipy/sparse/sparsetools/_csr.so','_csr.so'),
#('C:/Users/Sachin Nandakumar/Anaconda3/Lib/site-packages/scipy/sparse/sparsetools/_csc.so','_csc.so'), ('C:/Users/Sachin Nandakumar/Anaconda3/Lib/site-packages/scipy/sparse/sparsetools/_coo.so','_coo.so'),
#('C:/Users/Sachin Nandakumar/Anaconda3/Lib/site-packages/scipy/sparse/sparsetools/_dia.so','_dia.so'), ('C:/Users/Sachin Nandakumar/Anaconda3/Lib/site-packages/scipy/sparse/sparsetools/_bsr.so','_bsr.so'),
#('C:/Users/Sachin Nandakumar/Anaconda3/Lib/site-packages/scipy/sparse/sparsetools/_csgraph.so','_csgraph.so')] 

#includefiles = [r'C:/Users/Sachin Nandakumar/Desktop/exe/aneur.csv', 'ice_plot_feat_ei.jpg', 'load.gif','model_details.jpg','oops.gif','Transformed_dataset.csv','Transformed_dataset_orig.csv', 'Transformed_dataset_with_prediction.csv'] 
 
# GUI applications require a different base on Windows (the default is for a
# console application).
