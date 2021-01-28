#list declair
Tools="1. TensorFlow", "2. Apache Spark", "3. MATLAB", "4. Jupyter","5. Matplotlib","6. RapidMiner","7. Scikit-lear","8. Excel","9. BigML","10. DataRobot"
print(Tools)
fileObj=open("datascience.txt", "w")
for top10 in Tools:
    fileObj.write(top10 +" ")

fileObj.close()