def getdata(choice):
    import pandas as pand

    csv = pand.read_csv('iris.csv')

    if choice is 'measures':
        df_measures = csv[['sepallength','sepalwidth','petallength','petalwidth']]
        measures = df_measures.values
        return measures

    elif choice is 'classes':
        #get the classes and take dummies in a data frame
        tmp_classes = csv[['class']]
        df_classes = pand.get_dummies(tmp_classes)
        classes = df_classes.values
        return classes
    else:
        print("wrong argument")

