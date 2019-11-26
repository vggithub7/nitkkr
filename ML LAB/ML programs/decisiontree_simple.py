from sklearn import tree
x=[[121,65,7],
   [123,61,8],
   [101,55,8],
   [125,59,9],
   [131,61,6],
   [116,63,7],
   [111,96,9],
   [109,56,8],
   [107,58,7],
   [117,62,9]]
y=['Male','Female','Female','Male','Male',
    'Male','Female','Female','Female','Male']

clf=tree.DecisionTreeClassifier()
clf=clf.fit(x,y)
prediction=clf.predict([[120,53,6]])
print('Accuracy=',prediction)